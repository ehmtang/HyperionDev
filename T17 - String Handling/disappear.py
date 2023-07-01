my_string = input("Enter a sentence: ")

# Create empty list, to store characters
list_of_char_removed = []

# User input characters to be removed
char_removed = input("Enter characters to be removed from sentence: ")

# Loop list of characters
for idx, char in enumerate(char_removed):
    
    # Store list of characters
    list_of_char_removed.append(char)

# Loop each characters contained in the string to be removed
for idx, char in enumerate(list_of_char_removed):

    # Remove character from string
    my_string_strip = my_string.replace(char, '')
   
    # Update string with removed character
    my_string = my_string_strip

print(my_string_strip)
