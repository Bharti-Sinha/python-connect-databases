# python-connect-databases

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![PostgreSQL 10.18](https://img.shields.io/badge/PostgreSQL-10.18-blue.svg)](https://www.postgresql.org/download/)

## Table Of Contents

1. [Overview](#overview)
2. [SQLite](#sqlite)
3. [PostgreSQL](#postgresql)

# **Overview**

# Introduction on how to connect to databases using Python

- Audience: _Beginner_

- Language: _Python_

This repository is intends to help beginners to connect to databases such as SQLite and PostgreSQL using python. If you want to build a small scale applications you can use sqlite database which is an embedded database and can run within your application.

The PostgreSQL on the other hand deploys Client-Server Model and needs to set up a server.

# 1. SQLite <a name="sqlite"></a>

- `sqlite_connection.py` file explains the first 5 steps to interact with a database.

- `sqlite.py` file holds basic methods to perform following actions:

1. Create connection to a sqlite database
2. Add/Insert values into the table
3. Update values of the table
4. Delete values from the table
5. View the table values

# 2. PostgreSQL <a name="postgresql"></a>

- `postgresql.py` file holds basic methods to perform following actions on a postgresql database:

1. Create connection to a sqlite database
2. Add/Insert values into the table
3. Update values of the table
4. Delete values from the table
5. View the table values
