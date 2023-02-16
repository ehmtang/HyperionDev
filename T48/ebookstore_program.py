import sqlite3
import pandas as pd

db = sqlite3.connect('ebookstore')
cursor = db.cursor()  # Get a cursor object

# Create table if it does not exist
cursor.execute('''  
    CREATE TABLE IF NOT EXISTS Books
    (
        id INTEGER PRIMARY KEY, 
        title TEXT,
        author TEXT,
        qty INTEGER
    );
    ''')
db.commit()

# Inserting books
cursor.execute('''
    INSERT OR IGNORE INTO Books
    (
        id,
        title, 
        author,
        qty
    )
    VALUES
    (
        3001,
        "A Tale of Two Cities",
        "Charles Dickens",
        30
    ),
    (
        3002,
        "Harry Potter and the Philosopher's Stone",
        "J.K. Rowling",
        40
    ),
    (
        3003,
        "The Lion, the Witch, and the Wardrobe",
        "C.S. Lewis",
        25
    ),
    (
        3004,
        "The Lord of the Rings",
        "J.R.R. Tolkien",
        37
    ),
    (
        3005,
        "Alice in Wonderland",
        "Lewis Carroll",
        12
    );
    ''')
db.commit()

# Create class called eBookstore
# That contains the functions of the store
#   1. Enter Book
#   2. Update Book
#   3. Delete Book
#   4. Search Book
#   5. Read all
class eBookstore:

    def __init__(self, id, title, author, qty):
        self.id = id
        self.title = title
        self.author = author
        self.qty = qty

    # Allow user to enter a new book into table
    def enter_book():

        # Prompt user to add new record into books table
        print('\n1. Enter Book')
        
        # Ask for a unique book id,
        # If value exists, prompt user for a new one.
        while True:
            try:
                id = int(input('Enter book id: '))
                
                # Query Books 
                cursor.execute('''SELECT * FROM Books''')
                query = cursor.fetchall()
            
            except:
                print("You've entered an invalid book id.\n")
                continue
            
            # If input_id exists in list of ids (first element of each list in query) 
            if id in [value[0] for value in query]:
                print(f'Book id {id} already exists. Select another id.\n')
                
            else:
                break
            
        title = input('Enter book title: ')
        author = input('Enter book author: ')

        # Ask user for a valid quantity
        while True:
            try:
                qty = int(input('Enter quantity stored: '))
        
            except:
                print("You've entered an invalid quantity.\n")
                continue
            
            if qty < 1:
                print("You've entered an invalid quantity.\n")
            
            else:
                break

        # Inserting book into table
        cursor.execute('''
            INSERT INTO books
            (
                id, 
                title,
                author,
                qty
            )
            VALUES(?,?,?,?);''', (id, title, author, qty))
        db.commit()

        print('Book successfully entered')

    # Update title, author and quantity for specified book id
    def update_book():
        
        # Prompt user to update existing record in books table
        print('\n2. Update Book')
        
        id = int(input('Enter book id to be updated: '))
        title = input('Enter new book title: ')
        author = input('Enter new book author: ')
        qty = int(input('Enter new quantity stored: '))
        
        # Query to update title, author and quantity
        cursor.execute('''
            UPDATE Books 
            SET title = ?, author = ?, qty = ?
            WHERE id = ?;''', (title, author, qty, id))
        db.commit()
        
        print(f'Book id {id} successfully updated')

    # Delete entry from database
    def delete_book():

        # Prompt user to delete existing record in books table
        print('\n3. Delete Book')
        
        id = int(input('Enter book id to be deleted: '))
        
        # Query to delete row by book id
        cursor.execute('''
        DELETE FROM Books
        WHERE id = ? ''', (id,))
        db.commit()

        print(f'Book id {id} successfully deleted')

    # Search book in Books table
    # 1. Book id
    # 2. Book title
    # 3. Book author
    def search_book():
        
        # Prompt user to search for an existing record in books table
        print('\n4. Search Book')

        while True:
            try:
                search_book_menu = int(input('''Enter option to search: 
1. Search by book id
2. Search by book title
3. Search by book author
: '''))
                if search_book_menu == 1:
                    id = int(input('\nEnter book id to be queried: '))
                    print()

                    # Query to search by id
                    cursor.execute('''
                    SELECT * FROM Books
                    WHERE id = ?''', (id,))
                    
                    query = cursor.fetchall()

                    for book in query:
                        print(f"id: {book[0]}")
                        print(f"title: {book[1]}")
                        print(f"author: {book[2]}")
                        print(f"quantity: {book[3]}\n") 

                    break

                elif search_book_menu == 2:
                    title = input('\nEnter book title to be queried: ')
                    print()

                    # Query to search by title
                    cursor.execute('''
                    SELECT * FROM Books
                    WHERE title = ?''', (title,))
                    query = cursor.fetchall()

                    for book in query:
                        print(f"id: {book[0]}")
                        print(f"title: {book[1]}")
                        print(f"author: {book[2]}")
                        print(f"quantity: {book[3]}\n") 

                    break

                elif search_book_menu == 3:
                    author = input('\nEnter book author to be queried: ')
                    print()

                    # Query to search by author
                    cursor.execute('''
                    SELECT * FROM Books
                    WHERE author = ?''', (author,))
                    query = cursor.fetchall()
                    
                    for book in query:
                        print(f"id: {book[0]}")
                        print(f"title: {book[1]}")
                        print(f"author: {book[2]}")
                        print(f"quantity: {book[3]}\n")                
                    
                    break

            except:
                print("\nInvalid option.")
            
            else:
                print("\nInvalid option.")
                continue
    
    # Read all records in Books
    def read_all():
        print('\n5. Read all\n')
        print(pd.read_sql_query("SELECT * from Books", db))

# Start prompt and menu
while True:
    menu = int(input(f'''\nSelect one of the following options below:
1. Enter book
2. Update book
3. Delete book
4. Search book
5. Read all
0. Exit
: '''))

    if menu == 1:
        eBookstore.enter_book()

    elif menu == 2:
        eBookstore.update_book()

    elif menu == 3:
        eBookstore.delete_book()

    elif menu == 4:
        eBookstore.search_book()
    
    elif menu == 5:
        eBookstore.read_all()

    elif menu == 0:
         db.close()
         print("\nClosing connection to database.")
         print("Exitting program.")
         exit()

    else:
        print("\nInput invalid.")