
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


