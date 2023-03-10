
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"


#=============Shoe list===========
shoe_list = []

#==========Functions outside the class==============

# Read inventory.txt and append each line into shoe_list
# Prompt user if FileNotFound 
def read_shoes_data():
    try:
        with open("./inventory.txt", "r") as inventory:       
            for idx, line in enumerate(inventory):
                
                # Skip first line and any lines that are empty
                if idx == 0:
                    pass
                elif line == "\n":
                    pass
                
                # Split and append obj into the 'shoe_list'
                else:
                    line = line.rstrip().split(',')
                    shoe_list.append(Shoe(line[0], line[1], line[2], int(line[3]), int(line[4])))
    
    except FileNotFoundError as error:
        print("The file that you are trying to open does not exist.")
        print(error)

# Append new shoe into inventory
# Prompt user if FileNotFound 
# read_shoes_data rerun to refresh shoe_list
def capture_shoes():
    try:
        country = input("Enter country: ")
        code = input("Enter code: ")
        product = input("Enter product: ")
        cost = input("Enter cost: ")
        quantity = input("Enter quantity: ")
       
        with open("./inventory.txt", "a") as inventory:
            inventory.write(f"\n{country},{code},{product},{cost},{quantity}")
            print("Inventory added")
        
        # Reread data with updated inventory
        read_shoes_data()

    except FileNotFoundError as error:
        print("The file that you are trying to write to does not exist.")
        print(error)

# Print all shoes from shoe_list in console
def view_all():
    print("\nDisplaying all products in inventory:")
    print("Country, Code, Product, Cost, Quantity")
    for shoe in shoe_list:
       print(shoe.__str__())

# Identify stock from shoe_list
# Prompt user if item requires restocking
# If yes update quantity 
# and rerun read_shoes_data for updated shoe_list
def re_stock():
    # Use min() method to find shoe with lowest quantity
    lowest_qty = min(shoe_list, key=lambda shoe: shoe.get_quantity())

    # Output the results
    print("\nProduct with the lowest quantity:")
    print("Country, Code, Product, Cost, Quantity")
    print(lowest_qty.__str__())
 
    # Retreive the index of minimum value 
    idx = shoe_list.index(lowest_qty)

    re_stock_menu = input("Do you wish to restock this product - 'yes' or 'no'? ").lower()
    
    if re_stock_menu == "yes":
        try:
            re_stock_qty = int(input("Enter quantity you wish to restock: "))
            
            if re_stock_qty < 0:
                print("Please enter a positive integer.")

            shoe_list[idx].quantity = shoe_list[idx].quantity + re_stock_qty
            
            with open("./inventory.txt", "w") as inventory:
                inventory.write("Country,Code,Product,Cost,Quantity\n")
                for shoe in shoe_list:
                    inventory.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
                print("Inventory amended")
                
                # Reread data with updated inventory
                read_shoes_data()

        # Prompt user to enter a valid positive integer
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    elif re_stock_menu == "no":
        return

    else:
        print("Input invalid.")
    

# Search shoe by user input of shoe code
# Return shoe via code
def search_shoe():
    search_shoe_menu = input("Enter shoe code: ")
    
    shoe_searched = [shoe for shoe in shoe_list if shoe.code == search_shoe_menu]
    print("\nProduct searched using code:")
    print("Country, Code, Product, Cost, Quantity")
    print(shoe_searched[0].__str__())        

# Return all products and their stock value
def value_per_item():
    print("\nProducts and their value per item:")
    print("Country, Code, Product, Cost, Quantity, Stock Value")
    for shoe in shoe_list:
        print(f"{shoe.__str__()}, {shoe.cost * shoe.quantity}")

# Return product with highest quantity
# and prompt user product is for sale.
def highest_qty():
    highest_qty = max(shoe_list, key=lambda shoe: shoe.get_quantity())
    
    # Output the results
    print("\nProduct with the highest quantity:")
    print("Country, Code, Product, Cost, Quantity")
    print(highest_qty.__str__())
    print("\n... Product is for sale.")


#==========Main Menu=============

while True:
    menu = input(f'''\nSelect one of the following Options below:
r - Read shoe data
c - Add new shoe data
va - View all shoe data
re - Restock lowest quanitity product
s - Search by shoe code
v - Return stock value for each product
h - Return product with highest quantity
quit - Exit
: ''').lower()

    if menu == 'r':
        read_shoes_data()

    elif menu == 'c':
        capture_shoes()

    elif menu == 'va':
        view_all()

    elif menu == 're':
        re_stock()

    elif menu == 's':
        search_shoe()

    elif menu == 'v':
        value_per_item()

    elif menu == 'h':
        highest_qty()

    elif menu == 'quit':
         exit()

    else:
        print("Input invalid.")