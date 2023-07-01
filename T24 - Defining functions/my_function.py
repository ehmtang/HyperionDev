# function, days_of_the_week, prints the days of the week
def days_of_the_week():
    print('Monday'),
    print('Tuesday'),
    print('Wednesday'),
    print('Thursday'),
    print('Friday'),
    print('Saturday'),
    print('Sunday'),

# call function, days_of_the_week
days_of_the_week()

# Reference https://stackoverflow.com/questions/47085552/replace-every-second-word-with-the-word-hello-using-a-function

print()

# second_hello function replaces every 2nd word with the word 'hello'
def second_hello(string):
    
    # Create new list of string
    new_string = []

    # Split string into a list of words
    # For every word in list of words
    for idx, word in enumerate(string.split()):
    
        # Every 2nd word, replace 'word' with hello
        if (idx % 2) != 0:
            new_string.append('hello')
        
        # Otherwise append 'word' from 'string'
        else:
            new_string.append(word)
    
    # print newly formed string
    print(" ".join(new_string))

# Call second_hello function
second_hello("I am a function that replaces every 2nd word with 'hello'")
