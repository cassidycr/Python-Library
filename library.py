import cryptography
from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
from tkinter import messagebox
from add_book import add_book, book_register
from view_books import view_books
from delete_book import delete_book, delete
from issue_books import issue, issue_book
from return_books import returnn, return_book


mypass = "Scarlouvijo3!" #use your own password
mydatabase="library" #The database name
con = pymysql.connect (host="localhost",user="root",password=mypass,database=mydatabase)
#root is the username here
cur = con.cursor() #cur -> cursor

root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

same=True
n=0.25
# Adding a background image
canvas = Canvas(width=600, height=800, bg='white')
canvas.pack(expand=YES, fill=BOTH)

image = ImageTk.PhotoImage(file="lib.jpg")
canvas.create_image(10, 10, image=image, anchor=NW)

headingFrame1 = Frame(root,bg="#ECC1B2",bd=1)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n My Library", bg='white', fg='black', font=('Calibri Light',23))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Book Details",bg='white', fg='black', command=add_book)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete_book)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Book List",bg='black', fg='white', command=view_books)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issue_book)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Book",bg='black', fg='white', command = return_book)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()