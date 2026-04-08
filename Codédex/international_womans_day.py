# Daily Challenge: March 8, 2026
# Completed On: April 8, 2026

# Analyze trends and quantify each company's progress in “closing the gap"
# using three metrics: net change per year, trend, and dips
def analyze(percentages):
  # Average yearly increase or decrease (round to four decimals)
  net_change_per_year = round((percentages[-1] - percentages[0]) / (len(percentages) - 1), 4)

  # Compares last 3-year average to first 3-year average
  first_avg = sum(percentages[0:3]) / 3; last_avg = sum(percentages[-3:]) / 3
  trend = "improving" if last_avg > first_avg else "improving" if last_avg is first_avg else "declining"

  # Number of years where percentage decreased compared to the previous year
  dips = 0
  dips += sum(1 for cur_index in range(1, len(percentages)) if percentages[cur_index] < percentages[cur_index - 1])

  # Returns an array with the three calculations above
  return net_change_per_year, trend, dips
