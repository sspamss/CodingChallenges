# Daily Challenge: March 2, 2026

# Given two strings, secret and guess, which are guaranteed to be of the same length (5 letters),
# determine how many characters are correct and in the exact same position
def wordle_guess(secret, guess):
  # Turn words into array of letters
  secretArray = list(secret)
  guessArray = list(guess)

  # Count how many indices have matching values
  counter = 0

  # Loop through both arrays
  for i, (x, y) in enumerate(zip(secretArray, guessArray)):
    # Check if values at indices match, if so increase counter
    if x == y:
      counter += 1
      
  return counter
