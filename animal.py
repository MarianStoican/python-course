class Animal:
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age

    def set_name(self, new_name=None):
        self.name = new_name

    def __str__(self):
        return 'animal: %s, age: %s' % (self.name, self.age)


class Dog(Animal):
    def speak(self):
        print("Ham ham")

    def __str__(self):
        return 'dog: %s, age: %s' % (self.name, self.age)


dog = Dog(3)
dog.set_name("boby")
print(dog)

dog.speak()


