# Simple contact book using a dictionary

contacts = {}

while True:
    print("\n1. Add contact")
    print("2. View contacts")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        print("Contact added!")

    elif choice == "2":
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
