# creates database myrestaurant database
# creates tables for the database

import MySQLdb

# connect to database
mydb = MySQLdb.connect(
    host="localhost",           # host
    user="root",                # username
    passwd="Jonghyun3908!",     # password
    database="myrestaurant"     # database name
)

mycursor = mydb.cursor()

# create customer table
sql = "CREATE TABLE IF NOT EXISTS my_customers (cust_id INT PRIMARY KEY, name VARCHAR(30), party_size INT, reservation " \
      "TIME) "
mycursor.execute(sql)

# create table table
sql = "CREATE TABLE IF NOT EXISTS my_tables (table_no INT PRIMARY KEY, table_size INT, occupied INT)"
mycursor.execute(sql)

# create employee table
sql = "CREATE TABLE IF NOT EXISTS my_employee (emp_id INT PRIMARY KEY, f_name VARCHAR(30), l_name VARCHAR(30), " \
      "role VARCHAR(30)) "
mycursor.execute(sql)

# create waitlist table
sql = "CREATE TABLE IF NOT EXISTS my_waitlist (pos INT, cust_id INT, cust_name VARCHAR(30), party_size INT)"
mycursor.execute(sql)

# create menu table
sql = "CREATE TABLE IF NOT EXISTS my_menu (dish_no INT PRIMARY KEY, dish_name VARCHAR(30), description VARCHAR(255), " \
      "cal INT, price DECIMAL(6,2)) "
mycursor.execute(sql)

# create order table
sql = "CREATE TABLE IF NOT EXISTS my_order (order_no INT PRIMARY KEY, order_name VARCHAR(30), quantity INT)"
mycursor.execute(sql)

# create receipt table
sql = "CREATE TABLE IF NOT EXISTS my_receipt (receipt_no INT PRIMARY KEY, cust_name VARCHAR(30), name VARCHAR(30), " \
      "day DATE, time TIME, server_name VARCHAR(60)) "
mycursor.execute(sql)

# check if tables are added
# print table
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

mydb.close()