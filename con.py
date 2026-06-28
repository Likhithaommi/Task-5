
# Contact Book Management System

contacts = {}

def add_contact():
    name = input("Enter Name: ").strip()

    if name in contacts:
        print("Contact already exists!")
        return

    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }

    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\n------ CONTACT LIST ------")
    for name, details in contacts.items():
        print(f"\nName    : {name}")
        print(f"Phone   : {details['Phone']}")
        print(f"Email   : {details['Email']}")
        print(f"Address : {details['Address']}")

def search_contact():
    name = input("Enter Name to Search: ").strip()

    if name in contacts:
        details = contacts[name]
        print("\nContact Found")
        print("Name    :", name)
        print("Phone   :", details["Phone"])
        print("Email   :", details["Email"])
        print("Address :", details["Address"])
    else:
        print("Contact not found!")

def update_contact():
    name = input("Enter Name to Update: ").strip()

    if name in contacts:
        print("Leave blank if you don't want to change.")

        phone = input("New Phone: ")
        email = input("New Email: ")
        address = input("New Address: ")

        if phone:
            contacts[name]["Phone"] = phone

        if email:
            contacts[name]["Email"] = email

        if address:
            contacts[name]["Address"] = address

        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter Name to Delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

while True:

    print("\n" + "=" * 50)
    print("      CONTACT BOOK MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("\nThank you for using Contact Book!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")