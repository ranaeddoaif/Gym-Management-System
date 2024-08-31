# list_employee
import sqlite3
from tkinter import *
from tkinter import PhotoImage
import tkinter
import welcome
from tkinter import ttk
import tkinter as tk


def display_list_emp():
    root = tk.Tk()
    root.title("Gym")

    image_path = PhotoImage(file='image/welcom.png')
    bg_image = tkinter.Label(root, image=image_path)
    bg_image.place(relheight=1, relwidth=1)

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

    def back_fun():
        root.destroy()
        welcome.display_welcome()

    back_btn_add = Button(root, text='Back', width=8, height=1, font=('', 16, 'bold'), bd=2, bg='gray',
                          command=back_fun)
    back_btn_add.place(x=100, y=500)

    frame = Frame(root)
    frame.pack(padx=2000, pady=200, anchor='center')
    tree = ttk.Treeview(frame)

    con = sqlite3.connect('gymproject.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM employees')
    resultes = cur.fetchall()

    tree["columns"] = ('name', 'emp_id','age', 'phone_number', 'username', 'gender', 'password','position', "salary")

    tree.column("#0", width=0, stretch=tk.NO)
    tree.column('name', anchor='center', width=100)
    tree.column('emp_id', anchor='center', width=100)
    tree.column('age', anchor='center', width=100)
    tree.column('phone_number', anchor='center', width=100)
    tree.column('username', anchor='center', width=100)
    tree.column('gender', anchor='center', width=100)
    tree.column('password', anchor='center', width=100)
    tree.column('position', anchor='center', width=100)
    tree.column("salary", anchor='center', width=100)

    tree.heading("#0", text="", anchor='center')
    tree.heading("name", text="Name", anchor='center')
    tree.heading("emp_id", text="ID", anchor='center')
    tree.heading("age", text="Age", anchor='center')
    tree.heading("phone_number", text="Mobile Number", anchor='center')
    tree.heading("username", text="Email", anchor='center')
    tree.heading("gender", text="Gender", anchor='center')
    tree.heading("password", text="Password", anchor='center')
    tree.heading("position", text="Position", anchor='center')
    tree.heading("salary", text="Salary", anchor='center')

    lable_text = Label(root, text='List OF Employee:', font=('georgia', 26, 'bold'), bg='#F86F03')
    lable_text.place(x=70, y=50)

    # def add_table():
    for i in resultes:
        tree.insert("", "end", values= (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))

    frame.grid(row=1, column=1)
    frame.place(x=70, y=150)

    tree.pack(pady=10, padx=10)

    root.mainloop()