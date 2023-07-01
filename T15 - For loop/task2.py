year = int(input("What year do you want to start with? "))
number_of_years = int(input("How many years do you want to check? "))

# Start loop from year to year + number of years
for year in range(year, year+number_of_years):
    
    # Not divisible by 4 - not a leap year
    if (year%4) != 0:
        print(f"{year} isn't a leap year")
    
    # Divisible by 4 - is a leap year
    elif (year%4) == 0:
        print(f"{year} is a leap year")