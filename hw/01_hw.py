import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE inventory
                (Make TEXT, Model TEXT, Quantity Int)
                """)
