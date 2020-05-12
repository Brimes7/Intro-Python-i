


class Store:

    def __init__(self, name, departments):
        self.name = name
        self.departments = departments
    def __str__(self):
        print(f'Store name is {self.name}')

store = Store("The Dugout", ["Running", "Baseball", "Basketball"])

print(store)