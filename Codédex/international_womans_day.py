def analyze(percentages):
  # Length of percentages array
  len_pct = len(percentages)

  # Average yearly increase or decrease (round to four decimals)
  net_change_per_year = round((percentages[len_pct - 1] - percentages[0]) / (len_pct - 1), 4)

  # Compares last 3-year average to first 3-year average
  first_avg = sum(percentages[0:3]) / 3; last_avg = sum(percentages[-4:-1]) / 3
  trend = "improving" if last_avg > first_avg else "improving" if last_avg is first_avg else "declining"

  # Number of years where percentage decreased compared to the previous year
  dips = 0
  dips += sum(1 for cur_index in range(1, len_pct) if percentages[cur_index] < percentages[cur_index - 1])

  # Returns an array with the three calculations above
  return net_change_per_year, trend, dips
