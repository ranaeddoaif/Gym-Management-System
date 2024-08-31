# list_member
from tkinter import *
from tkinter import PhotoImage
import tkinter
import welcome
from tkinter import ttk
import tkinter as tk
import sqlite3


def display_list_mem():
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

    con = sqlite3.connect('gymproject.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM members')
    results = cur.fetchall()
    cur.execute('SELECT * FROM health_state')
    res = cur.fetchall()
    con.close()

    frame = Frame(root)
    frame.pack(padx=100, pady=100, anchor='center')

    tree = ttk.Treeview(frame)

    tree["columns"] = ("name", "id", "age", "phone_number", "email", "gender", "coins", "weight", "height", "program")

    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("name", anchor='center', width=100)
    tree.column("id", anchor='center', width=100)
    tree.column("age", anchor='center', width=100)
    tree.column("phone_number", anchor='center', width=100)
    tree.column("email", anchor='center', width=100)
    tree.column("gender", anchor='center', width=100)
    tree.column("coins", anchor='center', width=100)
    tree.column("weight", anchor='center', width=100)
    tree.column("height", anchor='center', width=100)
    tree.column("program", anchor='center', width=100)

    tree.heading("#0", text="", anchor='center')
    tree.heading("name", text="Name", anchor='center')
    tree.heading("id", text="ID", anchor='center')
    tree.heading("age", text="Age", anchor='center')
    tree.heading("phone_number", text="Mobile Number", anchor='center')
    tree.heading("email", text="Email", anchor='center')
    tree.heading("gender", text="Gender", anchor='center')
    tree.heading("coins", text="Coins", anchor='center')
    tree.heading("weight", text="Weight", anchor='center')
    tree.heading("height", text="Height", anchor='center')
    tree.heading("program", text="Program", anchor='center')

    for i in range(0, len(results)):
        tree.insert("", "end", values=(
        results[i][0], results[i][1], results[i][2], results[i][3], results[i][4], results[i][5], results[i][6],
        res[i][0], res[i][1], res[i][2]))

    lable_text = Label(root, text='List OF Members:', font=('georgia', 26, 'bold'), bg='#F86F03')
    lable_text.place(x=20, y=50)

    frame.grid(row=1, column=1)
    frame.place(x=20, y=150)

    tree.pack(pady=10, padx=10)

    root.mainloop()
