#BOOKSTORE APPLICATION

""" 

Reference idea credit to Youtuber Bek Brace with Video title 'Build a CLI Application in Python[BookStore Application]'
19/9/2024 by Hakkun

"""

def main():
    try:
        booklist = [] #Blank list to be appended
        INfile = open("Booklists.txt", "r")
        line = INfile.readline()
        while line:
            booklist.append(line.rstrip("\n").split(","))
            line = INfile.readline()
        INfile.close()
    except FileNotFoundError: #If txt file is not there(accidentaly deleted)
        print("The <booklist.txt> file is not FOUND")
        print("Starting new booklists...")
        booklist = [] # reinitialize the list

    choice = 0 #initialize starting
    while choice != 4:
        print("1)Add a book\n2)Search your book\n3)Display all books\n4)Close")
        choice = int(input("Choose which number: "))
        #Making Choice
        if choice == 1:
            print("Adding a book...")
            nBook = input("Name of book: ")
            nAuthor = input("Author Name: ")
            nPages = input("Number of pages: ")
            booklist.append([nBook, nAuthor, nPages])
            print("Book added to list")
            outfile = open("Booklists.txt", "w")
            for book in booklist: #saving to external file TXT
                outfile.write(",".join(book) + "\n")
            outfile.close()
        
        elif choice == 2:
            keyword = input("Input the keyword(Title, Author): ")
            for book in booklist:
                if keyword in book:
                    print(str(book) + " is in the list")
        
        elif choice == 3:
            print("Displaying all books...")
            print(booklist) #I don't quite get it the used of range(len(booklist)) print booklist[i] by the youtuber which print the same result if I just do this

        elif choice == 4:
            print("Closing the application...")
    print("Exit the app")

if __name__ == "__main__":
    main()