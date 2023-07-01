with open('./input.txt', 'w+') as f:
    my_string = f"I have a cat and a dog.\nTheir names are Cerveza and Limon"
    list_of_words = my_string.split(' ')
    lines = my_string.split(f"\n")

    # Write string to file
    f.write(f"{my_string}\n")
    
    # Write length to file
    f.write(f"\nMy string has {len(my_string)} characters.")

    # Write number of words to file
    f.write(f"\nMy string has {len(list_of_words)} words.")

    # Write number of lines to file
    f.write(f"\nMy string has {len(lines)} lines.")

f.close