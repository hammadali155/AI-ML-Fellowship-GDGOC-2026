import os
import json

CONTACTS_FILE = "contacts.json"


def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return {}
    
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error reading contacts file. Starting fresh.")
        return {}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {}


def save_contacts(contacts):
    try:
        with open(CONTACTS_FILE, 'w') as file:
            json.dump(contacts, file, indent=4)
        print("Contacts saved successfully!")
    except Exception as e:
        print(f"Error saving contacts: {e}")


def add_contact(name, phone, email=""):
    contacts = load_contacts()
    
    if name in contacts:
        print(f"⚠ Contact '{name}' already exists. Use update instead.")
        return
    
    contacts[name] = {
        "phone": phone,
        "email": email
    }
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")


def update_contact(name, phone=None, email=None):
    contacts = load_contacts()
    
    if name not in contacts:
        print(f"Contact '{name}' not found!")
        return
    
    if phone:
        contacts[name]["phone"] = phone
    if email is not None:
        contacts[name]["email"] = email
    
    save_contacts(contacts)
    print(f"Contact '{name}' updated successfully!")


def delete_contact(name):
    contacts = load_contacts()
    
    if name not in contacts:
        print(f"Contact '{name}' not found!")
        return
    
    del contacts[name]
    save_contacts(contacts)
    print(f"Contact '{name}' deleted successfully!")


def view_contacts():
    contacts = load_contacts()
    
    if not contacts:
        print("No contacts found!")
        return
    
    print("\n" + "="*50)
    print(f"{'Name':<20} {'Phone':<15} {'Email':<20}")
    print("="*50)
    
    for name, info in contacts.items():
        print(f"{name:<20} {info['phone']:<15} {info.get('email', 'N/A'):<20}")
    
    print("="*50)
    print(f"Total contacts: {len(contacts)}\n")


def search_contact(name):
    contacts = load_contacts()
    
    if name in contacts:
        info = contacts[name]
        print(f"\nContact Found:")
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info.get('email', 'N/A')}\n")
    else:
        print(f"Contact '{name}' not found!")


def main():
    while True:
        print("\n" + "="*50)
        print("CONTACT MANAGER")
        print("="*50)
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            email = input("Enter email (optional): ").strip()
            add_contact(name, phone, email)
        
        elif choice == "2":
            view_contacts()
        
        elif choice == "3":
            name = input("Enter name to search: ").strip()
            search_contact(name)
        
        elif choice == "4":
            name = input("Enter name to update: ").strip()
            phone = input("Enter new phone (press Enter to skip): ").strip()
            email = input("Enter new email (press Enter to skip): ").strip()
            update_contact(name, phone if phone else None, email if email else None)
        
        elif choice == "5":
            name = input("Enter name to delete: ").strip()
            confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").strip().lower()
            if confirm == 'y':
                delete_contact(name)
        
        elif choice == "6":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
