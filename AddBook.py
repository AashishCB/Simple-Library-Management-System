from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def bookRegister():

	bid = bookInfo1.get()
	title = bookInfo2.get()
	author = bookInfo3.get()
	status = bookInfo4.get()
	status = status.lower()

	insertBooks = "insert into "+bookTable +" values ('"+bid+"', '"+title+"', '"+author+"', '"+status+"')"
	print(insertBooks)
	try:
		cur.execute(insertBooks)
		con.commit()
		messagebox.showinfo('Success',"Book added successfully")
	except:
		messagebox.showinfo("Error","Can't add data into Database")
	
	print(bid)
	print(title)
	print(author)
	print(status)
	root.destroy()

def addBook():

	global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

	root = Tk()
	root.title("Library")
	root.minsize(width = 400, height = 400)
	root.geometry("600x500")

	mypass = "A@shish.2"
	mydatabase = "MYSQL"
	con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
	cur = con.cursor()

	bookTable = "books"
	
	Canvas1 = Canvas(root)
	Canvas1.config(bg="#ff6e40")
	Canvas1.pack(expand=True, fill=BOTH)

	headFrame1 = Frame(root,bg="#FFBB00",bd=5)
	headFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
	headLabel = Label(headFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
	headLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

	labelFrame = Frame(root,bg='black')
	labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

	Label(labelFrame,text="Book ID : ", bg='black', fg='white').place(relx=0.05,rely=0.2, relheight=0.08)
	bookInfo1 = Entry(labelFrame)
	bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
	# Title
	Label(labelFrame,text="Title : ", bg='black', fg='white').place(relx=0.05,rely=0.35, relheight=0.08)
	bookInfo2 = Entry(labelFrame)
	bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)							        
	# Book Author
	Label(labelFrame,text="Author : ", bg='black', fg='white').place(relx=0.05,rely=0.50, relheight=0.08)
	bookInfo3 = Entry(labelFrame)
	bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
	# Book Status
	Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white').place(relx=0.05,rely=0.65, relheight=0.08)
	bookInfo4 = Entry(labelFrame)
	bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
	#Submit Button
	Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister).place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
	Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy).place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)				        
	root.mainloop()
