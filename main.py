class Animal:
    happy = "nothing"

    def feed(self):
        print("Full")

    def clean(self):
        print("Ok")

    def pet(self):
        x = self.__class__.__name__
        print("{} said: {}".format(x, self.happy))


class Bird(Animal):
    happy = "sing"

    def lay_eggs(self):
        print("You have an egg")


class Duck(Bird, Animal):

    def __init__(self, name):
        self.name = name
    happy = "Kwak"

    def save_money(self):
        if self.name == "Donald":
            print("More money!")


class Chicken(Bird, animal):
    happy = "Kuku"


class Gusi(Bird, Animal):
    happy = "Gagaga"


class NoBird(Animal):
    happy = "dance"

    def watch_birds(self):
        a = self.__class__.__name__
        print("{} said: Woah!".format(a))


class Cow(NoBird, Animal):
    happy = "Moo"


class Goat(NoBird, Animal):
    happy = "Mee"


class Sheep(NoBird, Animal):
    happy = "Beeeee"


class Pig(NoBird, Animal):
    happy = "Hru"

    def life_purpose(self):
        print("I will be a bacon, when I grow up!")

MyClass = duck("Donald")
MyClass.save_money()
