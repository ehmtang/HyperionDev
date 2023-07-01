# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:05:32 2022

@author: erwin
"""

#%%
name = input("What is your name? ")
email = input("What is your email? ")

print(f"\nHi " + name + "! " + "We will be contacting you shortly at " + email)

#%%
# Repeating actions

"""
Create while loop
input a number
counts donw
when number reaches negative break
return the average of the countdown excluding -1

"""

def average_of_countdown(number):
    # type cast into integer
    val = int(number)
    
    # create empty array
    arr =[]
    
    # decrement integer 
    while val > 0:
        
        # append new value to array
        arr.append(val)
        
        # decrement value
        val -= 1
        
        # sum of the array
        sum_of_countdown = sum(arr)
        
        # length of the array
        len_of_countdown = len(arr)
        
        # calculate the average of the array
        average_of_countdown = sum_of_countdown/len_of_countdown
    
    # print the last calculation of the average of the array
    return print("The average of the countdown is " + str(average_of_countdown)) 

# user inputs a positive number
number = input("Enter a positive integer ")

# Implement function
average_of_countdown(number)

#%%

def average_of_countdown_with_checks():
    
    # Loop function until user inputs correct number
    while True:
        
        # user inputs a number
        number = input("Enter a positive integer: ")
        try:
            
            # cast type as int
            val = int(number)
            
            # if number is 0, the average is 0
            if val == 0:
                print("The average of countdown is 0")
            
            # check if number is positive
            elif val > 0:
                
                # prompt user, number is positive and an integer
                print("It's an integer and it's positive; run countdown function.")
                
                # create empty array
                arr =[]
                
                # loop average of countdown. This can be rewritten as a nested function.
                while val > 0:
                    
                    # append new value to array
                    arr.append(val)

                    # decrement value
                    val -= 1

                    # sum of the array
                    sum_of_countdown = sum(arr)

                    # length of the array
                    len_of_countdown = len(arr)
                    
                    # calculate the average of the array
                    average_of_countdown = sum_of_countdown/len_of_countdown

                # print the last calculation of the average of the array
                return print("The average of the countdown is " + str(average_of_countdown))

            # if input is negative, asks user to try again
            elif val < 0:  
                print("Input is negative. Try again")
                continue
            break
        
        # if input is not an integer, asks user to try again
        except ValueError:
            print("Input is not an integer. Try again")     

# Implement function
average_of_countdown_with_checks()

#%%

time = list(range(0, 24, 1))

# function to check if guard is on duty
def guard_on_duty(hour):
    
    #cast type to integer
    hour = int(hour)
    
    # check if hours is between 7 to 17
    if 7 <= hour <= 17:
        guard = False
        print("No guard, go to the library.")
    
    # otherwise guard is 
    else:
        guard = True
        print("Go see guard for access to the library.")

# user input positive integer
hour = input("Enter the hour, you go to the library: ")

# Implement function
guard_on_duty(hour)

#%%

# Current waiting line
waiting_line = ['Paula', 'Alberta', 'Carla', 'Roberta', 'Martha']
print()
print(waiting_line)

# Jenny joins the waiting line at the front
waiting_line.insert(0,'Jenny')
print()
print(waiting_line)

# Woman third in line (index=2), leaves the waiting line.
waiting_line.pop(2)
print()
print(waiting_line)

# Alice joins the line at the end
waiting_line.append('Alice')
print()
print(waiting_line)

#%%
# Letter frequency

# string to do frequency test on
string = "You can have data without information, but you cannot have information without data."

# convert to lower case
string = string.lower()

# clean string from punctuations, whitespaces and special characters
string = ''.join(char for char in string if char.isalnum())

# create empty set
char_frequency = {}

# loop each character in the string
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
    
    
    
#%%

print()
print("Identity matrix")
size = int(input("enter size of NxN matrix: ")) 
for row in range(0, size):
    for col in range(0, size):
 
       # Here end is used to stay in same line
      if (row == col):
          print("1 ", end=" ")
      else:
          print("0 ", end=" ")
    print()


print()
print("Mirrored Identity matrix")
for row in range(0, size):
    for col in range(0, size):
 
       # Here end is used to stay in same line
      if (row + col + 1 == size):
          print("1 ", end=" ")
      else:
          print("0 ", end=" ")
    print()
# %%

# Prison Break
"""
for idx, item in enumerate(list):
   if 'foo' in item:
       item = replace_all(...)
       list[idx] = item
"""

# function for prison break
def freed_prisoners(prison):
    
    print()

    # cast type as boolean, it's easier that way 
    prison = list(map(bool, prison))
    
    # initialise counter 
    count_flip = 0

    # loop each prison_cell starting from index 0
    for idx, cell in enumerate(prison):
        
        # prompt user checking the cell
        print("I'll check the door...")
        
        # if cell is false, it's open
        if prison[idx] == False:
            print("...It's open, I don't need to flip the switch.")
        
        # if cell is true, it's locked
        elif prison[idx] == True:
            print("...It's locked, I need to unlock the cell!")

            # True become False, False becomes True
            prison = [not elem for elem in prison]
            
            # increment counter
            count_flip += 1
            print("I've flipped the switch.")           
            
        print()
    return print(count_flip)

# Implement function
freed_prisoners([1, 1, 0, 0, 0, 1, 0])
print()
freed_prisoners([1, 1, 1])
print()
freed_prisoners([0, 0, 0])
print()
freed_prisoners([0, 1, 1, 1])
print()


