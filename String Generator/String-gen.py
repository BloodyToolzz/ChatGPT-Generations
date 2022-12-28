import random

# Generate a random string starting with "END-"
def generate_string():
  # Choose a random length for the string
  length = random.randint(5, 10)
  # Initialize the string with "END-"
  s = "END-"
  # Generate random characters and append them to the string
  for i in range(length - 4):
    s += chr(random.randint(ord('a'), ord('z')))
  return s

# Prompt the user for the number of strings to generate
num_strings = int(input("How many strings would you like to generate? "))

# Open a text file for writing
with open("output.txt", "w") as f:
  # Write the generated strings to the file
  for i in range(num_strings):
    f.write(generate_string() + "\n")
