# add2
import sqlite3
from tkinter import *
from tkinter import PhotoImage
import tkinter
from tkinter import messagebox
from tkinter.ttk import Combobox
import welcome

con = sqlite3.connect('gymproject.db')
conn = con.cursor()
result = conn.execute("SELECT *FROM employees").fetchall()
conn.close()
for i in result:
    k = i[1]


def add_emp_fun():
    root = Tk()
    root.title("Gym")
    name = StringVar()
    mobile = StringVar()
    email = StringVar()
    password = StringVar()
    salary = StringVar()
    age = StringVar()
    object_pos = ['Coach', 'Receptionist']
    object_gen = ['Male', 'Female']

    def insert_data():

        global k
        na = name.get()
        mo = mobile.get()
        em = email.get()
        g = combo1.get()
        ps = password.get()
        sal = salary.get()
        ag = age.get()
        p = combo2.get()
        if na == "" or mo == "" or em == "" or ps == "" or sal == "" or ag == "":
            messagebox.showwarning('Error', "Your Entries Are Not Complete")
        elif not mo.isdigit():
            messagebox.showwarning('Error', "Please enter a number")
        elif len(mo) != 11:
            messagebox.showwarning('Error', "Please enter a 11 number")
        # elif len(ps) < 8 or len(ps) > 20:
        #     messagebox.showwarning('Error', "Please enter Password in Range[8,20]")
        else:
            connect = sqlite3.connect('gymproject.db')
            cur = connect.cursor()
            cur.execute(
                'INSERT Into employees (name,age,phone_number,username,gender,"password",position,salary) VALUES (?,?,?,?,?,?,?,?)',
                (na, ag, mo, em, g, ps, p, sal))
            connect.commit()
            connect.close()
            u = k + 2

            id = Label(root, text=u, font=('calibri', 16))
            id.place(x=280, y=148)
            messagebox.showinfo('done', "Add Sucssful")
            clear()
            k = u - 1

    def clear():
        name.set('')
        mobile.set('')
        email.set('')
        password.set('')
        salary.set('')
        age.set('')
        combo2.set('')
        combo1.set('')

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

    Label(root, text='ADD NEW EMPLOYEE:', font=('georgia', 26, 'bold'), bg='#F86F03').place(x=100, y=50)
    Label(root, text='Employee ID:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=120, y=150)
    txt_id = Label(root, text=k + 1, font=('calibri', 16))
    txt_id.place(x=280, y=148)

    Label(root, text='Name:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=120, y=200)
    Entry(root, textvariable=name, font=('calibri', 16)).place(x=280, y=198)

    Label(root, text='MobileNumber:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=120,
                                                                                                   y=250)
    Entry(root, textvariable=mobile, font=('calibri', 16)).place(x=280, y=248)

    Label(root, text='E-Mail:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=120, y=300)
    Entry(root, textvariable=email, font=('calibri', 16)).place(x=280, y=298)

    Label(root, text='Password:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=120, y=350)
    Entry(root, textvariable=password, font=('calibri', 16)).place(x=280, y=348)

    Label(root, text='Gender:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=120, y=400)
    combo1 = Combobox(root, values=object_gen, state='readonly', font=('calibri', 16), width=18, height=9)
    combo1.place(x=280, y=398)

    Label(root, text='Salary:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=600, y=200)
    Entry(root, textvariable=salary, font=('calibri', 16)).place(x=730, y=198)

    Label(root, text='Position:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=600, y=250)
    combo2 = Combobox(root, values=object_pos, state='readonly', font=('calibri', 16), width=18, height=9)
    combo2.place(x=730, y=248)

    Label(root, text='Age:', font=("", 16, 'bold'), bg='#F86F03', bd=0, fg='black').place(x=600, y=300)
    Entry(root, textvariable=age, font=('calibri', 16)).place(x=730, y=298)

    savebtn = Button(root, text='Save', width=10, height=1, font=('', 18, 'bold'), bg='#F86F03', command=insert_data)
    savebtn.place(x=600, y=400)

    resetbtn = Button(root, text='Reset', width=10, height=1, font=('', 18, 'bold'), bg='#F86F03', command=clear)
    resetbtn.place(x=800, y=400)

    back_btn_add = Button(root, text='Back', width=8, height=1, font=('', 16, 'bold'), bd=2, bg='gray',
                          command=back_fun)
    back_btn_add.place(x=100, y=500)

    root.mainloop()
