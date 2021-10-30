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

def delete(item):
    '''
    The method deleted ALL the rows from the database where item column has a particular value
    as passed in the parameter

    '''
    conn = sqlite3.connect("practice.db")
    cur = conn.cursor()
    # delete column values from the table where item value=parameter
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()



def update(quantity, price, item):
    '''
    The method updates the rows from the database where item column has a particular value
    as passed in the parameter

    '''
    conn = sqlite3.connect("practice.db")
    cur = conn.cursor()
    # delete column values from the table where item value=parameter
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price,item))
    conn.commit()
    conn.close()


# create a table
create_table()

# insert some values
insert("Coffee", 2, 3)
insert("Coffee", 2, 3)
insert("Tea", 1, 2.5)
insert("Cookies", 4, 5)
# view the table values
print("view after inserting values: ",view())

# delete an entry
delete("Coffee")
# view the table values again
print("view after deleting rows with 'coffee' as item values: ",view())


# update an entry
update(3, 7, "Cookies")
# view the table values again
print("view after updating 'cookies' rows: ", view())



