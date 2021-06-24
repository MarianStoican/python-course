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
    @staticmethod
    def speak():
        print("Ham ham")

    def __str__(self):
        return 'dog: %s, age: %s' % (self.name, self.age)


class Person(Animal):
    id = 1

    def __init__(self, name, age):
        super().__init__(age)
        self.set_name(name)
        self.friends = set()
        self.tag = Person.id
        Person.id += 1

    def get_friends(self):
        return self.friends

    def add_friend(self, friend):
        if friend:
            self.friends.add(friend)

    def __str__(self):
        return 'person: %s, age: %s, tag: %s' % (self.name, self.age, self.tag)


dog = Dog(3)
dog.set_name("boby")
print(dog)

dog.speak()

print('-----------------')
ion = Person('Ion', 43)
maria = Person('Maria', 31)

print(ion)
print(maria)
print(Person.id)
print('-----------------')
print(maria.get_friends())
maria.add_friend('ion')
print(maria.get_friends())
maria.add_friend('george')
maria.add_friend('george')
print(maria.get_friends())

