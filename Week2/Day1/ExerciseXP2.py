# 🌟 Exercise 2 : Dogs

# Goal: Create a Dog class, instantiate objects,
# call methods, and compare dog sizes.

# Key Python Topics:
#     Classes and objects
#     Object instantiation
#     Methods
#     Attributes
#     Conditional statements (if)

# Instructions:
# Create a Dog class with methods for barking and
# jumping. Instantiate dog objects, call their methods,
# and compare their sizes.

# Step 1: Create the Dog Class
#     Create a class called Dog.
#     In the __init__ method, take name and height as 
#       parameters and create corresponding attributes.
#     Create a bark() method that prints “<dog_name> 
#       goes woof!”.
#     Create a jump() method that prints “<dog_name> 
#       jumps <x> cm high!”, where x is height * 2.

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Step 2: Create Dog Objects
#     Create davids_dog and sarahs_dog objects with 
#       their respective names and heights.

davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 35)

# Step 3: Print Dog Details and Call Methods
#     Print the name and height of each dog.
#     Call the bark() and jump() methods for each dog.

print(f"{davids_dog.name} is {davids_dog.height} cm high.")
davids_dog.bark()
davids_dog.jump()

print()

print(f"{sarahs_dog.name} is {sarahs_dog.height} cm high.")
sarahs_dog.bark()
sarahs_dog.jump()

# Step 4: Compare Dog Sizes

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is {davids_dog.height - sarahs_dog.height} cm higher than {sarahs_dog.name}.")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is {sarahs_dog.height - davids_dog.height} cm higher than {davids_dog.name}.")
else:
    print("Both dogs are the same height.")
