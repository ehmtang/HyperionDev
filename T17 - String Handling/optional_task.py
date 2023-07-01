my_palindrome = input("Enter a word: ")
print(my_palindrome[::-1])

if my_palindrome == my_palindrome[::-1]:
    print("Your word is a palindrome!")
else:
    print("Your word is not a palindrome!")