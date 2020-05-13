


class Store:

    def __init__(self, name, departments):
        self.name = name
        self.departments = departments
    def __str__(self):
        output = ""
        output += self.name + "\n"

        for index, department in enumerate(self.departments):
            output += str(index + 1) + ". " + department + "\n"

        output += "4. Exit"
        return output

store = Store("The Dugout", ["Running", "Baseball", "Basketball"])

print(store)