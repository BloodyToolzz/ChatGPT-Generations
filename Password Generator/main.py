import os # I did this
import string
import random

# Function to generate a random password
def generate_password(length):
  # Choose a random selection of characters from the alphabet, digits, and special characters
  characters = string.ascii_letters + string.digits + string.punctuation
  # Shuffle the characters to ensure a random selection
  characters = random.sample(characters, k=length)
  # Return the generated password
  return "".join(characters)

# Generate a random password of length 10
password = generate_password(10)

# Print the generated password
print("Generated password:", password)
os.system("pause") # I added this

# I added the pause, I literally just asked it to create a script of it's choice