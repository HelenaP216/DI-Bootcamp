# 🌟 Exercise 6: Birthday and minutes

# Key Python Topics:
#     datetime module
#     datetime.datetime.strptime() (parsing dates)
#     Time difference calculations
#     .total_seconds() method

# Instructions:
# Create a function that accepts a birthdate as an 
#   argument (in the format of your choice), then 
#   displays a message stating how many minutes the 
#   user lived in his life.

from datetime import datetime

def minutes_lived(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    now = datetime.now()
    time_difference = now - birthdate
    total_seconds = time_difference.total_seconds()
    total_minutes = int(total_seconds // 60)

    return total_minutes

minutes = minutes_lived("1980-06-24")

print(f"You have lived approximately {minutes} minutes.")
