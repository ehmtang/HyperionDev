my_string = input("Enter a sentence: ")

# Split each word in string
list_of_words = my_string.split()

# Loop each word in string
for idx, word in enumerate(list_of_words):
    
    # Print word on new line
    print(f"\n{word}")
        
