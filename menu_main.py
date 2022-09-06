from tkinter import *
import capture
import input_info
import cctv_service


def window_setting(window):
    window.destroy()
    capture.test_capture()

def user_add(window):
    window.destroy()
    input_info.input_info()

def start_service(window):
    window.destroy()
    cctv_service.cctv_service()

def main():
    window=Tk()
    window.title(' ')
    window.resizable(False, False)

    main_frame = Frame(window, background='white')
    window_setting_button_image = PhotoImage(file="ui_image\home1.png")
    window_setting_button = Button(main_frame, image=window_setting_button_image, borderwidth=0, command= lambda: window_setting(window))
    window_setting_button.pack(side='left')

    user_add_button_image = PhotoImage(file="ui_image\home3.png")
    user_add_button = Button(main_frame, image=user_add_button_image, borderwidth=0, command= lambda: user_add(window))
    user_add_button.pack(side='right')

    start_button_image = PhotoImage(file="ui_image\home2.png")
    start_button = Button(main_frame, image=start_button_image, borderwidth=0, command= lambda: start_service(window))
    start_button.pack(side='top')
    main_frame.pack()
    
    window.mainloop()


