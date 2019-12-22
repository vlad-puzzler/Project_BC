from operate_recipes import create_recipes
from file import get_delishes_list


def main():
    file_name = "delishes"
    delishes_list = get_delishes_list(file_name, file_extension="csv")
    # contact_list.sort(key=lambda contact: (contact["first_name"], contact["second_name"]))
    # contact_list = sorted(contact_list, key=lambda contact: contact["first_name"], reverse=True)
    new_recipe = create_recipes()
    # file_manager.write(contact_list=[new_contact.to_dict() for x in range(3)])


main()
