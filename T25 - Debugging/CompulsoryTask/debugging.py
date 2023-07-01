def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key]) #NameError k not defined, changed to key

simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": "d'oh", "maggie": " (Pacifier Suck)"} #SyntaxError on 'd'oh', changed to single quote to double quotations

print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer']) #TypeError functions calls 2 arguments, keys encapsulated as a list of keys. 

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

