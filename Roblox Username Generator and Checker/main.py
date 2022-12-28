# This most likely will not find a valid username but still a great attempt for ChatGPT

import string # Importing this myself
import random
import requests

# The word to use as the prefix for the usernames
prefix = "hello"

# Function to generate a random Roblox username
def generate_username():
  # Choose a random selection of characters from the alphabet and digits
  characters = string.ascii_letters + string.digits
  # Shuffle the characters to ensure a random selection
  characters = random.sample(characters, k=8)
  # Return the generated username
  return prefix + "_" + "".join(characters)

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
    if check_username(username):
      # Write the valid username to the file
      f.write(username + "\n")
      break
