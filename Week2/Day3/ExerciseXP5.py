# 🌟 Exercise 5: Amount of time left until January 1st

# Goal: Create a function that displays the amount of 
# time left until January 1st.

# Key Python Topics:
#     datetime module
#     Time difference calculations

# Instructions:
# Use the datetime module to calculate and display the 
#   time left until January 1st.
# more info about this module HERE

# Step 1: Import the datetime module

from datetime import datetime

# Step 2: Get the current date and time

def time_until_new_year():
    now = datetime.now()

# Step 3: Create a datetime object for January 1st of 
#   the next year

    next_year = now.year + 1
    jan_first = datetime(next_year, 1, 1)

# Step 4: Calculate the time difference

    time_left = jan_first - now

# Step 5: Display the time difference

    days = time_left.days
    seconds = time_left.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    print(f"Time left until January 1st: {days} days, {hours} hours, {minutes} minutes left.")
#    print("Time left until January 1st:")
#    print(time_left)

time_until_new_year()