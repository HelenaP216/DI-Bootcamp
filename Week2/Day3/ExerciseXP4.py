# 🌟 Exercise 4: Current Date

# Goal: Create a function that displays the current 
# date.

# Key Python Topics:
#     datetime module

# Instructions:
# Use the datetime module to create a function that 
#   displays the current date.

# Step 1: Import the datetime module

# from datetime import date

from datetime import date

# Step 2: Get the current date

date.today()

# Step 3: Display the date

def display_current_date():
    today = date.today()
    print(today)

display_current_date()
