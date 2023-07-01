# Dictionary containing abbreviations (key) and their meanings (value)
abbre_dict = {
    'ADSL' : 'Asymmetric Digital Subscriber Line',
    'API' : 'Application Programming Interface',
    'IDE' : 'Integrated Development Environment',
    'SDK' : 'Software Development Kit'
    }

abbre_dict['UI'] = 'User Interface'
abbre_dict['UX'] = 'User Experience'

print(abbre_dict)

abbreviation = input('Enter an abbreviation: ')

if abbreviation in abbre_dict.keys():
    print(f"{abbreviation} means {abbre_dict[abbreviation]}")
else:
    print("Abbreviation not found")
