import cv2, numpy as np
import cctv_detect
import using_telegram
import threading
import play_sound
from PIL import ImageGrab
from flask import Flask, render_template, Response, request, flash
import menu_main


"""
이 파일을 실행해주세요.
"""

app = Flask(__name__)

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def gen_frames(): # generate frame by frame from camera
    f = open('screen_xy.txt', 'r')
    x1, y1, x2, y2 = map(int, f.readline().split())
    f.close()

    while True:
        src = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2))), cv2.COLOR_BGR2RGB)
        det = cctv_detect.detect(src)

        if det is not None:
            dst = cctv_detect.draw_boxes(src, det)
        else: 
            dst = src.copy()

        ret, buffer = cv2.imencode('.jpg', dst)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/occur')
def occur():
    days, assaults, faintings, property_damages, stairway_falls, turnstile_trespassings, totals = [], [], [], [], [], [], []

    f = open('occur.txt', 'r', encoding='UTF-8')
    lines = f.readlines()
    f.close()

    for line in lines:
        day, assault, fainting, property_damage, stairway_fall, turnstile_trespassing, total = line.split()
        days.append(day)
        assaults.append(assault)
        faintings.append(fainting)
        property_damages.append(property_damage)
        stairway_falls.append(stairway_fall)
        turnstile_trespassings.append(turnstile_trespassing)
        totals.append(total)

    return render_template('occur.html', days=days, assaults=assaults, faintings=faintings, property_damages=property_damages, stairway_falls=stairway_falls, turnstile_trespassings=turnstile_trespassings, totals=totals)

@app.route('/result')
def result():
    using_telegram.update_result_c5_c6()
    c1, c2, c3, c4, c5, c6 = [], [], [], [], [], []
    f = open('result.txt', 'r', encoding='UTF-8')
    lines = f.readlines()
    for line in lines:
        day, no, cats, occur, end, who = line.split()
        c1.append(day)
        c2.append(no)
        c3.append(cats)
        c4.append(occur)
        c5.append(end)
        c6.append(who)

    return render_template('result.html', c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, zip=zip)

@app.route('/user')
def user():
    names, cats, chatids, clears, totals, add_days = [], [], [], [], [], []
    korean_list = {"assault": "폭행", "fainting": "실신", "property_damage": "기물파손", "stairway_fall": "계단낙상", "turnstile_trespassing": "무단진입"}
    f = open('id_list.txt', 'r', encoding='UTF-8')
    lines = f.readlines()

    for line in lines:
        name, cat, chatid, clear, total, add_day = line.split()
        names.append(name)
        chatids.append(chatid)
        clears.append(clear)
        totals.append(total)
        add_days.append(add_day)

        change_cat = cat.split(',')
        temp = ''
        for v in change_cat:
            temp += (korean_list[v]+'. ')
        cats.append(temp)

    end_point = len(names)
    return render_template('user.html', names=names, cats=cats, chatids=chatids, clears=clears, totals=totals, add_days=add_days, end_point=end_point, zip=zip)

def app_run():
    app.run(host='0.0.0.0', port=5000)

def start_menu():
    menu_thread = threading.Thread(target = menu_main.main, args=()) # 시간이 오래 걸리는 부분을 스레딩으로 처리하여 성능 향상.
    menu_thread.daemon = True # if문에서 30초에 한번씩 보내기로 하였는데 그 30초 사이에 끄고 싶을 수 있기 때문에 데몬 스레드로 설정하여 메인 스레드가 꺼지면 꺼지게 하였다.
    menu_thread.start()

if __name__ == '__main__':
    using_telegram.init()
    play_sound.init()
    start_menu()
    app_run()

    using_telegram.save()