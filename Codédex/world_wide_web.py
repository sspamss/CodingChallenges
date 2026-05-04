# Daily Challenge: March 12, 2026
# Completed On: May 3, 2026

# Given a string representing a web address, determine if it's a valid URL or not:
# 1. It starts with http:// or https://
# 2. The domain must contain at least one dot .
# 3. The domain only contains letters, digits, hyphens -, or dots .
import re

def check_url(address):
  # Match http/https, valid domain parts separated by single dots, and a letter-only ending
  pattern = r"(https?:\/\/)([a-zA-Z\d\-]+\.)+([a-zA-Z]+)$"

  return "valid" if re.fullmatch(pattern, address) else "invalid"
