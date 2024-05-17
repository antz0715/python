def display_menu():
    print("Contact Book Menu:")
    print("1. View contacts")
    print("2. Add contact")
    print("3. Delete contact")
    print("4. Quit")

def view_contacts(contacts):
    if not contacts:
        print("No contacts in the book.")
    else:
        for name, number in contacts.items():
            print(f"Name: {name}, Number: {number}")

def add_contact(contacts):
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contacts[name] = number
    print("Contact added.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def contact_book():
    contacts = {}
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

contact_book()
