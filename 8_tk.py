from tkinter import *
from tkinter import ttk

# root window
root = Tk()
root.geometry('640x480+200+100')
root.title('Notebook Demo')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
frame1 = Frame(notebook, width=400, height=280)
frame2 = Frame(notebook, width=400, height=280)
frame3 = Frame(notebook, width=400, height=280)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

# add frames to notebook

notebook.add(frame1, text='General Information')
notebook.add(frame2, text='Profile')
notebook.add(frame3, text='test')

lb1 = Label(frame1, text='Name:', padx=5, pady=5, anchor='e')
lb1.grid(row=0, column=0, sticky='w')
ety1 = Entry(frame1)
ety1.grid(row=0, column=1)

lb2 = Label(frame1, text='Address:', padx=5, pady=5)
lb2.grid(row=1, column=0, sticky='w')
ety2 = Entry(frame1)
ety2.grid(row=1, column=1)

lb3 = Label(frame1, text='Phone:', padx=5, pady=5)
lb3.grid(row=2, column=0, sticky='w')

phone_ety_frame = Frame(frame1)
phone_ety_frame.grid(row=2, column=1, sticky='w')


ety3 = Entry(phone_ety_frame, width=3)
ety3.grid(row=0, column=0)
ety3_1 = Entry(phone_ety_frame, width=4)
ety3_1.grid(row=0, column=2)
ety3_2 = Entry(phone_ety_frame, width=4)
ety3_2.grid(row=0, column=4)
lb5 = Label(phone_ety_frame, text='/')
lb5.grid(row=0, column=1)
lb6 = Label(phone_ety_frame, text='/')
lb6.grid(row=0, column=3)

sp1=ttk.Separator(frame1, orient='horizontal')
sp1.grid(row=3, columnspan=2, sticky='ew', pady=10)

lf1 = LabelFrame(frame1, text='test', padx=10, pady=10)
lf1.grid(row=4, columnspan=2, sticky='w', ipadx=5)

lb4 = Label(lf1, text='Hello Python')
lb4.grid(row=0, column=0)



root.mainloop()
