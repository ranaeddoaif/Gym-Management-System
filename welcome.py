from tkinter import *
from PIL import Image, ImageTk
import add1
import payment
import list_member
import add2_emp
import update
import list_employee
import update_emp

def display_welcome():
    root = Tk()
    root.title("Gym")
    root.resizable(False, False)
    image2 = ImageTk.PhotoImage(Image.open("image/welcom.png"))
    w = image2.width()
    h = image2.height()

    image_logo = PhotoImage(file="icon/gym.png")
    root.iconphoto(False, image_logo)

    toolbar = Frame(root, height=57, width=0, bg='white')
    toolbar.pack()

    canvas = Canvas(root, width=w, height=h)
    canvas.create_image(0, 0, anchor=NW, image=image2)
    root.geometry('%dx%d+0+0' % (w, h))

    lab_icon = Label(root, bg='white', fg='white', width=1075)

    def centerscreen(w, h):
        screenwidth = root.winfo_screenwidth()
        screenhight = root.winfo_screenheight()
        x = int((screenwidth - w) / 2)
        y = int((screenhight - h) / 2)
        root.geometry(f'{w}x{h}+{x}+{y}')

    centerscreen(w, h)

    def add_show_mem():
        root.destroy()
        add1.add_mem_fun()

    def add_emp_show():
        root.destroy()
        add2_emp.add_emp_fun()

    def update_show():
        root.destroy()
        update.update_fun()

    def update_employee():
        root.destroy()
        update_emp.update_emp_fun()

    def logout_show():
        root.destroy()
        import logIN
        logIN.display_login()

    def payment_show():
        root.destroy()
        payment.display_payment()

    def list_mem_show():
        root.destroy()
        list_member.display_list_mem()

    def list_emp_show():
        root.destroy()
        list_employee.display_list_emp()

    add_mem_icon = ImageTk.PhotoImage(Image.open("icon/add.png"),width=30,height=30)
    btn_mem_add = Button(root, text='Add Members ', compound='left', image=add_mem_icon, relief='flat',
                         command=add_show_mem)
    btn_mem_add.place(x=130, y=0)

    add_emp_icon = ImageTk.PhotoImage(Image.open("icon/add-employee.png"),width=30,height=30)
    btn_emp_add = Button(root, text='Add Employee ', compound='left', image=add_emp_icon, relief='flat',
                         command=add_emp_show)
    btn_emp_add.place(x=0, y=0)

    update_icon = ImageTk.PhotoImage(Image.open("icon/update.png"),width=30,height=30)
    btn_update = Button(root, text='Update Members ', compound='left', image=update_icon, relief='flat',
                        command=update_show)
    btn_update.place(x=260, y=0)

    update_icon2 = ImageTk.PhotoImage(Image.open("icon/update employee.png"),width=30,height=30)
    btn_update2 = Button(root, text='Update Employee ', compound='left', image=update_icon2, relief='flat',
                        command=update_employee)
    btn_update2.place(x=410, y=0)

    list_mem_icon = ImageTk.PhotoImage(Image.open("icon/list-of-members.png"),width=30,height=30)
    btn_list = Button(root, text='List Of Members', compound='left', image=list_mem_icon, relief='flat',
                      command=list_mem_show)
    btn_list.place(x=562, y=0)

    list_emp_icon = ImageTk.PhotoImage(Image.open("icon/list-employee.png"),width=30,height=30)
    btn_list = Button(root, text='List Of Employee', compound='left', image=list_emp_icon, relief='flat',
                      command=list_emp_show)
    btn_list.place(x=710, y=0)

    pay_icon = ImageTk.PhotoImage(Image.open("icon/payment.png"),width=30,height=30)
    btn_pay = Button(root, text='Attend', compound='left', image=pay_icon, relief='flat', command=payment_show)
    btn_pay.place(x=862, y=0)

    logout_icon = ImageTk.PhotoImage(Image.open("icon/logout.png"),width=30,height=30)
    btn_logout = Button(root, text='Log Out', compound='left', image=logout_icon, relief='flat', command=logout_show)
    btn_logout.place(x=967, y=0)

    welcome_label = Label(root, text="Welcome", font=('georgia', 80, 'bold'), bg='#F86F03')
    welcome_label.place(x=250, y=250)

    canvas.pack()
    lab_icon.pack()
    root.mainloop()
