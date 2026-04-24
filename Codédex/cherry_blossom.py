# Daily Challenge: March 20, 2026
# Completed On: April 7, 2026

# Calculate the average temperature using that day and the previous 4 days
# Return the first 1-indexed day where this 5-day rolling average exceeds 15, or -1 if none do
def cherry_blossoms(temps):
  # If temps is empty, then avg def did not clear 15°C
  if temps is None: return -1

  # Start at index 4 to get the first 5-day average
  for i in range(4, len(temps)):
    # Window sliding problem in disguise
    avg = sum(temps[i - 4 : i + 1]) / 5

    # Rolling 5-day avg is above 15°C
    if avg > 15: return i + 1
  
  # Rolling 5-day avg is below 15°C
  return -1
