#BOOKSTORE APPLICATION

""" 

Reference idea credit to Youtuber Bek Brace with Video title 'Build a CLI Application in Python[BookStore Application]'
19/9/2024 by Hakkun

"""

booklist = []

def main():
    choice = 0
    while choice != 4:
        print("1)Add a book\n2)Search your book\n3)Display all books\n4)Close")
        choice = int(input("Choose which number: "))
        if choice == 1:
            print("Adding a book...")
            nBook = input("Name of book: ")
            nAuthor = input("Author Name: ")
            nPages = input("Number of pages: ")
            booklist.append([nBook, nAuthor, nPages])
            print("Book added to list")
        
        elif choice == 2:
            if len(booklist) == 0:
                print("No book in the list yet...\nPlease add a book first")
            for book in booklist:
                keyword = input("Input the keyword(Title, Author): ")
                if keyword in book:
                    print(str(book) + " is in the list")
        
        elif choice == 3:
            print(booklist)
        elif choice == 4:
            print("Closing the application...")
    print("Exit the app")

if __name__ == "__main__":
    main()