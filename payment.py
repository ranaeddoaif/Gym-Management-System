import sqlite3
from tkinter import *
from tkinter import PhotoImage
import tkinter
from tkinter import messagebox
import datetime
import welcome
from tkinter import ttk
import tkinter as tk


def display_payment():
    root = tk.Tk()
    root.title("Gym")

    def screencenter(w, h):
        screenwidth = root.winfo_screenwidth()
        screenhight = root.winfo_screenheight()

        x = int((screenwidth - w) / 2)
        y = int((screenhight - h) / 2)
        root.geometry(f'{w}x{h}+{x}+{y}')

    screencenter(1075, 600)

    image_logo = PhotoImage(file="icon/gym.png")
    root.iconphoto(False, image_logo)

    root.resizable(False, False)

    id = StringVar()
    name = StringVar()
    coins = IntVar()
    date = datetime.datetime.now().strftime("%d/%B/%Y")

    def clear():
        id.set('')
        name.set('')
        coins.set(0)


    def add():
        i = id.get()
        na = name.get()
        co = coins.get() - 1
        if i == "" or na == "" or co == "":
            messagebox.showerror('Error', "Your Entries Are Not Complete")
        else:
            con = sqlite3.connect('gymproject.db')
            conn = con.cursor()
            conn.execute(
                """UPDATE members SET coins=:coins WHERE id=:id""",
                {
                    'coins': co,
                    'id': i,
                }
            )
            con.commit()
            conn.close()
            con.close()
            if co == -1:
                messagebox.showerror('Error', "PLEASE RECHARGE!\nMember is out of coins!")
            else:
                messagebox.showinfo('done', f"Attended\nMembers Coins Are : {co}")
            clear()

    def back_fun():
        root.destroy()
        welcome.display_welcome()

    def reset():
        id.set('')
        name.set('')
        coins.set(0)

    def search():
        try:
            i = id.get()
            if i == '':
                messagebox.showerror('Error', "Please Enter ID")
            else:
                connect = sqlite3.connect('gymproject.db')
                co = connect.cursor()
                result = co.execute(f"SELECT *FROM members WHERE id ={i}").fetchall()
                co.close()
                name.set(result[0][0])
                id.set(result[0][1])
                coins.set(result[0][6])
        except:
            messagebox.showerror('error', "Member is not found")

    image_path = PhotoImage(file=r"image/welcom.png")
    bg_image = tkinter.Label(root, image=image_path)
    bg_image.place(relheight=1, relwidth=1)

    lable_text = Label(root, text='A T T E N D A N C E:', font=('georgia', 26, 'bold'), bg='#F86F03')
    lable_text.place(x=80, y=50)

    lbl_id = Label(root, text='Member ID:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_id.place(x=80, y=190)


    txt_id = Entry(root, textvariable=id, font=('calibri', 16), width='10')
    txt_id.place(x=200, y=188)

    searchbtn = Button(root, text='Search', width=10, height=1, font=('', 14, 'bold'), bg='#F86F03',command=search)
    searchbtn.place(x=320, y=184)

    lbl_name = Label(root, text='Name:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_name.place(x=80, y=260)


    txt_name = Entry(root, textvariable=name, font=('calibri', 16))
    txt_name.place(x=245, y=258)

    lbl_date = Label(root, text='Date:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_date.place(x=80, y=330)


    txt_date = Label(root, text=date, font=('calibri', 16), fg='black')
    txt_date.place(x=245, y=328)


    lbl_pay = Label(root, text='Coins:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_pay.place(x=80, y=400)


    txt_pay = Entry(root, textvariable=coins, font=('calibri', 16))
    txt_pay.place(x=245, y=398)

    addbtn = Button(root, text='Attend', width=15, height=1, font=('', 16, 'bold'), bg='#F86F03', command=add)
    addbtn.place(x=250, y=500)

    resetbtn = Button(root, text='Reset', width=8, height=1, font=('', 16, 'bold'), bg='#F86F03', command=reset)
    resetbtn.place(x=500, y=500)

    back_btn_add = Button(root, text='Back', width=8, height=1, font=('', 16, 'bold'), bd=2, bg='gray',command=back_fun)
    back_btn_add.place(x=100, y=500)


    root.mainloop()
