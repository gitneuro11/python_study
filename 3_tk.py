from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('WINDOWS')
root.geometry('640x480+200+100')

def AddData():
	messagebox.showinfo('Basic Example', 'a Basic Tk MessageBox')

#   messagebox.showwarning("Warning Example", "Warning MessageBox")

#	messagebox.showerror("Error Example", "Error MessageBox")

#	messagebox.askquestion("Ask Question Example", "Quit?")

#	messagebox.askyesno("Ask Yes/No Example", "Quit?")

#	messagebox.askokcancel("Ask OK Cancel Example", "Quit?")

#	messagebox.askretrycancel("Ask Retry Cancel Example", "Quit?")

btnAddData = Button(root, text = 'ADD', command=AddData)
btnAddData.grid(row=0, column=0)

root.mainloop()
