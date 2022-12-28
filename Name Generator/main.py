import random
import os # Added this 

# List of possible first names
first_names = ["Alice", "Bob", "Charlie", "David", "Emily", "Frank"]

# List of possible last names
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis"]

# Function to generate a random name
def generate_name():
  # Choose a random first and last name
  first_name = random.choice(first_names)
  last_name = random.choice(last_names)
  # Return the generated name
  return first_name + " " + last_name

# Generate a random name
name = generate_name()

# Print the generated name
print("Generated name:", name)
os.system("pause") # Added by me

# Asked ChatGPT to generate a script of it's choice