# Literally doesn't work 

import random
import requests

# The word to use as the prefix for the usernames
prefix = "hello"

# List of possible words to use as the suffix
words = ["apple", "banana", "carrot", "diamond", "elephant", "fish", "grape", "house", "icecream", "juice"]

# Function to generate a random Roblox username
def generate_username():
  # Choose a random word as the suffix
  suffix = random.choice(words)
  # Return the generated username
  return prefix + "_" + suffix

# Function to check if a Roblox username is valid
def check_username(username):
  # Send a request to the Roblox API to check the username
  url = f"https://api.roblox.com/users/username-available?username={username}"
  response = requests.get(url)
  if response.status_code != 200:
    print(f"Error checking username {username}:", response.text)
    return False
  
  # Check the response to see if the username is available
  data = response.json()
  return data["success"]

# Open a file for writing
with open("roblox_usernames.txt", "w") as f:
  # Generate and check a random username until a valid one is found
  while True:
    username = generate_username()
