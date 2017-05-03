import sqlite3
from random import randint

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    # c.execute(
    #     'CREATE TABLE orders (make TEXT, model TEXT, order_date DATE)'
    # )

    c.execute(
        'SELECT DISTINCT Make, Model FROM inventory'
    )
    rows = c.fetchall()

    orders = list()
    for row in rows:
        for i in range(0, 3):
            year = randint(2000, 2017)
            month = str(randint(1, 12)).zfill(2)
            day = str(randint(1,28)).zfill(2)
            orders.append(
                (row[0], row[1], f'{year}-{month}-{day}')
            )

    c.executemany(
        'INSERT INTO orders (make, model, order_date) values (?, ?, ?)',
        orders
    )
