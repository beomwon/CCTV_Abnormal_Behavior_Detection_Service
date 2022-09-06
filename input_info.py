from tkinter import *
from math import *
import menu_main
import using_telegram
import tkinter.font
import time

global user_id_list, user_id_names, user_id_codes, user_send_cats, id_send_cat, user_clears, user_totals, user_add_days

def check_cat(cat, check):
    global id_send_cat
    if check == 1: id_send_cat.append(cat)
    elif check == 0: id_send_cat.remove(cat)
    
def popup(text):
    global window, temp  #720, 488
    temp = Toplevel()
    temp.resizable(False, False)
    temp.geometry("%dx60+%d+%d" % (len(text)*12 + 50, window.winfo_x()+360-int((len(text)*12 + 50)/2), window.winfo_y()+244-20))
    msg = Label(temp, text=text)
    msg.place(x=32, y=20)
    
def get_info(listbox, id_name, id_code, id_send_cat):
    global user_id_names, user_id_codes, user_send_cats, user_clears, user_totals, user_add_days
    if using_telegram.check_id(id_code.get()):
        if ' ' not in id_name.get():
            user_id_names.append(id_name.get())
            user_id_codes.append(id_code.get())

            if len(id_send_cat):
                user_send_cats.append(id_send_cat)
                user_clears.append('0')
                user_totals.append('0')

                now = time.localtime(time.time())
                add_day = str(now.tm_year) + '년' + (str(now.tm_mon) if now.tm_mon>9 else ('0'+str(now.tm_mon))) + '월'+ (str(now.tm_mday) if now.tm_mday>9 else ('0'+str(now.tm_mday))) + '일'
                user_add_days.append(add_day)

                listbox.insert(len(user_id_names), user_id_names[-1])
                id_name.delete(0,len(id_name.get()))
                id_code.delete(0,len(id_code.get()))
            else:
                popup('카테고리를 한개이상 선택해주세요')
        else:
            popup('이름에 띄어쓰기를 빼주세요')
    else:
        popup('아이디가 존재하지 않습니다')
        

def del_info(listbox):
    global user_id_names, user_id_codes, user_send_cats

    del user_id_names[int(listbox.curselection()[0])]
    del user_id_codes[int(listbox.curselection()[0])]
    del user_send_cats[int(listbox.curselection()[0])]

    listbox.delete(listbox.index(listbox.curselection()[0]),listbox.index(listbox.curselection()[0])+1)

def save():
    global user_id_names, user_id_codes, user_send_cats, user_clears, user_totals, user_add_days
    
    f = open('id_list.txt', 'w', encoding='UTF-8')

    for name, cat, code, clear, total, add_day in zip(user_id_names, user_send_cats, user_id_codes, user_clears, user_totals, user_add_days):
        cat_str = ','.join(cat)
        f.write(f'{name} {cat_str} {code} {clear} {total} {add_day}\n')
    f.close()
    
    using_telegram.update_id_list()

def back(window, listbox):
    listbox.delete(0, listbox.size())
    window.destroy()
    menu_main.main()

def input_info():
    global user_id_list, user_id_names, user_id_codes, user_send_cats, id_send_cat, user_clears, user_totals, user_add_days, window

    ### init ###
    user_id_list, user_id_names, user_id_codes, user_send_cats, user_clears, user_totals, user_add_days = [], [], [], [], [], [], []

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

    window = Tk()
    window.title(' ')
    window.geometry("720x488")
    window.configure(bg="#ffffff")
    window.resizable(False, False)
    
    canvas = Canvas(window, bg="#ffffff", height=488, width=720, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)

    ### user list ###
    frame = Frame(window, borderwidth=0)
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    
    listbox_font = tkinter.font.Font(family="맑은 고딕", size=10)
    listbox = Listbox(frame, borderwidth=0, yscrollcommand=scrollbar.set, width=38, height=15, highlightthickness=0, font=listbox_font)
    for i, v in enumerate(user_id_names): listbox.insert(i, v)
    listbox.pack()
    scrollbar["command"]=listbox.yview
    frame.place(x=400,y=119)

    background_img = PhotoImage(file = f"ui_image\input_info_bg.png")
    canvas.create_image(360.0, 244.0, image=background_img)

    id_name_label = PhotoImage(file = f"ui_image\TextBox.png")
    canvas.create_image(186.0, 129.0, image=id_name_label)

    id_name = Entry(bd=0, bg="#fcfdfe", highlightthickness=0)
    id_name.place(x=50.0, y=109, width=246.0, height=40)
    id_name.insert(0,'이름을 입력해주세요.')
 
    id_code_label = PhotoImage(file = f"ui_image\TextBox.png")
    canvas.create_image(186.0, 218.0, image=id_code_label)


    id_code = Entry(bd=0, bg="#fcfdfe", highlightthickness=0)
    id_code.place(x=50.0, y=198, width=246.0, height=40)
    id_code.insert(0,'아이디를 입력해주세요.')



    ### check box ###
    id_send_cat = []
    assault_boolean = tkinter.IntVar()
    fainting_boolean = tkinter.IntVar()
    property_boolean = tkinter.IntVar()
    stairway_boolean = tkinter.IntVar()
    turnstile_boolean = tkinter.IntVar()

    assault_check_before_image = PhotoImage(file="ui_image\Assult_off.png")
    assault_check_after_image = PhotoImage(file="ui_image\Assult_on.png")
    assault_check_box = tkinter.Checkbutton(window, variable=assault_boolean, image=assault_check_before_image, 
                                            selectimage=assault_check_after_image, command=lambda: check_cat('assault', assault_boolean.get()), 
                                            bg = "#ffffff", activebackground = "#ffffff")
    assault_check_box.place(x=18, y=294)


    fainting_check_before_image = PhotoImage(file="ui_image\Fainting_off.png")
    fainting_check_after_image = PhotoImage(file="ui_image\Fainting_on.png")
    fainting_check_box = tkinter.Checkbutton(window, variable=fainting_boolean, image=fainting_check_before_image,
                                             selectimage=fainting_check_after_image, command=lambda: check_cat('fainting', fainting_boolean.get()), 
                                             bg = "#ffffff",  activebackground = "#ffffff")
    fainting_check_box.place(x=186, y=294)


    property_damage_check_before_image = PhotoImage(file="ui_image\property_off.png")
    property_damage_check_after_image = PhotoImage(file="ui_image\property_on.png")
    property_damage_check_box = tkinter.Checkbutton(window, variable=property_boolean, image=property_damage_check_before_image, 
                                                    selectimage=property_damage_check_after_image, command=lambda: check_cat('property_damage', property_boolean.get()), 
                                                    bg = "#ffffff",  activebackground = "#ffffff")
    property_damage_check_box.place(x=18, y=327)


    stairway_fall_damage_check_before_image = PhotoImage(file="ui_image\Fall_off.png")
    stairway_fall_damage_check_after_image = PhotoImage(file="ui_image\Fall_on.png")
    stairway_fall_check_box = tkinter.Checkbutton(window, variable=stairway_boolean, image=stairway_fall_damage_check_before_image, 
                                                  selectimage=stairway_fall_damage_check_after_image, command=lambda: check_cat('stairway_fall', stairway_boolean.get()), 
                                                  bg = "#ffffff",  activebackground = "#ffffff")
    stairway_fall_check_box.place(x=186, y=327)


    turnstile_trespassing_check_before_image = PhotoImage(file="ui_image\Turnstile_off.png")
    turnstile_trespassing_check_after_image = PhotoImage(file="ui_image\Turnstile_on.png")
    turnstile_trespassing_check_box = tkinter.Checkbutton(window, variable=turnstile_boolean, image=turnstile_trespassing_check_before_image, 
                                                          selectimage=turnstile_trespassing_check_after_image, command=lambda: check_cat('turnstile_trespassing', turnstile_boolean.get()), 
                                                          bg = "#ffffff",  activebackground = "#ffffff")
    turnstile_trespassing_check_box.place(x=18, y=360)


    ## hide check box##
    trick1_img = PhotoImage(file='ui_image\Trick.png')
    trick1= Label(image=trick1_img)
    trick1.place(x = 4, y = 300,width = 43,height = 91)

    trick2_img = PhotoImage(file='ui_image\Trick.png')
    trick2= Label(image=trick2_img)
    trick2.place(x = 164, y = 300,width = 43,height = 56)

    ### button ###
    back_button_image = PhotoImage(file=f"ui_image\Back_mini_kr.png")
    back_button = Button(image=back_button_image, borderwidth=0, highlightthickness=0, command=lambda: back(window, listbox), relief="flat")
    back_button.place(x = 628, y = 25,width = 59,height = 30)

    add_button_image = PhotoImage(file = f"ui_image\Add_button.png")
    add_button = Button(image=add_button_image, borderwidth=0, highlightthickness=0, command=lambda: get_info(listbox, id_name, id_code, id_send_cat))
    add_button.place(x = 95, y = 425,width = 181,height = 51)

    delete_button_image = PhotoImage(file = f"ui_image\del_kr.png")
    delete_button = Button(image=delete_button_image, borderwidth=0, highlightthickness=0, command=lambda: del_info(listbox))
    delete_button.place( x = 447, y = 422,width = 181,height = 52)

    save_button_image = PhotoImage(file = f"ui_image\save_mini_kr.png")
    save_button = Button(image = save_button_image, borderwidth = 0, highlightthickness = 0, command =lambda: save(), relief = "flat")
    save_button.place( x = 558, y = 25,width = 59,height = 30)

    window.mainloop()

if __name__ == '__main__':
    input_info()