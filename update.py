import sqlite3
from tkinter import *
from tkinter import PhotoImage
import tkinter
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import ttk
import welcome


def update_fun():
    root = Tk()
    root.title("Gym")

    def screencenter(w, h):
        screenwidth = root.winfo_screenwidth()
        screenhight = root.winfo_screenheight()

        x = int((screenwidth - w) / 2)
        y = int((screenhight - h) / 2)
        root.geometry(f'{w}x{h}+{x}+{y}')

    screencenter(1075, 600)

    root.resizable(False, False)
    id = StringVar()
    name = StringVar()
    mobile = StringVar()
    email = StringVar()
    gender = StringVar()
    weight = StringVar()
    height = StringVar()
    program = StringVar()
    age = StringVar()
    coins = StringVar()
    object = ['Male', 'Female']
    object2 = ['Gaining muscles', 'Losing weight']
    object3 = []
    con = sqlite3.connect('gymproject.db')
    conn = con.cursor()
    result = conn.execute("SELECT *FROM employees WHERE position='Coach'").fetchall()
    conn.close()
    for jj in result:
        object3.append(jj[0])

    def search():
        i = id.get()
        if i == '':
            messagebox.showerror('error', "Please Enter ID")
        else:
            try:
                con = sqlite3.connect('gymproject.db')
                conn = con.cursor()
                result = conn.execute(f"SELECT *FROM members WHERE id ={i}").fetchall()
                res = conn.execute(f"SELECT *FROM health_state WHERE member_id ={i}").fetchall()
                rop = conn.execute(f"SELECT *FROM employees WHERE emp_id ={result[0][7]}").fetchall()
                conn.close()
                id.set(result[0][1])
                name.set(result[0][0])
                mobile.set(result[0][3])
                email.set(result[0][4])
                combo1.set(result[0][5])
                weight.set(res[0][0])
                height.set(res[0][1])
                combo2.set(res[0][2])
                age.set(result[0][2])
                coins.set(result[0][6])
                combo3.set(rop[0][0])
            except:
                messagebox.showerror('error', "Member Not Found")

    def update():
        global cohid
        i = id.get()
        na = name.get()
        mo = mobile.get()
        em = email.get()
        we = weight.get()
        he = height.get()
        ag = age.get()
        p = coins.get()
        pr = combo2.get()
        g = combo1.get()
        coh = combo3.get()
        con = sqlite3.connect('gymproject.db')
        conn = con.cursor()
        result = conn.execute("SELECT *FROM employees WHERE position='Coach'").fetchall()
        conn.close()
        for h in result:
            if coh == h[0]:
                cohid = h[1]
                break
        if i == "" or na == "" or mo == "" or em == "" or we == "" or he == "" or ag == "" or p == "" or pr == "" or g == "" or cohid == "":
            messagebox.showerror('Error', "Your Entries Are Not Complete")

        else:
            con = sqlite3.connect('gymproject.db')
            conn = con.cursor()
            co = con.cursor()
            conn.execute(
                """UPDATE members SET 
                name= :name,age=:age,phone_number=:phone_number,email=:email,gender=:gender,coins=:coins,
                coach_id=:coach_id 
                WHERE id=:id""",
                {
                    'name': na,
                    'age': ag,
                    'phone_number': mo,
                    'email': em,
                    'gender': g,
                    'coins': p,
                    'coach_id': cohid,
                    'id': i,
                }
            )
            co.execute(
                """UPDATE health_state 
                SET weight= :w,height=:h,program=:p 
                WHERE member_id=:m"""
                , {
                    'w': we,
                    'h': he,
                    'p': pr,
                    'm': i,
                }
            )
            con.commit()
            con.close()

            messagebox.showinfo('done', "Update Successful ")
            clear()

    def delete():
        i = id.get()
        na = name.get()
        mo = mobile.get()
        em = email.get()
        we = weight.get()
        he = height.get()
        ag = age.get()
        p = coins.get()
        if i == "" or na == "" or mo == "" or em == "" or we == "" or he == "" or ag == "" or p == "":
            messagebox.showerror('Error', "Your Entries Are Not Complete")

        else:
            con = sqlite3.connect('gymproject.db')
            coco = con.cursor()
            coco.execute('DELETE FROM health_state WHERE member_id=:i', {'i': i})
            coco.execute('DELETE FROM members WHERE id=:i', {'i': i})
            con.commit()
            con.close()

            messagebox.showinfo('done', "Delete Successful")
            clear()

    def clear():

        id.set('')
        name.set('')
        mobile.set('')
        email.set('')
        gender.set('')
        weight.set('')
        height.set('')
        program.set('')
        age.set('')
        coins.set('')
        combo1.set('')
        combo2.set('')
        combo3.set('')

    def back_fun():
        root.destroy()
        welcome.display_welcome()

    image_path = PhotoImage(file="image/welcom.png")
    bg_image = tkinter.Label(root, image=image_path)
    bg_image.place(relheight=1, relwidth=1)

    image_logo = PhotoImage(file="icon/gym.png")
    root.iconphoto(False, image_logo)

    Label(root, text='UPDATE AND DELETE MEMBERS:', font=('georgia', 20, 'bold'), bg='#F86F03').place(x=80,
                                                                                                     y=50)

    lable_text = Label(root, text='UPDATE AND DELETE MEMBERS:', font=('georgia', 20, 'bold'), bg='#F86F03')
    lable_text.place(x=80, y=50)

    lbl_id = Label(root, text='Member ID:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_id.place(x=120, y=150)

    txt_id = Entry(root, textvariable=id, font=('calibri', 16), width=10)
    txt_id.place(x=240, y=148)

    searchbtn = Button(root, text='Search', width=10, height=1, font=('', 14, 'bold'), bg='#F86F03', command=search)
    searchbtn.place(x=360, y=144)

    lbl_name = Label(root, text='Name:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_name.place(x=120, y=220)

    txt_name = Entry(root, textvariable=name, font=('calibri', 16))
    txt_name.place(x=280, y=218)

    lbl_mobile = Label(root, text='MobileNumber:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_mobile.place(x=120, y=270)

    txt_mobile = Entry(root, textvariable=mobile, font=('calibri', 16))
    txt_mobile.place(x=280, y=268)

    lbl_email = Label(root, text='E-Mail:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_email.place(x=120, y=320)

    txt_email = Entry(root, textvariable=email, font=('calibri', 16))
    txt_email.place(x=280, y=318)

    lbl_gender = Label(root, text='Gender:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_gender.place(x=120, y=370)

    combo1 = ttk.Combobox(root, values=object, state='readonly', font=('calibri', 16), width=18, height=9)
    combo1.place(x=280, y=368)

    lbl_weight = Label(root, text='Weight:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_weight.place(x=120, y=420)

    txt_weight = Entry(root, textvariable=weight, font=('calibri', 16))
    txt_weight.place(x=280, y=418)

    lbl_height = Label(root, text='Height:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_height.place(x=600, y=220)

    txt_height = Entry(root, textvariable=height, font=('calibri', 16))
    txt_height.place(x=750, y=218)

    lbl_time = Label(root, text='Program:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_time.place(x=600, y=270)

    combo2 = ttk.Combobox(root, values=object2, state='readonly', font=('calibri', 16), width=18, height=9)
    combo2.place(x=750, y=268)

    lbl_age = Label(root, text='Age:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_age.place(x=600, y=320)

    txt_age = Entry(root, textvariable=age, font=('calibri', 16))
    txt_age.place(x=750, y=318)

    lbl_pay = Label(root, text='Coins:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_pay.place(x=600, y=370)

    txt_pay = Entry(root, textvariable=coins, font=('calibri', 16))
    txt_pay.place(x=750, y=368)

    Label(root, text='Coach Name:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=600, y=420)

    combo3 = Combobox(root, values=object3, state='readonly', font=('calibri', 16), width=18, height=9)
    combo3.place(x=750, y=418)

    updatebtn = Button(root, text='Update', width=8, height=1, font=('', 16, 'bold'), bd=2, bg='#F86F03',
                       command=update)
    updatebtn.place(x=600, y=500)

    deletebtn = Button(root, text='Delete', width=8, height=1, font=('', 16, 'bold'), bd=2, bg='#F86F03',
                       command=delete)
    deletebtn.place(x=750, y=500)

    resetbtn = Button(root, text='Reset', width=8, height=1, font=('', 16, 'bold'), bd=2, bg='#F86F03', command=clear)
    resetbtn.place(x=900, y=500)

    back_btn_up = Button(root, text='Back', width=8, height=1, font=('', 16, 'bold'), bd=2, bg='gray', command=back_fun)
    back_btn_up.place(x=100, y=500)
    root.mainloop()

