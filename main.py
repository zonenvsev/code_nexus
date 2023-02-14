
import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("time to study")
        self.gladness -= 3
        self.progress += 0.12

    def to_sleap(self):
        print("time to sleap")
        self.gladness += 3

    def to_chill(self):
        if self.progrres < -0.5:
            print("cast out")
            self.alive = False
        elif self.gladness <= 0
            print("depresion")
            self.alive = False
        elif self.progress > 50:
            print("passed externally")
            self.alive = False

    def end_of_the_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {self.progress, 2}")

    def live(self, day):
        day = "Say" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        life_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
    elif live_cube == 3:
        self.to_chil()
    self.end_of_day()

nick = Student(name="nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)


   