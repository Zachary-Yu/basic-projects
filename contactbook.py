import time

contact_book = {}

def add_contacts():
    name = input("Enter the name of the person you would like to add: ").upper().strip()
    while not name.isalpha():
        print("Please enter a valid name.")
        name = input("Enter the name of the person you would like to add: ").upper().strip()
    
    number = input("Enter the number of the person you would like to add: ").strip()
    while not number.isdigit():
        print("Please enter a valid number.")
        number = input("Enter the number of the person you would like to add: ").strip()
        
    contact_book[name] = number
    print(f"{name}'s phone number ({number}) has successfully been added.")
    print("Redirecting to menu...")
    time.sleep(2.5)
    menu()

    
    
def view_contacts():
     if not contact_book:
        print("The contact book is empty.")
        print("Redirecting to menu...")
        time.sleep(2.5)
        menu()
     else:
        for name in contact_book:
            print(f"{name}'s phone number is: {contact_book[name]}")
            
        time.sleep(2.5)
        print("Redirecting to menu...")
        menu()
    
def delete_contacts():
    if not contact_book:
        print("The contact book is empty.")
        print("Redirecting to menu...")
        time.sleep(2.5)
        menu()
    else:  
        print("Ensure the name inputted is one of the following: ")
        print("----------------------------------------")
        for name in contact_book:
                print(name)
        print("----------------------------------------")
        time.sleep(2.5)
        
        
        name_to_delete = input("What name would you like to delete? ").strip().upper()
        
        del contact_book[name_to_delete]
        print(f"{name_to_delete} has successfully been deleted.")
        print("Redirecting to menu...")
        time.sleep(2.5)
        menu()

def menu():
    print("----------------------------------------")
    print("             Contact Book")
    print("----------------------------------------")
    time.sleep(1)
    print("Choose the number of your choice:")
    print("1. Add contact/s")
    print("2. View contact/s")
    print("3. Delete contact/s")
    print("4. Exit")
    print("----------------------------------------")
    choice = input("").strip()
    
    if choice == "1":
        add_contacts()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        delete_contacts()
    elif choice == "4":
        print("Exiting the program...")
        time.sleep(0.5)
        exit()
    
menu()