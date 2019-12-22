from Recipe import Recipe


def create_recipes(title, cuisine, first_prepare, total_kal, for_how_much_person, main_ingridient):
    try:
        new_recipe = Recipe(
            title=title,
            cuisine=cuisine,
            first_prepare=first_prepare,
            total_kal=total_kal,
            for_how_much_person=for_how_much_person,
            main_ingridient=main_ingridient
        )
    except ValueError:
        new_recipe = None
        pass

    return new_recipe