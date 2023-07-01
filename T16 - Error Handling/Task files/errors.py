# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print ("Welcome to the error program") # SyntaxError, missing parenthesis
print (f"\n") # IndentationError, unexpected indent and SyntaxError, missing parenthesis. Likely to have missed out f-string for new line.

ageStr = "24 years old" #I'm 24 years old. #IndentationError, #NameError, used equality operator
age = int(ageStr[0:2]) #IndentationError, #ValueError, characters cannot be typecasted as integers
print(age)
print("I'm " + f"{age}" + " years old.") #IndentationError, #TypeError cannot concatenate int to str, added whitespace after 'I'm' and before 'years old'
three = "3" #IndentationError, 

answerYears = age + int(three) #IndentationError, #TypeError cannot add int to str, casted three as int

print("The total number of years: " + f"{answerYears}") # SyntaxError, missing parenthesis. 'answerYears' not in within f-strings and calling variable, added whitespace after ':'
answerMonths = answerYears * 12 #NameError, answer not defined. Likely to calling answerYears
print("In 3 years and 6 months, I'll be " + f"{answerMonths + 6}" + " months old.") # SyntaxError, missing parenthesis. Missing f-string and curly braces. Result did not calculate the additional 6 months. Added full-stop at end of sentence

#HINT, 330 months is the correct answer

