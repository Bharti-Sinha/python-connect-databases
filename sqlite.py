"""
Author: Bharti Sinha
Date: 29th October 2021 

"""

# import the built-in library
import sqlite3

def create_table():
    '''
    The method connects to a database and 
    creates a table practice.db if it does not already exists.
    '''
    conn = sqlite3.connect("practice.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    '''
    Insert values into the table as recieved in the arguments

    @param: item: item to be inserted,
            quantity: quantity of the item, 
            price: price of the item

    '''
    conn = sqlite3.connect("practice.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    '''
    The method fetches all the rows from the database and prints it as a python list

    '''
    conn = sqlite3.connect("practice.db")
    cur = conn.cursor()
    # select all columns from the table
    cur.execute("SELECT * FROM store")

    #fetchall returns all the rows as python list
    rows = cur.fetchall()
    conn.close()
    return rows


insert("Coffee", 2, 3)
insert("Tea", 1, 2.5)
insert("Cookies", 4, 5)

print(view())



