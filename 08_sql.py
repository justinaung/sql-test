# JOINing data fro mmultiple tables

import sqlite3

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()

    c.execute("""
        SELECT DISTINCT population.city, population.population, regions.region
        FROM population, regions
        WHERE population.city = regions.city
        ORDER by population.city ASC
    """)

    rows = c.fetchall()

    for r in rows:
        report = [
            f'City: {r[0]}',
            f'Population: {str(r[1])}',
            f'Region: {r[2]}'
        ]
        print('\n'.join(report))
        print('*'*10)
