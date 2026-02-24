# 🌟 Exercise 2: Dogs

# Goal: Create a Dog class with methods for barking, 
# running speed, and fighting.

# Key Python Topics:
#     Classes and objects
#     Methods
#     Attributes

# Instructions:
# Step 1: Create the Dog Class
#     Create a class called Dog with name, age, and 
#       weight attributes.
#     Implement a bark() method that returns 
#       “<dog_name> is barking”.
#     Implement a run_speed() method that returns 
#       weight / age * 10.
#     Implement a fight(other_dog) method that 
#       returns a string indicating which dog won the 
#       fight, based on run_speed * weight.

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} won the fight!"
        elif my_power < other_power:
            return f"{other_dog.name} won the fight!"
        else:
            return "It's a tie!"

# Step 2: Create Dog Instances
#     Create three instances of the Dog class with 
#       different names, ages, and weights.

dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 25)
dog3 = Dog("Bella", 4, 18)

# Step 3: Test Dog Methods
#     Call the bark(), run_speed(), and fight() 
#       methods on the dog instances to test their 
#       functionality.

# Test bark
print(dog1.bark())
print(dog2.bark())

# Test run_speed
print(f"{dog1.name}: speed is {dog1.run_speed()}")
print(f"{dog2.name}: speed is {dog2.run_speed()}")

# Test fight
print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog1.fight(dog3))
