from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *

# connecting to the MySql server
mypass = "A@shish.2"
mydatabase = "MYSQL"
con = pymysql.connect(host = "localhost", user = "root", password = mypass, database = mydatabase)
cur = con.cursor()

# Desingning the Window
root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

same=True
n=0.25
# Adding a background image
background_image =Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size
newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n)
else:
    newImageSizeHeight = int(imageSizeHeight/n)

background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headFrame = Frame(root, bg = "#FFBB00", bd = 5)
headFrame.place(relx = 0.2, rely = 0.1, relwidth = 0.6, relheight = 0.16)
headLabel = Label(headFrame, text = "Wecome to \n The Library", bg = 'black', fg = 'white', font = ('Courier', 15))
headLabel.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

Button(root,text="Add Book Details",bg='black', fg='white', command=None).place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
Button(root,text="Delete Book",bg='black', fg='white', command=None).place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
        
Button(root,text="View Book List",bg='black', fg='white', command=None).place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
	    
Button(root,text="Issue Book to Student",bg='black', fg='white', command = None).place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
       
Button(root,text="Return Book",bg='black', fg='white', command = None).place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()
