# 🌟 Exercise 4 : Afternoon at the Zoo

# Goal:
# Create a Zoo class to manage animals. The class 
# should allow adding animals, displaying them, 
# selling them, and organizing them into alphabetical 
# groups.

# Key Python Topics:
#     Classes and objects
#     Object instantiation
#     Methods
#     Lists
#     Dictionaries (for grouping)
#     String manipulation

# Instructions
# Step 1: Define the Zoo Class
# 1. Create a class called Zoo.
# 2. Implement the __init__() method:
#     It takes a string parameter zoo_name, 
#       representing the name of the zoo.
#     Initialize an empty list called animals to keep 
#       track of animal names.
# 3. Add a method add_animal(new_animal):
#     This method adds a new animal to the animals 
#       list.
#     Do not add the animal if it is already in the 
#       list.
# 4. Add a method get_animals():
#     This method prints all animals currently in the 
#       zoo.
# 5. Add a method sell_animal(animal_sold):
#     This method checks if a specified animal exists 
#       on the animals list and if so, remove from it.
# 6. Add a method sort_animals():
#     This method sorts the animals alphabetically.
#     It also groups them by the first letter of 
#       their name.
#     The result should be a dictionary where:
#         Each key is a letter.
#         Each value is a list of animals that start 
#           with that letter.
# 7. Add a method get_groups():
#     This method prints the grouped animals as 
#       created by sort_animals().
# Step 2: Create a Zoo Object
#     Create an instance of the Zoo class and pass a 
#       name for the zoo.
# Step 3: Call the Zoo Methods
#     Use the methods of your Zoo object to test 
#       adding, selling, displaying, sorting, and 
#       grouping animals.

# Step 1: Define the Zoo Class
# 1. Create a class called Zoo.
# 2. Implement the __init__() method:
#     It takes a string parameter zoo_name, 
#       representing the name of the zoo.
#     Initialize an empty list called animals to keep 
#       track of animal names.

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

# 3. Add a method add_animal(new_animal):

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

# 4. Add a method get_animals():

    def get_animals(self):
        print(f"Animals in {self.zoo_name}: {self.animals}")

# 5. Add a method sell_animal(animal_sold):

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

# 6. Add a method sort_animals():

    def sort_animals(self):
        sorted_animals = sorted(self.animals)

        groups = {}
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in groups:
                groups[first_letter] = []
            groups[first_letter].append(animal)

        self.groups = groups
        return groups
    
# 7. Add a method get_groups():

    def get_groups(self):
        if not self.groups:
            self.sort_animals()

        print("Animal groups:")
        for letter, animals_list in self.groups.items():
            print(f"{letter}: {animals_list}")

# Step 2: Create a Zoo Object

my_zoo = Zoo("Jerusalem Zoo")

# Step 3: Call the Zoo Methods

my_zoo.add_animal("Ape")
my_zoo.add_animal("Baboon")
my_zoo.add_animal("Bear")
my_zoo.add_animal("Cougar")
my_zoo.add_animal("Cat")
my_zoo.add_animal("Giraffe")
my_zoo.add_animal("Eagle")

my_zoo.get_animals()

my_zoo.sell_animal("Bear")
my_zoo.get_animals()

my_zoo.sort_animals()

my_zoo.get_groups()
