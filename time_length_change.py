


#1. Calculate 42 minutes and 42 seconds in seconds

def calculate_seconds(minutes, seconds):
    total_seconds = (minutes * 60) + seconds
    return total_seconds

minutes = 42
seconds = 42

total_seconds = calculate_seconds(minutes, seconds)
print(f"Total seconds in {minutes} minutes and {seconds} seconds: {total_seconds}")

#2. Calculate 10 kilometers to miles

def calculate_miles(miles, kilometers):
    total_miles = (kilometers / 1.61)
    return total_miles

kilometers = 10
miles = kilometers / 1.61

total_miles = calculate_miles(miles, kilometers)
print(f"Total miles in {kilometers} kilometers: {total_miles}")


