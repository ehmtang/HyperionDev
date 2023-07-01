str_manip = input("Enter a string: ")

# Length of string
print(f"\n{len(str_manip)}")

# Find last character in string
last_letter = str_manip[-1]

# Print string with last_letter replaced with "@" 
str_manip_with_replacement = str_manip.replace(last_letter, "@")
print(f"\n{str_manip_with_replacement}")

# Get last character in string
last_three_letters = str_manip[-3:]

# Print reversed last_three_letters
print(f"\n{last_three_letters[::-1]}") 

# Get first three and last two characters in string
new_word = str_manip[0:3] + str_manip[-2:]
print(f"\n{new_word}")