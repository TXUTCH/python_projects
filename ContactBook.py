import json

def save_contacts(filename="contacts.json"):
    with open(filename, "w") as f:
        json.dump(contacts, f)
    print("Contacts saved!")

def load_contacts(filename="contacts.json"):
    global contacts
    try:
        with open(filename, "r") as f:
            contacts = json.load(f)
        print("Contacts loaded!")
    except FileNotFoundError:
        contacts = {}

load_contacts()

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
        name = input("Enter the contact name: ").lower()
        found = False
        if not contacts:
            print("No contacts yet!")
        else:
            for contact_name, number in contacts.items():
                if contact_name.lower() == name.lower():
                    print(f"{contact_name}: {number}")
                    found = True
            if not found:
                print("Contact not found!")


    elif choice == 4:
        name = input("Enter the contact name: ").lower()
        found = False
        if not contacts:
            print("No contacts yet!")
        else:
            for contact_name, number in contacts.items():
                if contact_name.lower() == name.lower():
                    found = True
                    contact = str(input("Enter the new phone number: "))
                    updateContact = {contact_name: contact}
                    contacts.update(updateContact)
                    print(f"{contact_name}: {contact}")
            if not found:
                print("Contact not found!")
    elif choice == 5:
        name = input("Enter the contact name to delete: ").lower()
        found_key = None
        for contact_name, number in contacts.items():
            if contact_name.lower() == name.lower():
                found_key = contact_name
                break
        if found_key:
            del contacts[found_key]
            print(f"Deleted contact: {found_key}")
        else:
            print("Contact not found!")

    elif choice == 6:
        save_contacts()
        break

    else:
        print("Can't find that option, please input a correct number(1 - 6)!")