class animal():
    happy = "nothing"
    def feed(self):
        print("Full")
    def clean(self):
        print("Ok")
    def pet(self):
        a = self.__class__.__name__
        print("{} said: {}".format(a, self.happy))

class bird(animal):
    happy = "sing"
    def lay_eggs(self):
        print("You have an egg")

class duck(bird, animal):
    def __init__(self, name):
        self.name = name
    happy = "Kwak"
    def save_money(self):
        if self.name == "Donald":
            print("More money!")
class chicken(bird, animal):
    happy = "Kuku"

class Gusi(bird, animal):
    happy = "Gagaga"

class nobird(animal):
    happy = "dance"
    def watch_birds(self):
        a = self.__class__.__name__
        print("{} said: Woah!".format(a))

class cow(nobird, animal):
    happy = "Moo"

class goat(nobird, animal):
    happy = "Mee"

class sheep(nobird, animal):
    happy = "Beeeee"

class pig(nobird, animal):
    happy = "Hru"
    def life_purpose(self):
        print("I will be a bacon, when I grow up!")

a = duck("Donald")
a.save_money()
