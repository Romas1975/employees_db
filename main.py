from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

root = Tk()             
 
# Open window having dimension 700x50
root.geometry('700x50')
 
# Create a Button
button = Button(root, text = 'Welcome!', bd = '5',
                          command = root.destroy)
 
# Set the position of button on the top of window.  
button.pack(side = 'top')   
 
root.mainloop()
  

db = Database("Employee.db")
root = Tk()
root.title("Employee Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

name = StringVar()
age = StringVar()
dob = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()

# Entries Frame
entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Employee Management System", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

labelName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
labelName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
textName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=30)
textName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

labelAge = Label(entries_frame, text="Age", font=("Calibri", 16), bg="#535c68", fg="white")
labelAge.grid(row=1, column=2, padx=10, pady=10, sticky="w")
textAge = Entry(entries_frame, textvariable=age, font=("Calibri", 16), width=30)
textAge.grid(row=1, column=3, padx=10, pady=10, sticky="w")

labeldob = Label(entries_frame, text="D.O.B", font=("Calibri", 16), bg="#535c68", fg="white")
labeldob.grid(row=2, column=0, padx=10, pady=10, sticky="w")
textDob = Entry(entries_frame, textvariable=dob, font=("Calibri", 16), width=30)
textDob.grid(row=2, column=1, padx=10, pady=10, sticky="w")

labelEmail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white")
labelEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
textEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=30)
textEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

labelGender = Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white")
labelGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
comboGender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female")
comboGender.grid(row=3, column=1, padx=10, sticky="w")

labelContact = Label(entries_frame, text="Contact No", font=("Calibri", 16), bg="#535c68", fg="white")
labelContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
textContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=30)
textContact.grid(row=3, column=3, padx=10, sticky="w")

labelAddress = Label(entries_frame, text="Address", font=("Calibri", 16), bg="#535c68", fg="white")
labelAddress.grid(row=4, column=0, padx=10, pady=10, sticky="w")

textAddress = Text(entries_frame, width=85, height=5, font=("Calibri", 16))
textAddress.grid(row=5, column=0, columnspan=4, padx=10, sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    dob.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    textAddress.delete(1.0, END)
    textAddress.insert(END, row[7])

def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_employee():
    if textName.get() == "" or textAge.get() == "" or textDob.get() == "" or textEmail.get() == "" or comboGender.get() == "" or textContact.get() == "" or textAddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(textName.get(),textAge.get(), textDob.get() , textEmail.get() ,comboGender.get(), textContact.get(), textAddress.get(
            1.0, END))
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()



def update_employee():
    if textName.get() == "" or textAge.get() == "" or textDob.get() == "" or textEmail.get() == "" or comboGender.get() == "" or textContact.get() == "" or textAddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0],textName.get(), textAge.get(), textDob.get(), textEmail.get(), comboGender.get(), textContact.get(),
              textAddress.get(
                  1.0, END))
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()


def delete_employee():
    db.remove(row[0])
    clearAll()
    dispalyAll()


def clearAll():
    name.set("")
    age.set("")
    dob.set("")
    gender.set("")
    email.set("")
    contact.set("")
    textAddress.delete(1.0, END)


button_frame = Frame(entries_frame, bg="#535c68")
button_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
buttonAdd = Button(button_frame, command=add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
buttonEdit = Button(button_frame, command=update_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
buttonDelete = Button(button_frame, command=delete_employee, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
buttonClear = Button(button_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)

# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1980, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=5)
tv.heading("2", text="Name")
tv.heading("3", text="Age")
tv.column("3", width=5)
tv.heading("4", text="D.O.B")
tv.column("4", width=10)
tv.heading("5", text="Email")
tv.heading("6", text="Gender")
tv.column("6", width=10)
tv.heading("7", text="Contact")
tv.heading("8", text="Address")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()
root.mainloop()