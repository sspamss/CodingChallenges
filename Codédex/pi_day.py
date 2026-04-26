# Daily Challenge: March 14, 2026
# Completed On: April 26, 2026

# Calculate circumference of pie divided by number of friends
# Return crust per friend, rounded to 2 decimal places
import math

def cut_pie(diameter, friends):
  circumference = math.pi * diameter
  return round(circumference / friends, 2)
