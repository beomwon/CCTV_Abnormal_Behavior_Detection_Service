import telegram
import cv2
import time
import cvlib
import os

def init():
    global bot
    global user_id_list, user_id_codes, user_send_cats, user_id_names, user_clears, user_totals, user_add_days, user_add_count
    global cat_msg
    global incident_where, incident_c1, incident_c2, incident_c3, incident_c4, incident_c5, incident_c6, code_name_dic
    global occur

    user_id_list, user_id_codes, user_send_cats, user_id_names, user_clears, user_totals, user_add_days = [], [], [], [], [], [], []
    user_add_count = {}
    code_name_dic = {}

    incident_c1, incident_c2, incident_c3, incident_c4, incident_c5, incident_c6 = [], [], [], [], [], []

    now = time.localtime(time.time())
    occur = {
        'date': (str(now.tm_mon) if now.tm_mon>9 else ('0'+str(now.tm_mon))) + (str(now.tm_mday) if now.tm_mday>9 else ('0'+str(now.tm_mday))),
        'assault': 0, 
        'fainting': 0, 
        'property_damage': 0, 
        'stairway_fall': 0,
        'turnstile_trespassing': 0
    }

    incident_where = {
        'assault': 0, 
        'fainting': 1, 
        'property_damage': 2, 
        'stairway_fall': 3,
        'turnstile_trespassing': 4
    }

    f = open('telegraminfo.txt', 'r')
    TOKEN = f.readline()
    bot = telegram.Bot(TOKEN)
    f.close()

    f = open('result.txt', 'r', encoding="UTF-8")
    lines = f.readlines()
    f.close()
    for line in lines:
        if len(line.split()) == 6:
            c1, c2, c3, c4, c5, c6 = line.split()
            incident_c1.append(c1)
            incident_c2.append(c2)
            incident_c3.append(c3)
            incident_c4.append(c4)
            incident_c5.append(c5)
            incident_c6.append(c6)
    

    cat_msg = {
       'assault': '폭행이 감지된 상황입니다.', 
       'fainting': '실신이 감지된 상황입니다.', 
       'property_damage': '기물파손이 감지된 상황입니다.', 
       'stairway_fall': '이용객이 계단에서 넘어진 상황입니다.',
       'turnstile_trespassing': '개집표기 무단진입이 감지된 상황입니다.'
    }
    update_id_list()
    del_old_file()
    print('텔레그램 초기화 완료')

def update_id_list():
    global user_id_list, user_id_codes, user_send_cats, user_id_names, user_clears, user_totals, user_add_days, user_add_count

    f = open('id_list.txt', 'r', encoding="UTF-8")
    user_id_list = f.readlines()
    f.close()
    # clear, total, add_day
    for v in user_id_list:
        user_id_name, user_send_cat, user_id_code, user_clear, user_total, user_add_day = v.split()
        user_id_names.append(user_id_name)
        user_send_cats.append(user_send_cat.split(','))
        user_id_codes.append(user_id_code)
        user_clears.append(user_clear)
        user_totals.append(user_total)
        user_add_days.append(user_add_day)
        code_name_dic[user_id_code] = user_id_name

def del_old_file(): # CCTV 이미지 데이터 보관시간은 일주일이기때문에, 일주일이 지나면 지운다.
    now = time.localtime(time.time())
    compare = str(now.tm_year) + (str(now.tm_mon) if now.tm_mon>9 else ('0'+str(now.tm_mon))) + (str(now.tm_mday) if now.tm_mday>9 else ('0'+str(now.tm_mday))) \
                    + (str(now.tm_hour) if now.tm_hour>9 else ('0'+str(now.tm_hour))) + (str(now.tm_min) if now.tm_min>9 else ('0'+str(now.tm_min))) + '.jpg'

    for root, dirs, filenames in os.walk('send_image'):
        for filename in filenames:
            if int(compare[:8]) - int(filename[:8]) > 7: # 파일이름이 year(4) + month(2) + day(2) = 8 이기 때문에 8까지 잘라서 일주일인지 확인
                os.remove(os.path.join(root,filename))

def data_processing(src): # 이미지 처리하는 부분
    #현재 시간으로 이름 저장
    now = time.localtime(time.time())
    image_name = str(now.tm_year) + (str(now.tm_mon) if now.tm_mon>9 else ('0'+str(now.tm_mon))) + (str(now.tm_mday) if now.tm_mday>9 else ('0'+str(now.tm_mday))) \
                    + (str(now.tm_hour) if now.tm_hour>9 else ('0'+str(now.tm_hour))) + (str(now.tm_min) if now.tm_min>9 else ('0'+str(now.tm_min))) + '.jpg'

    # 얼굴 모자이크 하기 위한 이미지 처리
    faces, confidences = cvlib.detect_face(src, 0.2) # 0.2는 임계값
    # print(confidences)
    if len(faces) > 0:
        for (x1, y1, x2, y2) in faces: # lefttop, rightbottom
            mosaic_loc = src[y1:y2, x1:x2]
            mosaic_loc = cv2.blur(mosaic_loc,(50, 50))
            src[y1:y2, x1:x2] = mosaic_loc

    cv2.imwrite('send_image/'+ image_name, src) # 이미지 저장

    return image_name, src

def resend(queue_list, temp):
    time.sleep(30)
    for v, flag in zip(queue_list, temp):
        if flag:
            v.get()
            
def check_id(id):
    global bot
    try:
        bot.send_message(chat_id=str(int(id)), text='아이디가 있는지 확인하는 메시지입니다.')
        return True
    except:
        return False

def update_result_c5_c6():
    global incident_c1, incident_c2, incident_c3, incident_c4, incident_c5, incident_c6, code_name_dic, user_add_count
    
    for i in bot.getUpdates():
        compare_case_num = i.message.text
        if compare_case_num in incident_c2:
            change_index_num = incident_c2.index(compare_case_num)
            if incident_c5[change_index_num] == '-':
                c5_time = str(i.message.date.time())
                c5_time_hour, c5_time_min, _ = c5_time.split(':')
                str_hour = '0' + str((int(c5_time_hour)+9)%24) if len(str((int(c5_time_hour)+9)%24)) == 1 else str((int(c5_time_hour)+9)%24)
                incident_c5[change_index_num] = str_hour + '시' + c5_time_min + '분'
                incident_c6[change_index_num] = code_name_dic[str(i.message.chat.id)]
                user_add_count[str(i.message.chat.id)][0] += 1
                print(i.message.chat.id, user_add_count[str(i.message.chat.id)][0])

    f = open('result.txt', 'w', encoding='UTF-8')
    for c1, c2, c3, c4, c5, c6 in zip(incident_c1, incident_c2, incident_c3, incident_c4, incident_c5, incident_c6):
        f.write(f'{c1} {c2} {c3} {c4} {c5} {c6}\n')
    f.close()


def save():
    global occur, user_id_names, user_id_codes, user_send_cats, user_clears, user_totals, user_add_days, user_add_count
    global incident_c1, incident_c2, incident_c3, incident_c4, incident_c5, incident_c6

    total = occur['assault'] + occur['fainting'] + occur['property_damage'] + occur['stairway_fall'] + occur['turnstile_trespassing']
    f = open('occur.txt', 'r')
    dates = f.readlines()
    f.close()
    f = open('occur.txt', 'w')
    if len(dates):
        if occur['date'] in dates[-1]:
            date, o1, o2, o3, o4, o5, o6 = dates[-1].split()
            dates[-1] = '%s %s %s %s %s %s %s\n' % (date, str(int(o1)+occur['assault']), str(int(o2)+occur['fainting']), str(int(o3)+occur['property_damage']), str(int(o4)+occur['stairway_fall']), str(int(o5)+occur['turnstile_trespassing']), str(int(o6)+total))
        else:
            dates.append('%s %s %s %s %s %s %s\n' % (date, str(occur['assault']), str(occur['fainting']), str(occur['property_damage']), str(occur['stairway_fall']), str(occur['turnstile_trespassing'])), str(total))

        for v in dates:
            f.write(v)
    else:
        f.write('%s %s %s %s %s %s %s\n' % (occur['date'], str(occur['assault']), str(occur['fainting']), str(occur['property_damage']), str(occur['stairway_fall']), str(occur['turnstile_trespassing'])), str(total))
    f.close()
    
    update_result_c5_c6()

    f = open('id_list.txt', 'w', encoding='UTF-8')
    for name, cat, code, clear, total, add_day in zip(user_id_names, user_send_cats, user_id_codes, user_clears, user_totals, user_add_days):
        cat_str = ','.join(cat)
        if code in user_add_count:
            clear = str(int(clear) + user_add_count[code][0])
            total = str(int(total) + user_add_count[code][1])
        f.write(f'{name} {cat_str} {code} {clear} {total} {add_day}\n')
    f.close()

    

def send_msg(action_list, dst, queue_list, temp):
    global bot
    global cat_msg
    global user_id_list, user_id_codes, user_send_cats, user_id_names, user_clears, user_totals, user_add_days, user_add_count
    global occur
    global incident_where, incident_c1, incident_c2, incident_c3, incident_c4, incident_c5, incident_c6, code_name_dic

    
    now = time.localtime(time.time())
    incident_number_cat = ['0','0','0','0','0']
    incident_number_time = (str(now.tm_hour) if now.tm_hour>9 else ('0'+str(now.tm_hour))) + (str(now.tm_min) if now.tm_min>9 else ('0'+str(now.tm_min)))
    incident_c2_value = []

    occur_time = (str(now.tm_hour) if now.tm_hour>9 else ('0'+str(now.tm_hour))) + '시' + (str(now.tm_min) if now.tm_min>9 else ('0'+str(now.tm_min))) + '분'
    occur_day = str(now.tm_year) + '년' + (str(now.tm_mon) if now.tm_mon>9 else ('0'+str(now.tm_mon))) + '월' + (str(now.tm_mday) if now.tm_mday>9 else ('0'+str(now.tm_mday))) + '일'

    
    image_name, dst = data_processing(dst)
    cat = ''
    temp = ''
    for i, msg in enumerate(action_list):
        cat, conf = msg.split()
        occur[cat] += 1
        incident_number_cat[incident_where[cat]] = '1'
        conf = float(conf)*100 # 0.27 을 27로 만들어줌
        temp += str(i+1) + '번째, ' + str(conf) + '%로 ' + cat_msg[cat] + '\n'

    text = "상황발생번호[" + ''.join(incident_number_cat) + incident_number_time +  "]는 아래와 같은 상황이 있습니다.\n" + temp
    for user, send_cat in zip(user_id_codes, user_send_cats):
        if cat in send_cat:
            bot.send_photo(chat_id=user, photo=open('send_image/'+image_name,'rb'))
            bot.send_message(chat_id=user, text=text)
            incident_c2_value.append(code_name_dic[user])
            if user in user_add_count:
                user_add_count[user][1] += 1
            else:
                user_add_count[user] = [0, 1]
    
    incident_c1.append(occur_day)
    incident_c2.append(''.join(incident_number_cat)+incident_number_time)
    incident_c3.append(','.join(incident_c2_value))
    incident_c4.append(occur_time)
    incident_c5.append('-')
    incident_c6.append('-')

    # 나에게만 보내는 테스트라인
    # user = user_id_list[0]
    # bot.send_photo(chat_id=user, photo=open('send_image/'+image_name,'rb'))
    # bot.send_message(chat_id=user, text=text)

    resend(queue_list, temp)


if __name__ == '__main__':
    init()
    print(check_id('5184853548'))