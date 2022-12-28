import os # I added this
import pyfiglet

# Prompt the user for the text to convert to ASCII art
text = input("Enter the text to convert to ASCII art: ")

# Use the pyfiglet library to generate the ASCII art
ascii_art = pyfiglet.figlet_format(text)

# Print the ASCII art
print(ascii_art)
os.system("pause") # Added this
