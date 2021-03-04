from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])

def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), genre_text.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), genre_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), genre_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), genre_text.get())

window = Tk()

window.wm_title("Library Management")
window.resizable(0,0)

l1=Label(window, text="Title")
l1.grid(row=0, column=0)

l2=Label(window, text="Author")
l2.grid(row=0, column=2)

l3=Label(window, text="Year")
l3.grid(row=1, column=0)

l4=Label(window, text="Genre")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

genre_text = StringVar()
e4 = Entry(window, textvariable=genre_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=8, width=50)
list1.grid(row=2, column=0, rowspan=6,columnspan=4)

list1.bind("<<ListboxSelect>>", get_selected_row)

scroll1 = Scrollbar(window)
scroll1.grid(row=2, column=3, rowspan=6)

list1.configure(yscrollcommand=scroll1.set)
scroll1.configure(command=list1.yview)

b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2,column=5)

b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3,column=5)

b3 = Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=4,column=5)

b4 = Button(window, text="Update Entry", width=12, command=update_command)
b4.grid(row=5,column=5)

b5 = Button(window, text="Delete Entry", width=12, command=delete_command)
b5.grid(row=6,column=5)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7,column=5)

statusbar = Label(window, text="ROXXX LIBRARY®", anchor=W)
statusbar.grid(row=8, column=2)

right_ext = Label(window, bd=1)
right_ext.grid(row=0, column=6, rowspan=8)

window.mainloop()