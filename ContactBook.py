contacts = {}

while True:
    print("=" * 20)
    print(" [1] Add Contact")
    print(" [2] View Contacts")
    print(" [3] Search Contacts")
    print(" [4] Update Contact")
    print(" [5] Delete Contact")
    print(" [6] Quit")
    print("=" * 20)

    try:
        choice = int(input("Choice: "))
    except ValueError:
        print("Invalid Input, Please input a correct number!")
        continue

    if choice == 1:
        contact = str(input("Enter name and phone number, example(name phone_number): "))
        pairs = contact.split()
        for i in range(0, len(pairs), 2):
            key = pairs[i]
            value = pairs[i + 1]
            contacts[key] = value

    elif choice == 2:
        if not contacts:
            print("No contacts yet!")
        else:
            for i, contact in enumerate(contacts, start=1):
                    print(f"{i}. {contact}: {contacts[contact]}")

    elif choice == 3:
        name = input("Enter the contact name: ")
        if not contacts:
            print("No contacts yet!")
        else:
            if name in contacts:
                for i, contact in enumerate(contacts, start=1):
                    print(f"{contact}: {contacts[contact]}")
            else:
                print("Contact not found!")


    elif choice == 4:
        name = input("Enter the contact name: ")
        if not contacts:
            print("No contacts yet!")
        else:
            if name in contacts:
                contact = str(input("Enter the new phone number: "))
                updateContact = {name: contact}
                contacts.update(updateContact)
                for i, contact in enumerate(contacts, start=1):
                    print(f"{contact}: {contacts[contact]}")
            else:
                print("Contact not found!")
    elif choice == 5:
        name = input("Enter the contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Deleted contact: {name}")
        else:
            print("Contact not found!")

    elif choice == 6:
        break

    else:
        print("Can't find that option, please input a correct number(1 - 6)!")