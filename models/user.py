class User:
    def __init__(self, name):
        self.name = name

    def get_age(self):
        return input('Your age: ')

    def get_last_name(self):
        return input('Your last name: ')

    def get_dog_name(self):
        return input('Your dog name: ')

    def get_user_data(self):
        last_name = self.get_last_name()
        dog_name = self.get_dog_name()
        return last_name, dog_name
