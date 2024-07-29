from tkinter import *
from PIL import ImageTk,Image #PL -> Pillow
import pymysql
from tkinter import messagebox
from Addbooks import *
from Deletebooks import *
from Viewbooks import *
from Issuebooks import *
from Returnbooks import *

mypass="Raghu@2004"
mydatabase="db"
con=pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur=con.cursor()


root=Tk()
root.title("LIBRARY")
root.minsize(width=600,height=600)
root.geometry("600x500")

headingFrame1 = Frame(root,bg="#e6ffff",bd=8)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text=" Welcome to Library ", bg='#003366', fg='white', font=('Times new Roman',20,"bold"))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


btn1 = Button(root,text="Add Book Details",bg='#00ace6', fg='white',font=('bold',18),command=addBook)
btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book",bg='#00ace6', fg='white',font=('bold',18),command=delete)
btn2.place(relx=0.28,rely=0.42, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Book List",bg='#00ace6', fg='white',font=('bold',18), command=View)
btn3.place(relx=0.28,rely=0.54, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue Book to Student",bg='#00ace6', fg='white',font=('bold',18), command = issueBook)
btn4.place(relx=0.28,rely=0.66, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Book",bg='#00ace6', fg='white',font=('bold',18), command = returnBook)
btn5.place(relx=0.28,rely=0.78, relwidth=0.45,relheight=0.1)

root.mainloop()