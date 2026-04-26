# Daily Challenge: March 7, 2026
# Completed On: April 25, 2026

# Calculate total amount of sleep debt and longest number of days with sleep debt
# Return total sleep debt and longest sleep debt streak
def calculate_sleep_debt(planned, actual):
  # Start at 1 due to daylight savings; track current sleep debt streak; track highest sleep debt streak
  sleep_debt = 1; cur_longest_streak = 0; longest_streak = 0

  for i in range(len(planned)):
    # If actual < planned, we are in sleep debt
    if actual[i] < planned[i]:
      sleep_debt += planned[i] - actual[i]
      cur_longest_streak += 1
    # Otherwise, sleep debt streak broken
    else:
      cur_longest_streak = 0
    
    # Check if we already have longest streak, or we just found new highest
    longest_streak = max(longest_streak, cur_longest_streak)

  return sleep_debt, longest_streak
