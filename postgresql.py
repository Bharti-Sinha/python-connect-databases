'''
author: Bharti Sinha
date: 29th October 2021

# Steps for intial setup
1.
2.
3.
4.

'''

# import library
import psycopg2

def create_table():
    '''
    The method connects to an already existing database
    '''
    conn = psycopg2.connect("dbname='database1', user='postgres', password='postgres123' host='localhost' port='5432'")
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
    conn = psycopg2.connect("dbname='database1', user='postgres', password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    '''
    The method fetches all the rows from the database and prints it as a python list

    '''
    conn = psycopg2.connect("dbname='database1', user='postgres', password='postgres123' host='localhost' port='5432'")
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
    conn = psycopg2.connect("dbname='database1', user='postgres', password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    # delete column values from the table where item value=parameter
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()



def update(quantity, price, item):
    '''
    The method updates the rows from the database where item column has a particular value
    as passed in the parameter

    '''
    conn = psycopg2.connect("dbname='database1', user='postgres', password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    # delete column values from the table where item value=parameter
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()


# create a tabel
create_table()
print(view())


# # insert some values
# insert("Coffee", 2, 3)
# insert("Coffee", 2, 3)
# insert("Tea", 1, 2.5)
# insert("Cookies", 4, 5)
# # view the table values
# print("view after inserting values: ",view())

# # delete an entry
# delete("Coffee")
# # view the table values again
# print("view after deleting rows with 'coffee' as item values: ",view())


# # update an entry
# update(3, 7, "Cookies")
# # view the table values again
# print("view after updating 'cookies' rows: ", view())





