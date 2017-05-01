import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    c.execute(
        'UPDATE inventory SET Quantity = ? WHERE Make = ?',
        (12, 'Honda'),
    )

    print('\nNew Data:\n')

    c.execute('SELECT * from inventory')

    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1], r[2])
