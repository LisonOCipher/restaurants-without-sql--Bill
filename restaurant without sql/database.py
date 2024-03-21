import sqlite3

def create_tables():
    connection = sqlite3.connect('restaurant_reviews.db')
    cursor = connection.cursor()

    # Create restaurants table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price INTEGER
        )
    ''')

    # Create customers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT
        )
    ''')

    connection.commit()
    connection.close()

def insert_restaurant(name, price):
    connection = sqlite3.connect('restaurant_reviews.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO restaurants (name, price) VALUES (?, ?)
    ''', (name, price))
    
    connection.commit()
    connection.close()

def insert_customer(first_name, last_name):
    connection = sqlite3.connect('restaurant_reviews.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO customers (first_name, last_name) VALUES (?, ?)
    ''', (first_name, last_name))
    
    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_tables()

    # Insert sample data
    insert_restaurant("Hot Eats", 25)
    insert_restaurant("Treetops Hotel", 30)
    insert_restaurant("Views Hotel", 20)
    insert_restaurant("Cape Hotel", 35)
    insert_restaurant("Big Man Hotel", 40)

    insert_customer("Runner", "Rade")
    insert_customer("Kingsly", "Jas")
    insert_customer("Jaseh", "Onfroy")
    insert_customer("Huey", "Freeman")
    insert_customer("Peter", "Griffen")
