price_of_package = float(input("Enter the price of the package you would like to purchase: "))
distance_of_delivery = float(input("Enter the total distance of the delivery in kms: "))

transport = input("Enter mode of transport: ")
if transport == "air":
    transport_cost = distance_of_delivery * 0.36
elif transport == "freight":
    transport_cost = distance_of_delivery * 0.25

insurance_coverage = input("Enter insurance coverage: ")
if insurance_coverage == "full":
    insurance_cost = 50
elif insurance_coverage == "limited":
    insurance_cost = 25

gift_coverage = input("Do you require gift coverage, 'yes' or 'no': ")

if gift_coverage == "yes":
    gift_cost = 15
elif gift_coverage == "no":
    gift_cost = 0

delivery_coverage = input("Do you require 'priority' or 'standard delivery': ")
if delivery_coverage == "priority":
    delivery_cost = 100
elif delivery_coverage == "standard delivery":
    delivery_cost = 20

total_cost = price_of_package + transport_cost + insurance_cost + gift_cost + delivery_cost
print(total_cost)

# I think switch case statements would be better here