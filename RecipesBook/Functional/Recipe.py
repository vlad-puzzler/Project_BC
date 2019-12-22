class Recipe:
    def __init__(
            self,
            title,
            cuisine,
            first_prepare,
            total_kal,
            for_how_much_person,
            main_ingridient,
    ):
        self.main_ingridient = main_ingridient
        self.title = title
        self.cuisine = cuisine
        self.first_prepare = first_prepare
        self.total_kal = total_kal
        self.for_how_much_person = for_how_much_person
        self.main_ingridient = main_ingridient

    def check_title(self, title):
        if len(self.title) < 2:
            raise ValueError(f'Title can not be less 2 words!')
        return title

    def search(self, title, cuisine, for_how_much_person):
        pass

    def to_dict(self):
        return {
            "title": self.title,
            "cuisine": self.cuisine,
            "first_prepare": self.first_prepare,
            "total_kal": self.total_kal,
            "for_how_much_person": self.for_how_much_person,
            "main_ingridient": self.main_ingridient
        }