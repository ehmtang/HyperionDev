employee = input("Enter 'salesman' or 'manager': ")
if employee == "salesman":
    sales = float(input("Enter gross sales for the month: "))
    salary = 2000 + (0.08 * sales)
    print(salary)

elif employee == "manager":
    hours = float(input("Enter number of hours worked for the month: "))
    salary = 40 * hours
    print(salary)

