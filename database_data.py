# inputting data into database

import MySQLdb

# create host
mydb = MySQLdb.connect(
    host="localhost",           # host
    user="root",                # username
    passwd="Jonghyun3908!",     # password
    database="myrestaurant"     # database name
)

mycursor = mydb.cursor()

# adding entries to tables table
# there are 10 tables: 6 size of 4, 2 size of 6, and 2 size of 8
sql = "INSERT INTO my_tables(table_no, table_size, occupied) VALUES ('%d', '%d', '%d')" % (1, 4, 0)
mycursor.execute(sql)

sql = "INSERT INTO my_tables(table_no, table_size, occupied) VALUES ('%d', '%d', '%d')" % (2, 4, 0)
mycursor.execute(sql)

sql = "INSERT INTO my_tables(table_no, table_size, occupied) VALUES ('%d', '%d', '%d')" % (3, 4, 0)
mycursor.execute(sql)

sql = "INSERT INTO my_tables(table_no, table_size, occupied) VALUES ('%d', '%d', '%d')" % (4, 4, 0)
mycursor.execute(sql)

sql = "INSERT INTO my_tables(table_no, table_size, occupied) VALUES ('%d', '%d', '%d')" % (5, 4, 0)
mycursor.execute(sql)

sql = "INSERT INTO my_tables(table_no, table_size, occupied) VALUES ('%d', '%d', '%d')" % (6, 4, 0)
mycursor.execute(sql)

sql = "INSERT INTO my_tables(table_no, table_size, occupied) VALUES ('%d', '%d', '%d')" % (7, 6, 0)
mycursor.execute(sql)

sql = "INSERT INTO my_tables(table_no, table_size, occupied) VALUES ('%d', '%d', '%d')" % (8, 6, 0)
mycursor.execute(sql)

sql = "INSERT INTO my_tables(table_no, table_size, occupied) VALUES ('%d', '%d', '%d')" % (9, 8, 0)
mycursor.execute(sql)

sql = "INSERT INTO my_tables(table_no, table_size, occupied) VALUES ('%d', '%d', '%d')" % (10, 8, 0)
mycursor.execute(sql)

# check if records are inserted correctly
# print table
mycursor.execute("SELECT * FROM my_tables")

for x in mycursor:
    print(x)

# adding entries to employee table
# added 8 employees
sql = "INSERT INTO my_employee(emp_id, f_name, l_name, role) VALUES ('%d', '%s', '%s', '%s')" % (1, 'Jack', 'Ryan', 'waiter')
mycursor.execute(sql)

sql = "INSERT INTO my_employee(emp_id, f_name, l_name, role) VALUES ('%d', '%s', '%s', '%s')" % (2, 'Sam', 'Bae', 'waiter')
mycursor.execute(sql)

sql = "INSERT INTO my_employee(emp_id, f_name, l_name, role) VALUES ('%d', '%s', '%s', '%s')" % (3, 'Alice', 'Kim', 'waitress')
mycursor.execute(sql)

sql = "INSERT INTO my_employee(emp_id, f_name, l_name, role) VALUES ('%d', '%s', '%s', '%s')" % (4, 'Bob', 'Dill', 'waiter')
mycursor.execute(sql)

sql = "INSERT INTO my_employee(emp_id, f_name, l_name, role) VALUES ('%d', '%s', '%s', '%s')" % (5, 'Pepper', 'Pots', 'waitress')
mycursor.execute(sql)

sql = "INSERT INTO my_employee(emp_id, f_name, l_name, role) VALUES ('%d', '%s', '%s', '%s')" % (6, 'Ryan', 'Lee', 'chef')
mycursor.execute(sql)

sql = "INSERT INTO my_employee(emp_id, f_name, l_name, role) VALUES ('%d', '%s', '%s', '%s')" % (7, 'Kimberly', 'So', 'cashier')
mycursor.execute(sql)

sql = "INSERT INTO my_employee(emp_id, f_name, l_name, role) VALUES ('%d', '%s', '%s', '%s')" % (8, 'Tom', 'Brady', 'receptionist')
mycursor.execute(sql)

# check if records are inserted correctly
# print table
mycursor.execute("SELECT * FROM my_employee")

for x in mycursor:
    print(x)

# adding entries to menu table
sql = "INSERT INTO my_menu(dish_no, dish_name, description,  cal, price) VALUES ('%d', '%s', '%s', '%d', '%.2f')" % (1, 'Filet O Fish', 'Fish Sandwich', 360, 3.39)
mycursor.execute(sql)

sql = "INSERT INTO my_menu(dish_no, dish_name, description,  cal, price) VALUES ('%d', '%s', '%s', '%d', '%.2f')" % (2, 'Southern Style Chicken', 'Chicken Sandwich', 400, 3.39)
mycursor.execute(sql)

sql = "INSERT INTO my_menu(dish_no, dish_name, description,  cal, price) VALUES ('%d', '%s', '%s', '%d', '%.2f')" % (3, '3pc Chicken', 'Chicken Nuggets', 400, 3.69)
mycursor.execute(sql)

sql = "INSERT INTO my_menu(dish_no, dish_name, description,  cal, price) VALUES ('%d', '%s', '%s', '%d', '%.2f')" % (4, 'Classic Chicken (Grilled)', 'Grilled Chicken Sandwich', 530, 3.39)
mycursor.execute(sql)

sql = "INSERT INTO my_menu(dish_no, dish_name, description,  cal, price) VALUES ('%d', '%s', '%s', '%d', '%.2f')" % (5, 'Cheeseburger', 'Quarter Pounder w/ Cheese', 510, 3.49)
mycursor.execute(sql)

sql = "INSERT INTO my_menu(dish_no, dish_name, description,  cal, price) VALUES ('%d', '%s', '%s', '%d', '%.2f')" % (6, 'Double Cheeseburger', 'Two Patties', 740, 4.39)
mycursor.execute(sql)

sql = "INSERT INTO my_menu(dish_no, dish_name, description,  cal, price) VALUES ('%d', '%s', '%s', '%d', '%.2f')" % (7, 'Angus Mushroom and Swiss', 'Mushrooms and Swish Cheese', 770, 3.99)
mycursor.execute(sql)

sql = "INSERT INTO my_menu(dish_no, dish_name, description,  cal, price) VALUES ('%d', '%s', '%s', '%d', '%.2f')" % (8, 'Angus Bacon and Cheese', 'Bacon and Cheese', 790, 3.99)
mycursor.execute(sql)

sql = "INSERT INTO my_menu(dish_no, dish_name, description,  cal, price) VALUES ('%d', '%s', '%s', '%d', '%.2f')" % (9, 'Ceasar Salad', 'Contains chicken', 420, 2.99)
mycursor.execute(sql)

sql = "INSERT INTO my_menu(dish_no, dish_name, description,  cal, price) VALUES ('%d', '%s', '%s', '%d', '%.2f')" % (10, 'Ice Cream Sundae', '1 scoop, chocolate, and 1 choice of topping', 240, 1.39)
mycursor.execute(sql)

sql = "INSERT INTO my_menu(dish_no, dish_name, description,  cal, price) VALUES ('%d', '%s', '%s', '%d', '%.2f')" % (11, 'French Fries', 'Medium Size', 360, 1.99)
mycursor.execute(sql)

sql = "INSERT INTO my_menu(dish_no, dish_name, description,  cal, price) VALUES ('%d', '%s', '%s', '%d', '%.2f')" % (12, 'Soda', 'Small Size (Refillable)', 110, 1.00)
mycursor.execute(sql)

sql = "INSERT INTO my_menu(dish_no, dish_name, description,  cal, price) VALUES ('%d', '%s', '%s', '%d', '%.2f')" % (13, 'Milk Shake', 'Flavors: Chocolate, Vanilla, or Strawberry', 420, 2.39)
mycursor.execute(sql)

sql = "INSERT INTO my_menu(dish_no, dish_name, description,  cal, price) VALUES ('%d', '%s', '%s', '%d', '%.2f')" % (14, 'House Coffee', 'Medium Roast, Small Size', 150, 1.50)
mycursor.execute(sql)

# check if records are inserted correctly
# print table
mycursor.execute("SELECT * FROM my_menu")

for x in mycursor:
    print(x)

mydb.close()