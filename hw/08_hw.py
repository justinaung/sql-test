import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    c.execute(
        'SELECT * FROM inventory'
    )

    rows = c.fetchall()

    for row in rows:
        print(f'Make: {row[0]} Model: {row[1]} Quantity: {row[2]}')

        c.execute(
            'SELECT count(order_date) FROM orders WHERE make=? and model=?',
            row[:2]
        )
        order_count = c.fetchone()[0]

        print(f'Orders: {order_count}')
