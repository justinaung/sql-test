import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    c.execute(
        """
        SELECT DISTINCT inventory.make, inventory.model, inventory.quantity, orders.order_date
        FROM inventory
        INNER JOIN orders
        ON inventory.model = orders.model
        ORDER by orders.order_date DESC
        """
    )

    rows = c.fetchall()
    print(f'{len(rows)} records listed:')
    for row in rows:
        print(f'Make: {row[0]} Model: {row[1]}')
        print(f'Quantity: {row[2]}')
        print(f'Order date: {row[3]}')
        print('*' * 10)
