import sqlite3
from tkinter import *
from tkinter import PhotoImage
import tkinter
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import ttk
import welcome


def update_emp_fun():
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
    pas = StringVar()
    age = StringVar()
    salary = StringVar()
    object = ['Male', 'Female']
    object3 = ['Coach', 'Receptionist']

    def search():
        i = id.get()
        if i == '':
            messagebox.showerror('error', "Please Enter ID")
        elif i == "1":
            messagebox.showerror('error', "Can't Edit Admin")
        else:
            try:
                con = sqlite3.connect('gymproject.db')
                cur = con.cursor()
                result = cur.execute(f'SELECT * FROM employees WHERE emp_id ={i}').fetchall()
                con.close()
                id.set(result[0][1])
                name.set(result[0][0])
                mobile.set(result[0][3])
                email.set(result[0][4])
                pas.set(result[0][6])
                age.set(result[0][2])
                salary.set(result[0][8])
                combo1.set(result[0][5])
                combo3.set(result[0][7])
            except:
                messagebox.showerror('error', "Employee Not Found")

    def update():
        i = id.get()
        na = name.get()
        mo = mobile.get()
        em = email.get()
        ps = pas.get()
        ag = age.get()
        s = salary.get()
        g = combo1.get()
        pos = combo3.get()

        if i == "" or na == "" or mo == "" or em == "" or ps == "" or s == "" or ag == "" or pos == "" or g == "":
            messagebox.showerror('Error', "Your Entries Are Not Complete")

        else:
            con = sqlite3.connect('gymproject.db')
            cur = con.cursor()
            cur.execute(
                'UPDATE employees SET name=? ,age=? ,phone_number=?,username=?,gender=?,password=?,position=?,salary=?  WHERE emp_id = ?',
                (na, ag, mo, em, g, ps, pos, s, i)

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
        ps = pas.get()
        ag = age.get()
        s = salary.get()
        g = combo1.get()
        pos = combo3.get()
        if i == "" or na == "" or mo == "" or em == "" or ps == "" or s == "" or ag == "" or pos == "" or g == "":
            messagebox.showerror('Error', "Your Entries Are Not Complete")

        else:
            con = sqlite3.connect('gymproject.db')
            cur = con.cursor()
            cur.execute(f'DELETE FROM employees WHERE emp_id={i}')
            con.commit()
            con.close()

            messagebox.showinfo('done', "Delete Successful")
            clear()

    def clear():

        id.set('')
        name.set('')
        mobile.set('')
        email.set('')
        pas.set('')
        age.set('')
        salary.set('')
        combo1.set('')
        combo3.set('')

    def back_fun():
        root.destroy()
        welcome.display_welcome()

    image_path = PhotoImage(file="image/welcom.png")
    bg_image = tkinter.Label(root, image=image_path)
    bg_image.place(relheight=1, relwidth=1)

    image_logo = PhotoImage(file="icon/gym.png")
    root.iconphoto(False, image_logo)

    Label(root, text='UPDATE AND DELETE Employees:', font=('georgia', 20, 'bold'), bg='#F86F03').place(x=80,
                                                                                                       y=50)

    lbl_id = Label(root, text='Employee ID:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_id.place(x=120, y=150)


    txt_id = Entry(root, textvariable=id, font=('calibri', 16), width='10')
    txt_id.place(x=280, y=148)


    searchbtn = Button(root, text='Search', width=10, height=1, font=('', 14, 'bold'), bg='#F86F03',command=search)
    searchbtn.place(x=400, y=144)

    lbl_name = Label(root, text='Name:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_name.place(x=120, y=220)


    txt_name = Entry(root, textvariable=name, font=('calibri', 16))
    txt_name.place(x=280, y=218)


    lbl_mobile = Label(root, text='Mobile Number:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_mobile.place(x=120,y=270)


    txt_mobile = Entry(root, textvariable=mobile, font=('calibri', 16))
    txt_mobile.place(x=280, y=268)

    lbl_pas = Label(root, text='Password:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_pas.place(x=600, y=220)
    txt_pas = Entry(root, textvariable=pas, font=('calibri', 16))
    txt_pas.place(x=730, y=218)


    lbl_email = Label(root, text='E-Mail:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_email.place(x=120, y=320)
    txt_email = Entry(root, textvariable=email, font=('calibri', 16))
    txt_email.place(x=280, y=318)


    lbl_gender = Label(root, text='Gender:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_gender.place(x=120, y=370)
    combo1 = ttk.Combobox(root, values=object, state='readonly', font=('calibri', 16), width=18, height=9)
    combo1.place(x=280, y=368)


    lbl_age = Label(root, text='Age:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_age.place(x=600, y=270)
    txt_age = Entry(root, textvariable=age, font=('calibri', 16))
    txt_age.place(x=730, y=268)


    lbl_pay = Label(root, text='Salary:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black')
    lbl_pay.place(x=600, y=320)
    txt_pay = Entry(root, textvariable=salary, font=('calibri', 16))
    txt_pay.place(x=730, y=318)


    Label(root, text='Position:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=600, y=370)
    combo3 = Combobox(root, values=object3, state='readonly', font=('calibri', 16), width=18, height=9)
    combo3.place(x=730, y=368)

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
