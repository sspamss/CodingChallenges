def calculate_score(elements):
  # Sum of element scores
  total_score = 0

  # Unpack array of lists, no need for element name so use "_"
  for _, base_value, judges_scores in elements:
    # Sort judges scores, skip highest and lowest judges scores, then take average
    avgGoe = sum(sorted(judges_scores)[1:8]) / 7
    # Calculate element score using given formula
    element_score = base_value + (avgGoe * 0.1 * base_value)
    # Add each element score to overall total
    # (element_score only stores one number at a time)
    total_score += element_score

  # Sum of element scores rounded to 1 decimal place
  return round(total_score, 1_
