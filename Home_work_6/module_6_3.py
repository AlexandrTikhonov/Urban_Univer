import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        dz_1 = self._cords[2] + dz * self.speed
        if dz_1 < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] = dz_1

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Be careful, i'm attacking you 0_0")
        else:
            print("Sorry, i'm peaceful :)")


class Bird(Animal):
    beak = True

    @staticmethod
    def lay_eggs():
        choice_ = random.randint(1, 4)
        print(f"Here are(is) {choice_} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        dz_1 = self._cords[2] + dz * self.speed / 2
        if dz_1 < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[2] = dz_1


class PoisonousAnimal:
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):

    def __init__(self, speed):
        super().__init__(speed)
        self.sound = "Click-click-click"
        _DEGREE_OF_DANGER = 8


    def speak(self):
        print(self.sound)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
