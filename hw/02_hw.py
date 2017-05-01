import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    cars = [
        ('Ford', 'f1', 12),
        ('Ford', 'f2', 2),
        ('Ford', 'f3', 15),
        ('Honda', 'h1', 4),
        ('Honda', 'h2', 13),
    ]

    c.executemany(
        'INSERT INTO inventory(Make, Model, Quantity) values (?, ?, ?)',
        cars,
    )
