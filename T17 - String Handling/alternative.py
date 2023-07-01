my_string = "Hello World Joe Blogg's cat"

# Create empty list for string manipulation
alt_char = []

# Loop each character in string
for idx, char in enumerate(my_string):
    
    #If index is even, capitalise character
    if (idx%2) == 0:
        char = char.upper()
        alt_char.append(char)
    
    # Else index is odd, de-capitalise character
    else:
        char = char.lower()
        alt_char.append(char)

# Join list of characters to string
alt_char = "".join(alt_char)
print(alt_char)

print("-"*60)

# New string
my_string = "I am learning to code"

# Split each word in string
list_of_words = my_string.split()

# Create empty list for string manipulation
alt_word = []

# Loop each word in string
for idx, word in enumerate(list_of_words):
    
    #If index is even, de-capitalise word
    if (idx%2) == 0:
        word = word.lower()
        alt_word.append(word)
    
    # Else index is even, capitalise word
    else:
        word = word.upper()
        alt_word.append(word)
        
# Join list of words to string
alt_word = " ".join(alt_word)
print(alt_word)