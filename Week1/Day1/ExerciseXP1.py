# 🌟 Exercise 1: Converting Lists into Dictionaries

# Key Python Topics:
#    Creating dictionaries
#    Zip function or dictionary comprehension

# Instructions

# You are given two lists. Convert them into a 
# dictionary where the first list contains the keys 
# and the second list contains the corresponding 
# values.

# Lists:

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Expected Output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

number_tuples = list(zip(keys, values))

print(number_tuples)

number_dict = dict(number_tuples)

print(number_dict)
