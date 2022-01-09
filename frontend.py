from tkinter import *
import backend

def get_selected_row(event):
    try:# Listbox curselection is used to display the selected item(s).
        # curselection is a predefined function that fetches the value(s) of a selected item or items.
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)

        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)  # 0,END --> Delete everything from 0 to end of list
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(name_text.get(),group_text.get(),rollno_text.get(),branch_text.get()): # get() method is used in Python to retrieve a value from StringVar
        list1.insert(END,row)

def insert_command():
    backend.insert(name_text.get(),group_text.get(),rollno_text.get(),branch_text.get())
    list1.delete(0,END)
    list1.insert(END,(name_text.get(),group_text.get(),rollno_text.get(),branch_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],name_text.get(),group_text.get(),rollno_text.get(),branch_text.get())

window = Tk()
window.wm_title("Students Record")
window.geometry("535x258")

# LABEL WIDGETS

l1=Label(window, text="Name")
l1.grid(row=0,column=0)

l2=Label(window, text="Group")
l2.grid(row=0,column=2)

l3=Label(window, text="Roll No.")
l3.grid(row=1,column=0)

l4=Label(window, text="Branch")
l4.grid(row=1,column=2)

# ENTRY WIDGETS

name_text=StringVar() # StringVar method holds a string .By default it holds null string.
e1=Entry(window,textvariable=name_text,borderwidth=1,relief="solid")
e1.grid(row=0,column=1)

group_text=StringVar()
e2=Entry(window,textvariable=group_text,borderwidth=1,relief="solid")
e2.grid(row=0,column=3)

rollno_text=StringVar()
e3=Entry(window,textvariable=rollno_text,borderwidth=1,relief="solid")
e3.grid(row=1,column=1)

branch_text=StringVar()
e4=Entry(window,textvariable=branch_text,borderwidth=1,relief="solid")
e4.grid(row=1,column=3)

# LISTBOX

list1=Listbox(window,height=13,width=60,borderwidth=1,relief="solid")
list1.grid(row=3, column=0, rowspan=7,columnspan=2)

sb=Scrollbar(window)
sb.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb.set)  # To connect a scrollbar to another widget w, set w's xscrollcommand/yscrollcommand to the scrollbar's set() method.
sb.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row) # This is sent to a listbox when the set of selected item(s) in the listbox is updated.

# BUTTON WIDGETS

b1=Button(window,text="View All",width=13,command=view_command) #-->do not pass brackets here because you want this function to execute when u press button
b1.grid(row=3,column=3)

b2=Button(window,text="Add Entry",width=13,command=insert_command)
b2.grid(row=4,column=3)

b3=Button(window,text="Search Entry",width=13,command=search_command)
b3.grid(row=5,column=3)

b4=Button(window,text="Update Entry",width=13,command=update_command)
b4.grid(row=6,column=3)

b5=Button(window,text="Delete Entry",width=13,command=delete_command)
b5.grid(row=7,column=3)

b6=Button(window,text="Close",width=13,command=window.destroy)
b6.grid(row=8,column=3)

#window.configure(bg="light blue")
window.mainloop()
