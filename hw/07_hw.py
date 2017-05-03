import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    c.execute(
        'SELECT model from orders'
    )

    rows = c.fetchall()
    for row in rows:
        c.execute(
            'SELECT count(model) from orders WHERE model=?',
            row
        )
        count = c.fetchone()[0]
        print(f'Model : {row[0]} Orders: {count}')
