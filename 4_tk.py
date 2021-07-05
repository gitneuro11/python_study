from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('WINDOWS')
root.geometry('640x480+200+100')

def ExitApp():
    MsgBox = messagebox.askquestion('Exit App', 'Really Quit?', icon = 'error')
    if MsgBox == 'yes':
        root.destroy()
    else:
        messagebox.showinfo('Welcome Back', 'Welcome back to the App')

btnAddData = Button(root, text = 'Exit App', command=ExitApp)
btnAddData.grid(row=0, column=0)

root.mainloop()
