import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='Root@122',database='library_db')
cursor = conn.cursor()


books=[]
class Library:
    
    def add_books(self):
        book_id=int(input("Enter Book ID:"))
        book_name=input("Enter Book Name:")
        author=input("Enter Auther Name:")
        query= 'INSERT INTO books(book_id, book_name, book_status, student_name)VALUES(%s,%s,%s,%s)'
        values=(book_id,book_name,"Available",'None')
        cursor.execute(query, values)
        conn.commit()
        print("Book add Successfully")

        
    def borrow_books(self):
        book_id=int(input("Enter Book ID to borrow:"))
        student_name=input("Enter Student Name:")
        query='UPDATE books SET book_status=%s, student_name=%s WHERE book_id=%s'
        values=('Borrowed', student_name, book_id)
        cursor.execute(query,values)
        conn.commit()
        print('Borrowed book sucessfully')
                    
    def display_books(self):
        query="SELECT * FROM books"
        cursor.execute(query)
        
        for row in cursor.fetchall():
            print(f"Book ID:{row[0]} |Book Name: {row[1]} |Status: {row[2]} |Student:{row[3]}")
                    
    def return_books(self):
        book_id=int(input("Enter Book ID to return:"))
        query= "UPDATE books SET book_status=%s, student_name=%s WHERE book_id=%s"
        values=("Available",'None',book_id)
        cursor.execute(query, values)
        conn.commit()
        print('Book return sucessfully')

                    
def main():
    lib=Library()
    while True:
        print("=== Library Management System ===")
        print('1. Add Books')
        print('2. Display Books')
        print('3. Borrow Books')
        print('4. Return Books')
        print('5. Exit')
        choice=int(input("Enter your Choice:"))
        if choice==1:
            lib.add_books()
        elif choice==2:
            lib.display_books()
        elif choice==3:
            lib.borrow_books()
        elif choice==4:
            lib.return_books()
        elif choice==5:
            print('Thank you !')
            break
            
        else:
            print('invalid choice')
            
main()
