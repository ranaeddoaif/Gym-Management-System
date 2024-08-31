import sqlite3
from tkinter import *
from tkinter import PhotoImage
import tkinter
from tkinter import messagebox
from tkinter.ttk import Combobox
import welcome

k = 1
con = sqlite3.connect('gymproject.db')
conn = con.cursor()
result = conn.execute("SELECT *FROM members").fetchall()
conn.close()
for i in result:
    k = i[1] + 1


def add_mem_fun():
    root = Tk()
    root.title("Gym")
    name = StringVar()
    mobile = StringVar()
    email = StringVar()
    weight = StringVar()
    height = StringVar()
    age = StringVar()
    pay = StringVar()
    object = ['Male', 'Female']
    object3 = []
    object2 = ['Gaining muscles', 'Losing weight']

    con = sqlite3.connect('gymproject.db')
    conn = con.cursor()
    result = conn.execute("SELECT *FROM employees WHERE position='Coach'").fetchall()
    conn.close()
    for i in result:
        object3.append(i[0])

    def insert_data():
        global k, cohid
        na = name.get()
        mo = mobile.get()
        em = email.get()
        g = combo1.get()
        we = weight.get()
        he = height.get()
        ag = age.get()
        p = pay.get()
        pr = combo2.get()
        coh = combo3.get()
        con = sqlite3.connect('gymproject.db')
        conn = con.cursor()
        result = conn.execute("SELECT *FROM employees WHERE position='Coach'").fetchall()
        conn.close()
        for i in result:
            if coh == i[0]:
                cohid = i[1]
                break

        if na == "" or mo == "" or em == "" or we == "" or he == "" or ag == "" or p == "":
            messagebox.showwarning('Error', "Your Entries Are Not Complete")
        elif not mo.isdigit():
            messagebox.showwarning('Error', "Please enter a number")
        elif len(mo) != 11:
            messagebox.showwarning('Error', "Please enter a 11 number")
        else:
            co = sqlite3.connect('gymproject.db')
            rrrrr = co.cursor()
            cu = co.cursor()
            cu.execute(
                'INSERT Into health_state (weight,height,program,member_id) VALUES (?,?,?,?)',
                (we, he, pr, k))

            rrrrr.execute(
                'INSERT INTO members (name,age,phone_number,email,gender,coins,coach_id) VALUES (?,?,?,?,?,?,?)',
                (na, ag, mo, em, g, p, cohid))
            co.commit()
            co.close()
            k = k + 1
            Id = Label(root, text=k, font=('calibri', 16))
            Id.place(x=280, y=148)
            messagebox.showinfo('done', "Add Sucssful")
            clear()

    def clear():
        name.set('')
        mobile.set('')
        email.set('')
        weight.set('')
        height.set('')
        age.set('')
        pay.set('')
        combo2.set('')
        combo1.set('')
        combo3.set('')

    def back_fun():
        root.destroy()
        welcome.display_welcome()

    def screencenter(w, h):
        screenwidth = root.winfo_screenwidth()
        screenhight = root.winfo_screenheight()
        x = int((screenwidth - w) / 2)
        y = int((screenhight - h) / 2)
        root.geometry(f'{w}x{h}+{x}+{y}')

    screencenter(1075, 600)
    root.resizable(False, False)

    image_path = PhotoImage(file="image/welcom.png")
    bg_image = tkinter.Label(root, image=image_path)
    bg_image.place(relheight=1, relwidth=1)

    image_logo = PhotoImage(file="icon/gym.png")
    root.iconphoto(False, image_logo)

    Label(root, text='ADD NEW MEMBERS:', font=('georgia', 26, 'bold'), bg='#F86F03').place(x=100, y=50)
    Label(root, text='Member ID:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=120, y=150)
    id = Label(root, text=k, font=('calibri', 16))
    id.place(x=280, y=148)

    Label(root, text='Name:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=120, y=200)
    Entry(root, textvariable=name, font=('calibri', 16)).place(x=280, y=198)

    Label(root, text='MobileNumber:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=120,
                                                                                                   y=250)
    Entry(root, textvariable=mobile, font=('calibri', 16)).place(x=280, y=248)

    Label(root, text='E-Mail:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=120, y=300)
    Entry(root, textvariable=email, font=('calibri', 16)).place(x=280, y=298)

    Label(root, text='Gender:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=120, y=350)
    combo1 = Combobox(root, values=object, state='readonly', font=('calibri', 16), width=18, height=9)
    combo1.place(x=280, y=348)

    Label(root, text='Weight:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=600, y=200)
    Entry(root, textvariable=weight, font=('calibri', 16)).place(x=750, y=198)

    Label(root, text='Height:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=600, y=250)
    Entry(root, textvariable=height, font=('calibri', 16)).place(x=750, y=248)

    Label(root, text='Program:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=600, y=300)
    combo2 = Combobox(root, values=object2, state='readonly', font=('calibri', 16), width=18, height=9)
    combo2.place(x=750, y=298)

    Label(root, text='Age:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=120, y=400)
    Entry(root, textvariable=age, font=('calibri', 16)).place(x=280, y=398)

    Label(root, text='Coins:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=600, y=350)
    Entry(root, textvariable=pay, font=('calibri', 16)).place(x=750, y=348)

    Label(root, text='Coach Name:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=600, y=400)
    combo3 = Combobox(root, values=object3, state='readonly', font=('calibri', 16), width=18, height=9)
    combo3.place(x=750, y=398)

    savebtn = Button(root, text='Save', width=10, height=1, font=('', 18, 'bold'), bg='#F86F03', command=insert_data)
    savebtn.place(x=600, y=480)

    resetbtn = Button(root, text='Reset', width=10, height=1, font=('', 18, 'bold'), bg='#F86F03', command=clear)
    resetbtn.place(x=800, y=480)

    back_btn_add = Button(root, text='Back', width=8, height=1, font=('', 16, 'bold'), bd=2, bg='gray',
                          command=back_fun)
    back_btn_add.place(x=100, y=480)

    root.mainloop()
