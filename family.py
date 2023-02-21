class Grany:
    height = 196
    wealth = 100
    eyes = "blue"
    age = 87
    hair ="orange"
    stature = "tight"
class Grandad:
    height = 213
    wealth = 50
    eyes = "braun"
    age = 93
    hair ="black"
    stature = "thin"
class Mom(Grany):
    height = 163
    wealth = 200
    age = 23
    stature = "thin"
class Dad(Grandad):
    wealth = 150
    age = 34
    hair = "white"
    stature = "fat"
class Child(Mom):
    height = 137
    eyes = "orange"
    age = 6
    hair ="black"
    stature = "thin"
bob = Grandad()
elisabet = Grany()
tom = Dad()
steve = Child()
marry = Mom()
print(bob.height)
print(bob.wealth)
print(bob.eyes)
print(bob.age)
print(bob.hair)
print(bob.stature)
print(elisabet.height)
print(elisabet.wealth)
print(elisabet.eyes)
print(elisabet.age)
print(elisabet.hair)
print(elisabet.stature)
print(tom.height)
print(tom.wealth)
print(tom.eyes)
print(tom.age)
print(tom.hair)
print(tom.stature)
print(steve.height)
print(steve.wealth)
print(steve.eyes)
print(steve.age)
print(steve.hair)
print(steve.stature)
print(marry.height)
print(marry.wealth)
print(marry.eyes)
print(marry.age)
print(marry.hair)
print(marry.stature)