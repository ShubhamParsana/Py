from customtkinter import *
import mysql.connector
from tkinter import messagebox


mydb = mysql.connector.connect(host="localhost",user="root",password="",database="py")

mycursor=mydb.cursor()

def login():
    unm=txtunm.get()
    unm=txtpwd.get()


root = CTk()
root.geometry("300x300")
txtunm = CTkEntry(root,placeholder_text="Username", placeholder_text_color="Orange", text_color="Orange")
txtunm.pack(fill="x",padx=2,pady=2)
txtpwd = CTkEntry(root,placeholder_text="Password",placeholder_text_color="Orange",text_color="Orange")
txtpwd.pack(fill="x",padx=2,pady=2)
CTkButton(root,fg_color="Red",text="Log in",command="login").pack(padx=2,pady=2,fill="x")
root.mainloop()
