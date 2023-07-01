
# Return total cost of hotel
def hotel_cost(nights_in_hotel):

    # Cost = number of nights * 50
    hotel_costs = nights_in_hotel * 50    

    return hotel_costs

# Return plane ticket price based on destination
def plane_cost(destination):

    # Plane cost determined by the destination
    if destination == 'Los Angeles':
        plane_costs =  500
    elif destination == 'New York':
        plane_costs =  600
    elif destination == 'London':
        plane_costs =  200
    elif destination == 'Paris':
        plane_costs =  300
        
    return plane_costs

# Return total cost of car rental
def car_rental(days_rental):
   
    # Cost = number of days * 30
    car_rental_cost = days_rental * 30

    return car_rental_cost

# Return the total cost of the holiday
def holiday_cost(nights_in_hotel, destination, days_rental):
    
    # Total cost = hotel_cost + plane_cost + car_rental
    total_cost = hotel_cost(nights_in_hotel) + plane_cost(destination) + car_rental(days_rental)
    
    return total_cost

# Test functions with different parameter values

nights_in_hotel = 7
destination = 'London'
days_rental = 4

print(f"\n{nights_in_hotel} nights in the hotel costs: {hotel_cost(nights_in_hotel)}")
print(f"Plane ticket to {destination} costs: {plane_cost(destination)}")
print(f"Car rental for {days_rental} days costs: {car_rental(days_rental)}")
print(f"Total cost of holiday: {holiday_cost(nights_in_hotel,destination, days_rental)}")


nights_in_hotel = 14
destination = 'New York'
days_rental = 0

print(f"\n{nights_in_hotel} nights in the hotel costs: {hotel_cost(nights_in_hotel)}")
print(f"Plane ticket to {destination} costs: {plane_cost(destination)}")
print(f"Car rental for {days_rental} days costs: {car_rental(days_rental)}")
print(f"Total cost of holiday: {holiday_cost(nights_in_hotel,destination, days_rental)}")


nights_in_hotel = 3
destination = 'Los Angeles'
days_rental = 3

print(f"\n{nights_in_hotel} nights in the hotel costs: {hotel_cost(nights_in_hotel)}")
print(f"Plane ticket to {destination} costs: {plane_cost(destination)}")
print(f"Car rental for {days_rental} days costs: {car_rental(days_rental)}")
print(f"Total cost of holiday: {holiday_cost(nights_in_hotel,destination, days_rental)}")

nights_in_hotel = 10
destination = 'Paris'
days_rental = 11

print(f"\n{nights_in_hotel} nights in the hotel costs: {hotel_cost(nights_in_hotel)}")
print(f"Plane ticket to {destination} costs: {plane_cost(destination)}")
print(f"Car rental for {days_rental} days costs: {car_rental(days_rental)}")
print(f"Total cost of holiday: {holiday_cost(nights_in_hotel,destination, days_rental)}")
