import mysql.connector

# create host
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="restaurantadmin",
    passwd="secret",
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

# create database
sql = "CREATE DATABASE myrestaurant"
mycursor.execute(sql)

mydb.close()

# check to see if database exist
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="restaurantadmin",
    passwd="secret",
    database="myrestaurant",
    auth_plugin='mysql_native_password'
)

# create cursor to execute commands
mycursor = mydb.cursor()

# create tables array
tables = []

tbl1 = "CREATE TABLE customers (cust_id INT PRIMARY KEY, name VARCHAR(30), party_size INT, reservation TIME)"
tables.append(tbl1)
tbl2 = "CREATE TABLE tables (table_no INT PRIMARY KEY, table_size INT, server_id INT, occupied INT)"
tables.append(tbl2)
tbl3 = "CREATE TABLE employee (emp_id INT PRIMARY KEY, f_name VARCHAR(30), l_name VARCHAR(30), role VARCHAR(30), serving INT)"
tables.append(tbl3)
tbl4 = "CREATE TABLE waitlist (pos INT PRIMARY KEY, cust_id INT, cust_name VARCHAR(30), party_size INT"
tables.append(tbl4)
tbl5 = "CREATE TABLE menu (dish_no INT PRIMARY KEY, dish_name VARCHAR(30), description VARCHAR(255),  cal INT, price DECIMAL(6,2)"
tables.append(tbl5)
tbl6 = "CREATE TABLE order (order_no INT PRIMARY KEY, dish_name VARCHAR(30), quantity INT"
tables.append(tbl6)
tbl7 = "CREATE TABLE receipt (receipt_no INT PRIMARY KEY, cust_name VARCHAR(30), name VARCHAR(30), day DATE, time TIME, server_name VARCHAR(60), "
tables.append(tbl7)

# create all tables
for sql in tables:
    mycursor.execute(sql)

# check if tables are added
# print table
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

mydb.close()