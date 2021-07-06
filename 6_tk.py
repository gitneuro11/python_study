from tkinter import *
root = Tk()

root.title('WINDOWS')
root.geometry('640x480+200+100')

# Databases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()


# Create table

c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")
f_name = Entry(root, width=30)
f_name.grid(row=0, column=0)

l_name = Entry(root, width=30)
l_name.grid(row=0, column=0)

address = Entry(root, width=30)
address.grid(row=0, column=0)

f_name = Entry(root, width=30)
f_name.grid(row=0, column=0)

f_name = Entry(root, width=30)
f_name.grid(row=0, column=0)

f_name = Entry(root, width=30)
f_name.grid(row=0, column=0)
f_name = Entry(root, width=30)
f_name.grid(row=0, column=0)
root.mainloop()




