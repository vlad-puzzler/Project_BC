import sys
from file import *
from operate_recipes import create_recipes
from Recipe import *

print("Hello User! Please enter your choice: ")
choice = input("Enter 1 - Open all Recipe Book \
               Enter 2 - Open search in Recipe Book \
               Enter 3 - Add new recipe \n")

def main(input_choice):
    file_name = "delishes"
    if int(input_choice) == 1:
        delishes_list = get_delishes_list(file_name, file_extension="csv")
        for dish in delishes_list:
            print(dish)
    if int(input_choice) == 3:
        delishes_list = get_delishes_list(file_name, file_extension="csv")
        print(f"Enter please new recipe below. For end please enter quit: ")
        new_title = input(f"Enter Title please: ")
        if new_title == 'quit':
            quit
        new_cuisine = input(f"Enter Cuisine please: ")
        if new_cuisine == 'quit':
            quit
        new_first_prepare = input(f"Who first prepared it dishes: ")
        if new_first_prepare == 'quit':
            quit
        new_total_kol = input(f"How much Kal in one portion: ")
        if new_total_kol == 'quit':
            quit
        new_persons = input(f"For how person this dishes: ")
        if new_persons == 'quit':
            quit
        new_main_ing = input(f"Please enter main ingridient in dishes: ")
        if new_main_ing == 'quit':
            quit
    recipe = create_recipes(new_title, new_cuisine, new_first_prepare, new_total_kol, new_persons, new_main_ing)
    delishes_list.append(recipe)
    File.write(file_name, delishes_list)

    # contact_list.sort(key=lambda contact: (contact["first_name"], contact["second_name"]))
    # contact_list = sorted(contact_list, key=lambda contact: contact["first_name"], reverse=True)
    # new_recipe = create_recipes()
    # file_manager.write(contact_list=[new_contact.to_dict() for x in range(3)])


main(choice)
