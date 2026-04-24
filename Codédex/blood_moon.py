# Daily Challenge: March 3, 2026
# Completed On: April 23, 2026

# Given a timestamp in the format "HH:MM" (24-hour time),
# predict the next 3 times a blood moon will occur given that they are 2 hours and 48 minutes apart
import datetime

def blood_moon(time):
  hours = int(time[0:2]); minutes = int(time[3:5])
  predictions = []

  for i in range(3):
    # If minutes pass 59, we are in the next hour so mod 60
    # We also automatically mod hours in case it goes past 24
    if ((minutes + 48) > 59):
      hours = (hours + 3) % 24; minutes = (minutes + 48) % 60
    # Otherwise, we are still in the same hour, do nothing special
    # Again, also automatically mod hours in case it goes past 24
    else:
      hours = (hours + 2) % 24; minutes = minutes + 48

    # Convert hours and minutes back to military time string, then add to predictions array
    new_time = datetime.time(hours, minutes)
    format_time = new_time.strftime("%H:%M")
    predictions.append(format_time)

  return predictions
