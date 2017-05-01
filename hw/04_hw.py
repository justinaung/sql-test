import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    for row in c.execute('SELECT * FROM inventory WHERE Make="Ford"'):
        print(row)
