# SQLite functions

import sqlite3

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()

    # create a dictionary of sql queries
    sql = {
        'average': 'SELECT avg(population) FROM population',
        'maximum': 'SELECT max(population) FROM population',
        'minimum': 'SELECT min(population) FROM population',
        'sum': 'SELECT sum(population) FROM population',
        'count': 'SELECT count(city) FROM population',
    }

    # run each sql query item in the dicitonary
    for key, value in sql.items():
        c.execute(value)
        result = c.fetchone()
        print(f'{key}:{result[0]}')
