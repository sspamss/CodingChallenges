# Daily Challenge: March 23, 2026
# Completed On: April 24, 2026

# Find longest consecutive kitten group where max - min stays within limit
# Return length of longest group of consecutive kittens that can stay calm
def cuddly_kittens(kittens, limit):
  # Number of longest group; where current group starts
  longest = 0; left = 0

  for right in range(len(kittens)):
    # If current group is over limit, move "left" to right until it fits again
    while max(kittens[left:right + 1]) - min(kittens[left:right + 1]) > limit:
      left += 1

    # Check if current group or new group has longest group
    longest = max(longest, right - left + 1)

  return longest
