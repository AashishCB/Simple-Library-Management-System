Go to the link for download: https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.22.0.msi

follow the video for the further installation process of MySQL Server: https://www.youtube.com/watch?v=yxYba3ZSWc8

> Since MySQL Server will be enough to build the application.

Remember the name for your database (Ex:MYSQL80 or something that you changed it to) and the password.

Use the below line for creating the table in MySQL command line:
` CREATE TABLE books (bid VARCHAR(20) PRIMARY KEY NOT NULL, title VARCHAR(30), author VARCHAR(30), status VARCHAR(30)); `

` CREATE TABLE books_issued (bid VARCHAR(20) PRIMARY KEY NOT NULL, issuedto VARCHAR(30)); `

Use:
` desc books; `
` desc books_issued; `
to see the table description
