c=[]
while True:
    print("""
====================
LIBRARY CATALOG
          
1. Add Book
2. View All Books
3. Search Book
4. Edit Book
5. Delete Book
6. Exit
====================\n""")
    #c_b=cohice_book
    c_b=input(" Choose number an option: ").lower()
    if c_b== "1" or c_b== "add book":
        n=input("Name Tile: ")
        p=input("Name Author: ")
        e=input("Name category: ")
        c.append([n,p,e])
        print("✅ Book added successfully!")
    elif c_b== "2" or c_b== "view all book":
        print("\n--- All Books ---")
        print(f"total {len(c)} Books.")
        print(f"{'No.':<5}{'Name Tile':<20}{'Name Author':<15}{'Name category':<25}")
        print("-" * 65)
        for i, book in enumerate (c, start=1):
            print(f"{i:<5}{book[0]:<20}{book[1]:<15}{book[2]:<25}")
    
    elif c_b== "3" or c_b== "search book":
        s=input("Enter name to search a Book :")
        for c_s in c:
            if c_s[0].lower() == s.lower():
                print(f"Name Tile : {c_s[0]}")
                print(f"Name Author: {c_s[1]}")
                print(f"Name category: {c_s[2]}")
                break
        else:
            print("book not found!")
        
    elif c_b== "4" or c_b=="edit book":
        e_c=input("Enter Name Tile to edit :")
        for c_e in c:
            if c_e[0].lower() == e_c.lower():
                n_e=input("Name Tile Edit: ")
                p_e=input("Name Author Edit: ")
                e_e=input("Email Edit: ")
                c_e[0] = n_e
                c_e[1] = p_e
                c_e[2] = e_e
                print("✅ Edited Book added successfully!")
                found = True
                break
        if not found:
            print("book not found!")
    elif c_b=="5" or c_b=="delete book":
        d_c=input("Enter Name Tile to delete :")
        for c_d in c:
            if c_d[0].lower() == d_c.lower():
                print(c_d[0])
                print(c_d[1])
                print(c_d[2])
                d=input(" enter to delete Book (yes/no):")
                found = True
                if d =="yes":
                    c.remove(c_d)
                    print("✅ Delete Book added successfully!")
                else:
                    print("✅ don't Delete Book added successfully!")
        if not found:
            print("\n!not faound name in data!")
    elif c_b=="6" or c_b=="exit":
        print("Thank you, and we wish you a nice day.")
        break
    else:
        print("not faound in data, please Try again")
        
