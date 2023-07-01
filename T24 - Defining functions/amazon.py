with open('./input.txt', 'r+', encoding='utf-8-sig') as f:
    
    #Create empty dict to store user login information
    input_dict = {}

    # For each new line in input file, split line into elements
    # Assigning first element strings 'min', 'max', 'avg' as key
    # and second element as list of integers [1,2,3,4,5,6] as value
    for line in f:
        
        input_list = line.split(':')
        
        input_list[1] = input_list[1].split(',')

        input_list[1] = list(map(int, input_list[1]))
        
        input_dict[input_list[0]] = input_list[1]

# Return minimum value in array
def get_minimum(arr):
    minimum = min(arr)
    return minimum

# Return maximum value in array
def get_maximum(arr):
    maximum = max(arr)
    return maximum

# Return average value in array
def get_average(arr):
    average = sum(arr)/len(arr)
    return average

with open('./output.txt', 'w') as output_file:
    
    # For each key in return the following result min, max, avg for the arrays in input
    # Write the result into the output file
    for key in input_dict.keys():
        
        if key == 'min':
            
            output_file.write(f"The {key} of {input_dict[key]} is {get_minimum(input_dict[key])}.\n")

        elif key == 'max':
            #get_maximum(input_dict[key])
            output_file.write(f"The {key} of {input_dict[key]} is {get_maximum(input_dict[key])}.\n")
        
        elif key == 'avg':
            #get_average((input_dict[key]))
            output_file.write(f"The {key} of {input_dict[key]} is {get_average(input_dict[key])}.\n")

