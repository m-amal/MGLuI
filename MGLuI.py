from tkinter import*
from PIL import ImageTk, Image
import sqlite3


root=Tk()
root.title("MGLuI")



#welcome note
welcome_note_label=Label(root, text="Welcome to Mahtma Gandhi Library")
welcome_note_label.grid(row=0, column=1)
#welcome quote
welcome_quote_label=Label(root, text="Be the change you want to see in the world")
welcome_quote_label.grid(row=2, column=1)
#welcome image
mg_image=ImageTk.PhotoImage(Image.open("Image/MG_150.png"))
welcome_image_label=Label(image=mg_image)
welcome_image_label.grid(row=3, column=0, columnspan=3)



#test function
def tmp():
    pass


#function to view book details from database
def view_books_fun():
    
    #connecting to database
    book_conn = sqlite3.connect('books.db')
    book_csr=book_conn.cursor()
    
    #fetching details from database
    book_csr.execute("SELECT *, oid FROM book")
    book_records=book_csr.fetchall()
    #printing details on command prompt
    print(book_records)
    
    #commiting changes
    book_conn.commit()
    #closing connection
    book_conn.close()




#function to open view books window
def view_books_window_fun():
    view_books_window=Toplevel()
    
    #label
    view_books_top_label=Label(view_books_window, text="View books from book database")
    #buuton
    view_books_button=Button(view_books_window, text="View", command=view_books_fun)
    
    #grid layout
    view_books_top_label.grid(row=0, column=0, pady=5)
    view_books_button.grid(row=1, column=0, pady=10)

    

#function to add book details to database
def add_books_fun():

    #connecting to database
    book_conn = sqlite3.connect('books.db')
    book_csr=book_conn.cursor()

    #adding details to database
    book_csr.execute("INSERT INTO book VALUES (:book_no, :title, :author, :language, :original_text, :isbn, :awards, :value)",
    {
        'book_no': add_book_no_box.get(),
        'title': add_title_box.get(),
        'author': add_author_box.get(),
        'language': add_language_box.get(),
        'original_text': add_original_text_box.get(),
        'isbn': add_isbn_box.get(),
        'awards': add_awards_box.get(),
        'value': add_value_box.get()
    })

    #clearing the entry boxes
    add_book_no_box.delete(0, END),
    add_title_box.delete(0, END),
    add_author_box.delete(0, END),
    add_language_box.delete(0, END),
    add_original_text_box.delete(0, END),
    add_isbn_box.delete(0, END),
    add_awards_box.delete(0, END),
    add_value_box.delete(0, END)

    #commiting changes
    book_conn.commit()
    #closing connection
    book_conn.close()


    
#function to open add books window
def add_books_window_fun():
    global add_book_no_box, add_title_box, add_author_box, add_language_box, add_original_text_box, add_isbn_box, add_awards_box, add_value_box

    add_books_window=Toplevel()

    
    #label
    add_books_top_label=Label(add_books_window, text="Add books to book database")
    add_book_no_label=Label(add_books_window, text="Book No")
    add_title_label=Label(add_books_window, text="Title")
    add_author_label=Label(add_books_window, text="Author")
    add_language_label=Label(add_books_window, text="Language")
    add_original_text_label=Label(add_books_window, text="Origanal text")
    add_isbn_label=Label(add_books_window, text="ISBN")
    add_awards_label=Label(add_books_window, text="Awards")
    add_value_label=Label(add_books_window, text="Value")
    
    #entry box
    add_book_no_box=Entry(add_books_window, width=30)
    add_title_box=Entry(add_books_window, width=30)
    add_author_box=Entry(add_books_window, width=30)
    add_language_box=Entry(add_books_window, width=30)
    add_original_text_box=Entry(add_books_window, width=30)
    add_isbn_box=Entry(add_books_window, width=30)
    add_awards_box=Entry(add_books_window, width=30)
    add_value_box=Entry(add_books_window, width=30)
    
    #button to add book details to database
    add_books_button=Button(add_books_window, text="Submit", command=add_books_fun)


    #grid layout
    
    #label
    add_books_top_label.grid(row=0, column=0, columnspan=2, pady=5)
    add_book_no_label.grid(row=1, column=0, pady=1)
    add_title_label.grid(row=2, column=0, pady=1)
    add_author_label.grid(row=3, column=0, pady=1)
    add_language_label.grid(row=4, column=0, pady=1)
    add_original_text_label.grid(row=5, column=0, pady=1)
    add_isbn_label.grid(row=6, column=0, pady=1)
    add_awards_label.grid(row=7, column=0, pady=1)
    add_value_label.grid(row=8, column=0, pady=1)
    
    #entry box
    add_book_no_box.grid(row=1, column=1)
    add_title_box.grid(row=2, column=1)
    add_author_box.grid(row=3, column=1)
    add_language_box.grid(row=4, column=1)
    add_original_text_box.grid(row=5, column=1)
    add_isbn_box.grid(row=6, column=1)
    add_awards_box.grid(row=7, column=1)
    add_value_box.grid(row=8, column=1)
    
    #button
    add_books_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10, ipadx=150)
    


#function to delete book details from database
def delete_books_fun():

    #connecting to database
    book_conn = sqlite3.connect('books.db')
    book_csr=book_conn.cursor()

    #adding details to database
    book_csr.execute("DELETE from book WHERE oid="+delete_book_no_box.get())

    delete_book_no_box.delete(0, END)

    #commiting changes
    book_conn.commit()
    #closing connection
    book_conn.close()    



#function to open delete books window
def delete_books_window_fun():
    global delete_book_no_box
    
    delete_books_window=Toplevel()

    #label
    delete_books_top_label=Label(delete_books_window, text="Delete books from book database")
    delete_book_no_label=Label(delete_books_window, text="Book No")

    #entry box
    delete_book_no_box=Entry(delete_books_window, width=30)

    #button to delete books from database
    delete_books_button=Button(delete_books_window, text="Delete", command=delete_books_fun)


    #grid layout

    #label
    delete_books_top_label.grid(row=0, column=0, columnspan=2, pady=5)
    delete_book_no_label.grid(row=1, column=0, pady=1)

    #entry box
    delete_book_no_box.grid(row=1, column=1)

    #buton
    delete_books_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, ipadx=150)
    

#function to print detais of the searched book from book database
def edit_books_search_fun():
    #connecting to database
    book_conn = sqlite3.connect('books.db')
    book_csr=book_conn.cursor()

    #fetching details from database
    book_records_id=edit_uid_search_box.get()
    book_csr.execute("SELECT * FROM book WHERE oid="+book_records_id)
    book_records=book_csr.fetchall()

    for book_records in book_records:
        edit_book_no_box.insert(0, book_records[0])
        edit_title_box.insert(0, book_records[1])
        edit_author_box.insert(0, book_records[2])
        edit_language_box.insert(0, book_records[3])
        edit_original_text_box.insert(0, book_records[4])
        edit_isbn_box.insert(0, book_records[5])
        edit_awards_box.insert(0, book_records[6])
        edit_value_box.insert(0, book_records[7])

    #commiting changes
    book_conn.commit()
    #closing connection
    book_conn.close()



#function to edit books in book database
def edit_books_fun():
    #connecting to database
    book_conn = sqlite3.connect('books.db')
    book_csr=book_conn.cursor()

    #editing details in database
    book_records_id=edit_uid_search_box.get()
    book_csr.execute("SELECT * FROM book WHERE oid="+book_records_id)
    book_records=book_csr.fetchall()

    book_csr.execute("""UPDATE book SET
            book_no = :bno,
            title = :ttl,
            author = :aut,
            language = :lng,
            original_text = :org,
            isbn = :sbn,
            awards = :awd,
            value = :vlu

            WHERE oid + :oid""",
            {
            'bno': edit_book_no_box.get(),
            'ttl': edit_title_box.get(),
            'aut': edit_author_box.get(),
            'lng': edit_language_box.get(),
            'org': edit_original_text_box.get(),
            'sbn': edit_isbn_box.get(),
            'awd': edit_awards_box.get(),
            'vlu': edit_value_box.get(),
            'oid': book_records_id
            })
    
    #commiting changes
    book_conn.commit()
    #closing connection
    book_conn.close()

    #clear the text boxes
    edit_book_no_box.delete(0, END)
    edit_title_box.delete(0, END)
    edit_author_box.delete(0, END)
    edit_language_box.delete(0, END)
    edit_original_text_box.delete(0, END)
    edit_isbn_box.delete(0, END)
    edit_awards_box.delete(0, END)
    edit_value_box.delete(0, END)


    
#function to open edit books window
def edit_books_window_fun():
    
    global edit_uid_search_box, edit_book_no_box, edit_title_box, edit_author_box, edit_language_box, edit_original_text_box, edit_isbn_box, edit_awards_box, edit_value_box
    
    edit_books_window=Toplevel()

    #label
    edit_books_top_label=Label(edit_books_window, text="Edit books in book database")
    edit_uid_search_label=Label(edit_books_window, text="ID")
    edit_book_no_label=Label(edit_books_window, text="Book No")
    edit_title_label=Label(edit_books_window, text="Title")
    edit_author_label=Label(edit_books_window, text="Author")
    edit_language_label=Label(edit_books_window, text="Language")
    edit_original_text_label=Label(edit_books_window, text="Origanal text")
    edit_isbn_label=Label(edit_books_window, text="ISBN")
    edit_awards_label=Label(edit_books_window, text="Awards")
    edit_value_label=Label(edit_books_window, text="Value")
    
    #entry box
    edit_uid_search_box=Entry(edit_books_window, width=30)
    edit_book_no_box=Entry(edit_books_window, width=30)
    edit_title_box=Entry(edit_books_window, width=30)
    edit_author_box=Entry(edit_books_window, width=30)
    edit_language_box=Entry(edit_books_window, width=30)
    edit_original_text_box=Entry(edit_books_window, width=30)
    edit_isbn_box=Entry(edit_books_window, width=30)
    edit_awards_box=Entry(edit_books_window, width=30)
    edit_value_box=Entry(edit_books_window, width=30)
    
    #button to add book details to database
    edit_uid_search_button=Button(edit_books_window, text="Search", command=edit_books_search_fun)
    edit_books_button=Button(edit_books_window, text="Update", command=edit_books_fun)


    #grid layout
    
    #label
    edit_books_top_label.grid(row=0, column=0, columnspan=2, pady=5)
    edit_uid_search_label.grid(row=1,column=0, pady=1)
    edit_book_no_label.grid(row=3, column=0, pady=1)
    edit_title_label.grid(row=4, column=0, pady=1)
    edit_author_label.grid(row=5, column=0, pady=1)
    edit_language_label.grid(row=6, column=0, pady=1)
    edit_original_text_label.grid(row=7, column=0, pady=1)
    edit_isbn_label.grid(row=8, column=0, pady=1)
    edit_awards_label.grid(row=9, column=0, pady=1)
    edit_value_label.grid(row=10, column=0, pady=1)
    
    #entry box
    edit_uid_search_box.grid(row=1, column=1)
    edit_book_no_box.grid(row=3, column=1)
    edit_title_box.grid(row=4, column=1)
    edit_author_box.grid(row=5, column=1)
    edit_language_box.grid(row=6, column=1)
    edit_original_text_box.grid(row=7, column=1)
    edit_isbn_box.grid(row=8, column=1)
    edit_awards_box.grid(row=9, column=1)
    edit_value_box.grid(row=10, column=1)
    
    #button
    edit_uid_search_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, ipadx=150)
    edit_books_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=150)
    



#menu
main_menu=Menu(root)
root.config(menu=main_menu)


#system sub-menu
system_menu=Menu(main_menu)
main_menu.add_cascade(label="System", menu=system_menu)
system_menu.add_command(label="Quit", command=root.destroy)


#library sub-menu
library_menu=Menu(main_menu)
main_menu.add_cascade(label="Library", menu=library_menu)

#view books in database of books
library_menu.add_command(label="View", command=view_books_window_fun)

#update books in database of books (with options)
update_menu=Menu(library_menu)
library_menu.add_cascade(label="Update", menu=update_menu)
#add option
update_menu.add_command(label="Add", command=add_books_window_fun)
#delete option
update_menu.add_command(label="Delete", command=delete_books_window_fun)
#edit option
update_menu.add_command(label="Edit", command=edit_books_window_fun)


#help sub-menu
help_menu=Menu(main_menu)
main_menu.add_cascade(label="Help", menu=help_menu)
#about
help_menu.add_command(label="About MGLuI", command=tmp)
#license
help_menu.add_command(label="License", command=tmp)



root.mainloop()
