# 🌟 Exercise 1: Cats

# Key Python Topics:
#     Classes and objects
#     Object instantiation
#     Attributes
#     Functions

# Instructions:
# Use the provided Cat class to create three cat 
# objects. Then, create a function to find the 
# oldest cat and print its details.

# Step 1: Create Cat Objects
#     Use the Cat class to create three cat objects 
#       with different names and ages.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat(cat_name="Socks", cat_age=3)
cat2 = Cat(cat_name="Squeaky", cat_age=2)
cat3 = Cat(cat_name="Marilla", cat_age=7)

# Step 2: Create a Function to Find the Oldest Cat
#     Create a function that takes the three cat 
#       objects as input.
#     Inside the function, compare the ages of the 
#       cats to find the oldest one.
#     Return the oldest cat object.

def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1
    
    if cat2.age > oldest.age:
        oldest = cat2
        
    if cat3.age > oldest.age:
        oldest = cat3
        
    return oldest

# Step 3: Print the Oldest Cat’s Details
#     Call the function to get the oldest cat.
#     Print a formatted string: “The oldest cat is 
#       <cat_name>, and is <cat_age> years old.”
#     Replace <cat_name> and <cat_age> with the 
#       oldest cat’s name and age.

oldest = find_oldest_cat(cat1, cat2, cat3)

print(f"The oldest cat is {oldest.name}, and she is {oldest.age} years old.")



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




# 🌟 Exercise 3 : Who’s the song producer?

# Goal: Create a Song class to represent song lyrics 
# and print them.

# Key Python Topics:
#     Classes and objects
#     Object instantiation
#     Methods
#     Lists

# Instructions:
# Create a Song class with a method to print song
# lyrics line by line.

# Step 1: Create the Song Class
#     Create a class called Song.
#     In the __init__ method, take lyrics (a list) 
#       as a parameter and create a corresponding 
#       attribute.
#     Create a sing_me_a_song() method that prints 
#       each element of the lyrics list on a new line.

# Example:
# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()
# Output: There’s a lady who’s sureall that glitters is goldand she’s buying a stairway to heaven

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song([
    "There's a lady who's sure",
    "All that glitters is gold",
    "And she's buying a stairway to heaven"
])

stairway.sing_me_a_song()





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
