import math
print("Choose either 'investment' or 'bond' from the menu below to proceed:")
print()
print("investment - to calculate the amount of interest you'll earn on your investment.")
print("bond - to calculate the amount you'll have to pay on a home loan.")

finance_calc = input("Enter finance calculator, 'investment' or 'bond': ")

# Investment calculator
if finance_calc.lower() == "investment":

    P = float(input("Enter amount deposited: "))
    r = float(input("Enter the interest rate as a percentage: "))
    r = r / 100
    t = int(input("Enter number years planned on investing: "))
    plan = input("Enter interest plan, 'simple' or 'compound': ")
    
    # Simple interest plan
    if plan == "simple":
        A = P*(1+(r*t))
        print(f"Estimated return on simple investment plan for {t} years: {A}")

    # Compound interest plan
    elif plan == "compound":
        A = P* math.pow((1+r),t)
        print(f"Estimated return on compound investment plan for {t} years: {A}")

    # Plan input unrecognised, prompt user
    else:
        print("Input was not recognised, please enter either 'simple' or 'compound'.")

# Bond calculator
elif finance_calc.lower() == "bond":
    P = float(input("Enter present value of the house: "))
    i = float(input("Enter the interest rate as a percentage: "))
    i = (i / 100) / 12
    n = int(input("Enter the number of months over which the bond will be repaid: "))
    x = (i*P) / (1 - (1+i)**(-n))
    print(f"Required monthly repayment: {x}")

# Calculator input unrecognised, prompt user
else:
    print("Input was not recognised, please enter either 'investment' or 'bond'.")