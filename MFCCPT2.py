l = {}
def a(t, a):
    l[t] = a
    print("Book added successfully.")
def r(t):
    if t in l:
        del l[t]
        print("Book removed successfully.")
    else:
        print("Book not found.")
def u(t, nt, na):
    if t in l:
        del l[t]
        l[nt] = na
        print("Book updated successfully.")
    else:
        print("Book not found.")
def d():
    if l:
        print("Books in the library:")
        for t, a in l.items():
            print("Title:", t, ", Author:", a)
    else:
        print("No books in the library.")
while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Update Book")
    print("4. Display Books")
    print("5. Exit")

    c = input("Enter your choice: ")

    if c == '1':
        t = input("Enter book title: ")
        au = input("Enter book author: ")
        a(t, au)
    elif c == '2':
        t = input("Enter book title to remove: ")
        r(t)
    elif c == '3':
        t = input("Enter book title to update: ")
        nt = input("Enter new title: ")
        na = input("Enter new author: ")
        u(t, nt, na)
    elif c == '4':
        d()
    elif c == '5':
        print("Exit")
        break
    else:
        print("Invalid choice. Please try again.")
