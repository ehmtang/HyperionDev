# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

animal = "lion" #NameError 'Lion' not defined. Likely to be missing quotations. Corrected capitalisation 
animal_type = "cub"
number_of_teeth = 16

full_spec = "This is a "f"{animal}"". It is a "f"{animal_type}"" and it has "f"{number_of_teeth}"" teeth." #Missing f-strings and quotations. 'number_of_teeth' and 'animal_type' order changed. Added full-stop at end of sentence.

print(full_spec) #SyntaxError missing parenthesis

