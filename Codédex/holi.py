# Daily Challenge: March 4, 2026
# Completed On: May 10, 2026

# Given a 7 x 7 grid representing an area covered in Holi powders.
# Each cell contains an emoji representing one of seven colors.
# Find all of the colors missing from the 7 x 7 grid
import itertools

def find_missing_colors(grid):
  color_list = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]

  # Convert grid to list, then apply hashset, then back to list (syntax)
  hash_flat_grid = list(set(list(itertools.chain(*grid))))
  # Check that each color on our list exists in grid
  return [item for item in color_list if item not in hash_flat_grid]
