# Library Management System
A database system to manage record of books in library.

### Prerequisites

#### tkinter
Standard GUI Python library that is one of the fastest and easiest ways to build GUI applications.

#### pillow
Pillow is a Python Imaging Library (PIL), which adds support for opening, manipulating, and saving images.
**To install the library**

` pip install pillow `

#### pymysql
PyMySQL is an interface for connecting to a MySQL database server from Python.
**To install the library**

` pip install pymysql `

> Note: You are required to have MySQL server installed on your system in order to make pymysql work.

Go to the link for download: https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.22.0.msi

follow the video for the further installation process of MySQL Server: https://www.youtube.com/watch?v=yxYba3ZSWc8

> 'MySQL Server' will be enough to build the application.

Remember the name for your database (Ex:MYSQL80 or something that you changed it to) and the password.

After Installation,

-Go to MySQL command line. 

-Enter the password.

-Enter the command ` use [db]; ` [db] shall be replaced by the database name.

Use the below line for creating the table in MySQL command line:
	
` CREATE TABLE books (bid VARCHAR(20) PRIMARY KEY NOT NULL, title VARCHAR(30), author VARCHAR(30), status VARCHAR(30)); `

` CREATE TABLE books_issued (bid VARCHAR(20) PRIMARY KEY NOT NULL, issuedto VARCHAR(30)); `

Use the following command:

` desc books; `

` desc books_issued; `

to see the table description
------------------------------------------------------------------------------------------------------------------------
> You must have python3 installed on your computer to run it.

#### To run the .py file:
Run the below command in terminal or cmd through any IDE you prefer

` $ python main.py `

or 

` $ python3 main.py `