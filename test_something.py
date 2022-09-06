import threading
import time
import start

def test(i):
    global temp
    time.sleep(i)
    temp[i] = False

def main():
    global temp
    temp = [True, True, True, True]
    t = [threading.Thread(target = test, args=(1)), threading.Thread(target = test, args=(2)), threading.Thread(target = test, args=(3)), threading.Thread(target = test, args=(4))]
    for i in range(4):
        t[i].start
    while True:
        print(temp)
        if True not in temp:
            break 

if __name__ == '__main__':
    main()