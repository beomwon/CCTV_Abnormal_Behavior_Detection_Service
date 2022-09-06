from tkinter import *
import menu_main

def popup(root, text):
    global temp
    temp = Toplevel()
    temp.resizable(False, False)
    temp.geometry("%dx60+%d+%d" % (len(text)*12 + 50, root.winfo_x()+root.winfo_width()/2-int((len(text)*12 + 50)/2), root.winfo_y()+root.winfo_height()/2-20))
    msg = Label(temp, text=text)
    msg.place(x=32, y=20)

def capture_screen(root):
    x1 = root.winfo_x()
    y1 = root.winfo_y()
    x2 = x1 + root.winfo_width()
    y2 = y1 + root.winfo_height()
    print(x1, y1, x2, y2)
    
    f = open('screen_xy.txt', 'w')
    f.write('%d %d %d %d' % (x1, y1, x2, y2))
    f.close()

    popup(root, '화면이 정상적으로 저장되었습니다')

def back(root):
    root.destroy()
    menu_main.main()

def test_capture():
    root = Tk()
    root.title(" ") 
    root.geometry("500x500")
    root.wm_attributes("-transparentcolor", "blue") # 파란색을 투명하게 바꾼다.

    button_frame = Frame(root)
    button_frame.pack(side='bottom')

    capture_button_image = PhotoImage(file="ui_image\save_screen_kr.png")
    capture_button = Button(button_frame, image=capture_button_image, borderwidth=0, command= lambda: capture_screen(root))
    capture_button.pack(side='left')


    back_button_image = PhotoImage(file="ui_image\Back_kr.png")
    back_button = Button(button_frame, image=back_button_image, borderwidth=0, command= lambda: back(root))
    back_button.pack(side='right')

    my_frame = Frame(root, width=10000, height=10000, bg="blue")
    my_frame.pack(pady=10, padx=10, side='top')
    
    root.mainloop()