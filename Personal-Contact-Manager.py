contacts = {}


def add_contact():
    name = input("Enter name: ").title()
    phone_number = input("Phone number: ")
    email_address = input("Email address: ").capitalize()
    city = input("City: ").capitalize()

    contacts[name] = {"phone": phone_number,
                      "email": email_address, "city": city}

    return "\nContact added."


def view_contact():
    if len(contacts) == 0:
        print("No contacts yet.")

    else:
        print("\nCONTACTS")
        print("--------------------------------------------------------------------------------------------------------")
        print(
            f"{"Serial":<8} | {"Name":<25} | {"Phone Number":<20} | {"Email":<30} | {"City"}")
        print("--------------------------------------------------------------------------------------------------------")

        for i, name in enumerate(contacts, start=1):
            print(
                f"{i:<8} | {name:<25} | {contacts[name]['phone']:<20} | {contacts[name]['email']:<30} | {contacts[name]['city']}")


def contact_information():

    for name in contacts:
        print(name)

    try:
        search_name = input("\nSearch contact name for informations: ").title()

        contact = contacts[search_name]

        output = f"\n{"Name":<7} {search_name}\n"

        for information in contact:
            output += f"{information:<7} {contact[information]}\n"

        return output

    except KeyError:
        return "No contact found."


def remove_contact():
    view_contact()

    try:
        num = int(input("\nEnter the contact serial number to remove: "))

        remove_name = list(contacts.keys())[num - 1]

        contacts.pop(remove_name)

        return f"\n{remove_name} has removed."

    except ValueError:

        return "\nPlease enter the contact serial number to remove. "

    except IndexError:

        return "\nNo contact found with this serial number."


print("""
1 Add contact
2 View contact
3 Get contact's information
4 Remove contact
5 Exit
""")
while True:
    choice = input("\nChoose an option: ")

    if choice == "1":
        print(add_contact())

    elif choice == "2":
        view_contact()

    elif choice == "3":
        print(contact_information())

    elif choice == "4":
        print(remove_contact())

    elif choice == "5":
        break

    else:
        print("Choose between 1-5")
