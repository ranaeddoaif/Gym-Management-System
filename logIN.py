import sqlite3
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
import welcome


def display_login():
    root = Tk()
    root.title("Gym")
    root.resizable(False, False)

    image_logo = PhotoImage(file="icon/gym.png")
    root.iconphoto(False, image_logo)

    image1 = ImageTk.PhotoImage(Image.open("image/login (1).png"))
    w = image1.width()
    h = image1.height()
    canvas = Canvas(root, width=w, height=h)
    canvas.create_image(0, 0, anchor=NW, image=image1)
    root.geometry('%dx%d+0+0' % (w, h))

    def centerscreen(w, h):
        screenwidth = root.winfo_screenwidth()
        screenhight = root.winfo_screenheight()
        x = int((screenwidth - w) / 2)
        y = int((screenhight - h) / 2)
        root.geometry(f'{w}x{h}+{x}+{y}')

    centerscreen(w, h)

    def login_but():
        flag = 0
        em = emaillog.get()
        respass = passwordlog.get()
        con = sqlite3.connect('gymproject.db')
        conn = con.cursor()
        result = conn.execute("SELECT *FROM employees").fetchall()
        for i in result:
            if em == i[4] and i[6] == respass and (i[7] == "Receptionist" or i[7] == "admin"):
                flag = 1
        conn.close()
        if flag == 1:
            root.destroy()
            welcome.display_welcome()
        elif em == "" and respass == "":
            messagebox.showerror("Invalid", "Enter Your User Name and Password")
        elif em == "":
            messagebox.showerror("Invalid", "Enter Your User Name")
        elif respass == "":
            messagebox.showerror("error", "Enter Your Password")
        else:
            messagebox.showerror("error","Not found")

    font = ("", 16, 'bold')

    Label(root, text='LOG IN', font=('georgia', 26, 'bold'), bg='#F86F03', fg='black').place(x=688, y=117)

    Label(root, text='User Name:', font=font, bg='#F86F03', fg='black').place(x=590, y=206)
    emaillog = StringVar()
    Entry(root, textvariable=emaillog, font=font, width=23).place(x=750, y=206)

    Label(root, text='Password:', font=font, bg='#F86F03', bd=0, fg='black').place(x=590, y=310)
    passwordlog = StringVar()
    Entry(root, textvariable=passwordlog, font=font, width=23, show='*').place(x=750, y=310)

    (tkinter.Button(root, text='Log in', font=font, bg='#F86F03', bd=5, fg='black', command=login_but)
     .place(x=705, y=420))
    canvas.pack()
    root.mainloop()


display_login()
