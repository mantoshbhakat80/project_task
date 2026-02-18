contact = {}


def display_contact():
    print("Name\t\tphone number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))


while True:
    choice = int (input("1. Add Contacts\n 2. View Contacts\n 3.Display Contacts\n 4.Edit contact\n 5.Delete contact\n 6.Exit\n " \
    "Enter your choice: "))

    if choice == 1:
        name = input("Enter the contact name:")
        phone = input("Enter the contact phone number:")
        contact[name] = phone
        print("Contact added successfully.")

    elif choice == 2:
        search_name =input("Enter the contact name to search:")
        if search_name in contact:
            print(f"contact name: {search_name}, phone number: {contact[search_name]}")
        else:
            print("contact not found,please enter a vaild name.")

    elif choice == 3:
        if not contact:
            print("Empty Contact Book.")
        else:
            display_contact()


    elif choice == 4:
        edit_contact = input("Enter the contact to be edited:")
        if edit_contact in contact:
            phone = input("Enter mobile number to be updated:")
            contact[edit_contact] = phone
            print("contact updated successfully.")
            display_contact()
        else:
            print("contact not found,please enter a vaild name.")

    elif choice == 5:
        delete_contact = input("Enter the contact to be deleted :")
        if delete_contact in contact:
            confirm =input("Do you really want to delete this contact y/n?")
            if confirm == "y" or confirm == "Y":
                contact.pop(delete_contact)
            display_contact()
        else:
            print("contact not found in the contact book,please recheck the name and try again.")


    else:
        break