import sqlite3

with sqlite3.connect('newnum.db') as connection:
    c = connection.cursor()

    while True:
        try:
            num = int(input(
                'Enter the number to perform: (1)AVG, (2)MAX, (3)MIN, (4)SUM:\n'
            ).strip())

            if num == 5:
                print('Exited')
                break

            operation = {1: 'avg', 2: 'max', 3: 'min', 4: 'sum'}[num]
            c.execute(
                f'SELECT {operation}(number) from random_numbers'
            )

            result = c.fetchone()[0]
            print(f'Result : {result}')

        except (ValueError, KeyError):
            print('Please enter a number from 1 to 5.')
            continue
