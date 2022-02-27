import sqlite3

#creating book database 
book_conn = sqlite3.connect('books.db')

#connecting to book database
book_csr=book_conn.cursor()

#creating table in book database
book_csr.execute("""CREATE TABLE book (
                book_no text,
                title text,
                author text,
                language text,
                original_text text,
                isbn text,
                awards text,
                value integer
                )""")

#commiting the changes
book_conn.commit()

#closing the connection
book_conn.close()
