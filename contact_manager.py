import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")

def update_contact(contacts):
    name = input("Enter contact name to update: ")
    for contact in contacts:
        if contact["name"] == name:
            contact["phone"] = input("Enter updated phone number: ")
            contact["email"] = input("Enter updated email: ")
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter contact name to delete: ")
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")



def view_contacts(contacts):
    for contact in contacts:
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print()

if __name__ == "__main__":
    contacts = load_contacts()
    while True:
        print("1. Add contact")
        print("2. View contacts")
        print("3. Update contact")
        print("4. Delete contact")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")