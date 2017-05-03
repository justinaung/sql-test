import sqlite3
from contextlib import suppress
from random import randint

with sqlite3.connect('newnum.db') as connection:
    c = connection.cursor()

    c.execute('DROP TABLE if exists random_numbers')
    c.execute('CREATE TABLE random_numbers (number int)')

    random_ints = [(randint(0, 100),) for i in range(0, 100)]

    c.executemany(
        'INSERT INTO random_numbers VALUES (?)',
        random_ints
    )
