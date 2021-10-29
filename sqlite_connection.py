"""
Author: Bharti Sinha
Date: 29th October 2021 

Standard process to interact with the databases consists of 5 steps

1. Connect to the Database
2. Create a cursor object
3. Write an SQL Query
4. commit changes to the database
5. Close the connection to the database

"""

# import the built-in library
import sqlite3

# Step 1: Connect to a database

# if the database does not exist, a new database will be created 
# then a connection to the database will be established, 
# if the database exists, a connection will be established
conn = sqlite3.connect("practice.db")

# Step 2: create a cursor object on the connection
cur = conn.cursor()

#Step 3: write an SQL query

# include "IF NOT EXISTS" consition to avoid getting errors when to rerun the code
# The first value inside the store table is column name - item, quantity and price
# The values following the column names are the type of data the column holds - TEXT, INTEGER and REAL
cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

# insert some data to the table
# insert values in the same order as the column in the table 
cur.execute("INSERT INTO store VALUES ('Wine Glass', 10, 12.0)")

#Step 4: commmit changes to the database
conn.commit()

#step 5: close the connection to the table
conn.close()


# If we run the file repeately, the same values will get inserted into the table, i.e. 'Wine Glass', 10, 12.0
# To insert values as needed, please check `sqlite.py` file in the repository





