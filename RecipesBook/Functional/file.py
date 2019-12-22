import csv

from constraints import  FILE_FOLDER


class File:
    def __init__(self, file_name, file_extension="csv"):
        self.file_name = file_name
        self.extension = file_extension

    def open_file(self):
        with open(f"{FILE_FOLDER}{self.file_name}.{self.file_extension}") as f:
            return list(csv.DictReader(f))

    def write(self, delishes_list):
        with open(f"data/{self.file_name}.{self.file_extension}", "w") as f:
            fieldnames = list(delishes_list[0].keys())
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(delishes_list)


def get_delishes_list(file_name, file_extension="csv"):
    file_manager = File(file_name=file_name, file_extension=file_extension)
    delishes_list = file_manager.read()
    return delishes_list