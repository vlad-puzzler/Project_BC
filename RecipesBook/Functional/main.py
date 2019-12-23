from file import *

print("Hello User! Please enter your choice: ")
choice = input("Enter 1 - Open all Recipe Book \
               Enter 2 - Open search in Recipe Book \
               Enter 3 - Add new recipe")

def main(input_choice):
    if int(input_choice) == 1:
        file_name = "delishes"
        delishes_list = get_delishes_list(file_name, file_extension="csv")
        print(delishes_list)

    # contact_list.sort(key=lambda contact: (contact["first_name"], contact["second_name"]))
    # contact_list = sorted(contact_list, key=lambda contact: contact["first_name"], reverse=True)
    # new_recipe = create_recipes()
    # file_manager.write(contact_list=[new_contact.to_dict() for x in range(3)])


main(choice)
