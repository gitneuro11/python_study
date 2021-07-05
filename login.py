from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("WINDOWS")
root.geometry("300x150+200+100")

user_id = StringVar()
password = StringVar()

def check_data():
    if user_id.get() == "python" and password.get() == "python":
        messagebox.showinfo("알림","정상적으로 로그인 되었습니다.")
    else:
        messagebox.showwarning("경고","아이디와 패스워드가 맞지 않습니다. ")

lb1 = Label(root, text = "Username : ")
lb1.grid(row = 0, column = 0, padx = 10, pady = 10)
lb2 = Label(root, text = "Password : ")
lb2.grid(row = 1, column = 0, padx = 10, pady = 10)

ety1 = Entry(root, bg='yellow', textvariable = user_id)
ety1.grid(row = 0, column =1, padx =10, pady =10)
ety2 = Entry(root, show = '*', textvariable = password)
ety2.grid(row = 1, column =1, padx =10, pady =10)

btn1 = Button(root, text = "Login", command = check_data)
btn1.grid(row = 2, column = 1, padx = 10, pady = 10)

root.mainloop()


