# Daily Challenge: March 18, 2026
# Completed On: April 11, 2026

# Find voucher with highest dollar per hour within given options and criterias
# Skip any voucher where delay is greater than max hours willing to wait
# Return index of best valid voucher, or -1 if no option qualifies
def pick_voucher(vouchers, delays, max_wait):
  best_index = -1
  best_rate = -1

  for index, (voucher_amount, delay_hours) in enumerate(zip(vouchers, delays)):
    # Skip option because wait time is longer than max willing to wait time
    if delay_hours > max_wait: continue

    # Calculate dollars per hour current voucher gives
    rate = voucher_amount / delay_hours

    # Update best option only when this rate is better
    if rate > best_rate:
      best_rate = rate
      best_index = index

  # Return index of best valid voucher, or -1 if none qualify
  return best_index
