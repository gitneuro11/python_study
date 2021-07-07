from tkinter import *
root = Tk()
root.title('LabelFrame')
root.geometry('640x480+200+100')

def check():
    label.config(text=RadioVariety_1.get())

labelframe = LabelFrame(root, text='플랫폼 선택')
labelframe.pack()

RadioVariety_1=StringVar()
RadioVariety_1.set('미선택')

radio1 = Radiobutton(labelframe, text='Python', value='가능', variable=RadioVariety_1, command=check)
radio1.pack()

radio2 = Radiobutton(labelframe, text='C/C++', value='부분가능', variable=RadioVariety_1, command=check)
radio2.pack()

radio3 = Radiobutton(labelframe, text='JSON', value='불가능', variable=RadioVariety_1, command=check)
radio3.pack()

label = Label(labelframe, text='None')
label.pack()

labelframe1 = LabelFrame(root, text='플랫폼 선택')
labelframe1.pack()

RadioVariety_2=StringVar()
RadioVariety_2.set('미선택')

radio1 = Radiobutton(labelframe1, text='Python', value='가능', variable=RadioVariety_2, command=check)
radio1.pack()

radio2 = Radiobutton(labelframe1, text='C/C++', value='부분가능', variable=RadioVariety_2, command=check)
radio2.pack()

radio3 = Radiobutton(labelframe1, text='JSON', value='불가능', variable=RadioVariety_2, command=check)
radio3.pack()

label = Label(labelframe1, text='None')
label.pack()

root.mainloop()

