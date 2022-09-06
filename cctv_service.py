import queue
import cv2, numpy as np
import cctv_detect
import using_telegram
import threading
import play_sound
from PIL import ImageGrab

def send_message(action_list, src):
    global a_queue, f_queue, p_queue, s_queue, t_queue, first, t
    compare= ['assault', 'fainting', 'property_damage', 'stairway_fall', 'turnstile_trespassing']
    queue_list = [a_queue, f_queue, p_queue, s_queue, t_queue]
    temp = [False, False, False, False, False]
    flag = False

    for v in action_list:
        cat, _ = v.split()
        if queue_list[compare.index(cat)].qsize() == 0:
            flag = True
            temp[compare.index(cat)] = True
            queue_list[compare.index(cat)].put(cat)
            break
    
    if first or flag or not t.is_alive(): #판별될때마다 메세지를 보내면 오류가 나기때문에 30초에 한번씩 보내기로 하였다.
        first = False
        t = threading.Thread(target = using_telegram.send_msg, args=(action_list, src, queue_list, temp)) # 시간이 오래 걸리는 부분을 스레딩으로 처리하여 성능 향상.
        t.daemon = True # if문에서 30초에 한번씩 보내기로 하였는데 그 30초 사이에 끄고 싶을 수 있기 때문에 데몬 스레드로 설정하여 메인 스레드가 꺼지면 꺼지게 하였다.
        t.start()

def cctv_service():
    global a_queue, f_queue, p_queue, s_queue, t_queue, first
    f = open('screen_xy.txt', 'r')
    x1, y1, x2, y2 = map(int, f.readline().split())
    f.close()
    first = True
    a_queue = queue.Queue()
    f_queue = queue.Queue()
    p_queue = queue.Queue()
    s_queue = queue.Queue()
    t_queue = queue.Queue()

    # app_thread = threading.Thread(target = app_run, args=()) # 시간이 오래 걸리는 부분을 스레딩으로 처리하여 성능 향상.
    # app_thread.daemon = True # if문에서 30초에 한번씩 보내기로 하였는데 그 30초 사이에 끄고 싶을 수 있기 때문에 데몬 스레드로 설정하여 메인 스레드가 꺼지면 꺼지게 하였다.
    # app_thread.start()

    while True:
        src = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2))), cv2.COLOR_BGR2RGB)
        det = cctv_detect.detect(src)

        if det is not None:
            dst = cctv_detect.draw_boxes(src, det)
            action_list = cctv_detect.dst_info(det)

            if len(action_list): # 50퍼센트 이상인것만 보낸다.
                if not play_sound.is_singing(): # 노래가 틀어지지 않을때만 노래를 재생시킨다.
                    play_sound.play(action_list) #pygame.mixer는 원래 스레딩이라, 스레딩을 따로 해줄 필요가 없음.

                send_message(action_list, src)
        else: dst = src.copy()

        cv2.imshow('esc is quit', dst)

        if cv2.waitKey(5) & 0xFF == 27:
            break