from tkinter import *
import mysql.connector
 
root = Tk()
root.title("Contact Book")

canvas = Canvas(root,width=500,height=400)
canvas.pack()

# add block
 
def AddWindow():
    newWindow = Toplevel(root)
    newWindow.title("Add contact")
    newWindow.geometry("400x200")

    frame = Frame(newWindow)
    frame.place(relx=0.3,rely=0.1,relwidth=0.8,relheight=0.8)

    nameLabel = Label(frame,text="Name: ")
    nameLabel.grid(row=0,column=1)
    nameEntry = Entry(frame)
    nameEntry.grid(row=0,column=2)

    phoneLabel = Label(frame,text="Phone number: ")
    phoneLabel.grid(row=1,column=1)
    phoneEntry = Entry(frame)
    phoneEntry.grid(row=1,column=2)

    eLabel = Label(frame,text="Email: ")
    eLabel.grid(row=2,column=1)
    eEntry = Entry(frame)
    eEntry.grid(row=2,column=2)

    def get_data(name,phone,email):
        conn = mysql.connector.connect(host="localhost",user="root",password="password12345",database="contacts")
        ccursor = conn.cursor()

        query = "INSERT INTO contactbook (name,phone_number,email) VALUES (%s, %s,%s)"
        ccursor.execute(query,(name,phone,email))
        conn.commit()
        conn.close()

    button = Button(frame,text="Add",command=lambda:get_data(nameEntry.get(),phoneEntry.get(),eEntry.get()))
    button.grid(row=5,column=1)
    
addButton = Button(root,text ="Add Contact",command = AddWindow)
canvas.create_window(50,20,window=addButton)

# search block

searchlabel = Label(root,text="Search contact:")
canvas.create_window(150,20,window=searchlabel)
searchEntry = Entry(root)
canvas.create_window(260,20,window=searchEntry)

def displaydata(data):
    lbox=Listbox(root,width=50,height=1)
    canvas.create_window(260,50,window=lbox)
    lbox.insert(END,data)

def search(name):
    conn = mysql.connector.connect(host="localhost",user="root",password="password12345",database="contacts")
    ccursor = conn.cursor()

    query = "SELECT * FROM contactbook WHERE name=(%s)"
    ccursor.execute(query,(name,))
    data = ccursor.fetchone()
    displaydata(data)
    conn.commit()
    conn.close()

searchbutton = Button(root,text="Search",command=lambda:search(searchEntry.get()))
canvas.create_window(365,20,window=searchbutton)

# delete block

dellabel = Label(root,text="Delete contact: ")
canvas.create_window(150,80,window=dellabel)
delentry = Entry(root)
canvas.create_window(260,80,window=delentry)

def delete(name):
    conn = mysql.connector.connect(host="localhost",user="root",password="password12345",database="contacts")
    ccursor = conn.cursor()
    query = "DELETE FROM contactbook WHERE name = (%s)"
    ccursor.execute(query,(name,))
    conn.commit()
    conn.close()

delbutton = Button(root,text="Delete",command = lambda:delete(delentry.get()) )
canvas.create_window(365,80,window=delbutton)

# update block

def updateWindow():
    newWindow = Toplevel(root)
    newWindow.title("Update Contact")
    newWindow.geometry("600x200")

    frame = Frame(newWindow)
    frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

    # name
    nameLabel = Label(frame,text=" Original Name: ")
    nameLabel.grid(row=0,column=1)
    nameEntry = Entry(frame)
    nameEntry.grid(row=0,column=2)
    
    name1Label = Label(frame,text=" Updated Name: ")
    name1Label.grid(row=0,column=3)
    name1Entry = Entry(frame)
    name1Entry.grid(row=0,column=4)

    def updatename(uname,name):
        conn = mysql.connector.connect(host="localhost",user="root",password="password12345",database="contacts")
        ccursor = conn.cursor()
        query = "UPDATE contactbook SET name = (%s) WHERE name = (%s)"
        ccursor.execute(query,(uname,name))
        conn.commit()
        conn.close()

    updatenamebutton = Button(frame,text ="Update",command=lambda:updatename(name1Entry.get(),nameEntry.get()))
    updatenamebutton.grid(row=0,column=6)

    # phone number
    phoneLabel = Label(frame,text=" Original Phone: ")
    phoneLabel.grid(row=2,column=1)
    phoneEntry = Entry(frame)
    phoneEntry.grid(row=2,column=2)
    
    phone1Label = Label(frame,text=" Updated phone: ")
    phone1Label.grid(row=2,column=3)
    phone1Entry = Entry(frame)
    phone1Entry.grid(row=2,column=4)

    def updatephone(uphone,phone):
        conn = mysql.connector.connect(host="localhost",user="root",password="password12345",database="contacts")
        ccursor = conn.cursor()
        query = "UPDATE contactbook SET phone_number = (%s) WHERE phone_number = (%s)"
        ccursor.execute(query,(uphone,phone))
        conn.commit()
        conn.close()

    updatephonebutton = Button(frame,text ="Update",command=lambda:updatephone(phone1Entry.get(),phoneEntry.get()))
    updatephonebutton.grid(row=2,column=6)

    # email
    emailLabel = Label(frame,text=" Original Email: ")
    emailLabel.grid(row=4,column=1)
    emailEntry = Entry(frame)
    emailEntry.grid(row=4,column=2)
    
    email1Label = Label(frame,text=" Updated Email: ")
    email1Label.grid(row=4,column=3)
    email1Entry = Entry(frame)
    email1Entry.grid(row=4,column=4)

    def updatemail(uemail,email):
        conn = mysql.connector.connect(host="localhost",user="root",password="password12345",database="contacts")
        ccursor = conn.cursor()
        query = "UPDATE contactbook SET  email = (%s) WHERE  email = (%s)"
        ccursor.execute(query,(uemail,email))
        conn.commit()
        conn.close()

    updateemailbutton = Button(frame,text ="Update",command=lambda:updatemail(email1Entry.get(),emailEntry.get()))
    updateemailbutton.grid(row=4,column=6)

updateButton = Button(root,text ="Update Contact",command=updateWindow)
canvas.create_window(50,80,window=updateButton)

# display
def displayall():
    conn = mysql.connector.connect(host="localhost",user="root",password="password12345",database="contacts")
    ccursor = conn.cursor()
    query = "SELECT * FROM contactbook"
    ccursor.execute(query)
    data = ccursor.fetchall()
    lbox=Listbox(root,width=50,height=10)
    canvas.create_window(260,190,window=lbox)
    for x in data:
        lbox.insert(END,x)
    
    conn.commit()
    conn.close()

displayButton = Button(root,text ="Display Contact",command=displayall)
canvas.create_window(50,120,window=displayButton)

root.mainloop()
