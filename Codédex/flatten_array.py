# Daily Challenge: March 26, 2026
# Completed On: May 9, 2026

# Given a nested list/array your task is to flatten it into a "single-level" list/array.
import re

def flatten(list):
  # Turn list into string, remove brackets and commas, then convert back to a list
  return [int(new_int) for new_int in re.sub(r"[\[\],]", " ", (str(list))).split()]
