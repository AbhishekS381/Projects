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
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), Id_text.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), Id_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), Id_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), Id_text.get())

window = Tk()
window.configure(background='black')

window.wm_title("Marvel Cinematic Universe")
window.resizable(0,0)

l1=Label(window, text="Title:", bg="black", foreground='white')
l1.grid(row=0, column=0)

l2=Label(window, text="Director:", bg="black", foreground='white')
l2.grid(row=0, column=3)

l3=Label(window, text="Year:", bg="black", foreground='white')
l3.grid(row=1, column=0)

l4=Label(window, text="Id:", bg="black", foreground='white')
l4.grid(row=1, column=3)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=4)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

Id_text = StringVar()
e4 = Entry(window, textvariable=Id_text)
e4.grid(row=1, column=4)

list1 = Listbox(window, height=8, width=50)
list1.grid(row=2, column=1, rowspan=6,columnspan=4)

list1.bind("<<ListboxSelect>>", get_selected_row)

scroll1 = Scrollbar(window)
scroll1.grid(row=2, column=4, rowspan=6)

list1.configure(yscrollcommand=scroll1.set)
scroll1.configure(command=list1.yview)

b1 = Button(window, text="View All", width=12, bg="black", foreground='white', activebackground='white' ,activeforeground='black', command=view_command)
b1.grid(row=2,column=0)

b2 = Button(window, text="Search Movie", width=12, bg="black", foreground='white', activebackground='white' ,activeforeground='black', command=search_command)
b2.grid(row=3,column=0)

b3 = Button(window, text="Add Movie", width=12, bg="black", foreground='white', activebackground='white' ,activeforeground='black', command=add_command)
b3.grid(row=4,column=0)

b4 = Button(window, text="Update Movie", width=12, bg="black", foreground='white', activebackground='white' ,activeforeground='black', command=update_command)
b4.grid(row=5,column=0)

b5 = Button(window, text="Delete Movie", width=12, bg="black", foreground='white', activebackground='white' ,activeforeground='black', command=delete_command)
b5.grid(row=6,column=0)

b6 = Button(window, text="Close", width=12, bg="black", foreground='white', activebackground='white' ,activeforeground='black', command=window.destroy)
b6.grid(row=7,column=0)

statusbar = Label(window, text="MARVEL®", bg="black", foreground='white', anchor=W)
statusbar.grid(row=8, column=2)

right_ext = Label(window, bd=1)
right_ext.grid(row=0, column=6, rowspan=8)

window.mainloop()
