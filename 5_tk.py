from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('WINDOWS')
root.geometry('640x480+200+100')

frame_main = Frame(root, bd=5, bg='light blue', relief='groove')
frame_main.pack(fill='both', expand=True)

frame_left = Frame(root, bd=40, bg='white')
frame_left.pack(side=LEFT)

frame_right = Frame(root, bd=40, bg='yellow')
frame_right.pack(side=RIGHT)

frame_bottom = Frame(root, bd=40, bg='blue')
frame_bottom.pack(side=BOTTOM)

lb1 = Label(frame_main, text = 'Hello Python', bg='light blue', font=('arial', 20, 'bold'))
lb1.pack()
lb2 = Label(frame_left, text = 'LEFT')
lb2.pack()
lb3 = Label(frame_right, text = 'RIGHT')
lb3.pack()
lb4 = Label(frame_bottom, text = 'BOTTOM')
lb4.pack()



root.mainloop()

