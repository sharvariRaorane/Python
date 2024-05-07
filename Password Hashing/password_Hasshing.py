import bcrypt
from tkinter import *

def validate(passwordnew):
    password = b"thisismypassword"#demopassword
    hashed = bcrypt.hashpw(password,bcrypt.gensalt())

    passwordnew = bytes(passwordnew,encoding='utf-8')

    if bcrypt.checkpw(passwordnew,hashed):
        print("Logged in")
    else:
        print("Invalid password")

root = Tk()

root.geometry("300x300")

password_entry = Entry(root)
password_entry.pack()

button = Button(text="validate",command= lambda: validate(password_entry.get()))
button.pack()

root.mainloop()

