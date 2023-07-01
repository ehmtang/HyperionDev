# String to do frequency test on
string = "google.com"

# Convert to lower case
string = string.lower()

# Create empty dictionary
char_frequency = {}

# Loop each character in the string
for char in string:
    
    # if the character exists increment 1
    if char in char_frequency:
        char_frequency[char] += 1
    
    # otherwise the character stays at 1
    else:
        char_frequency[char] = 1

# loop and print each dictionary's entry, alphabetically, in the form 'key : value'
for key, value in sorted(char_frequency.items()):
    print(key, value, sep = ' : ')


