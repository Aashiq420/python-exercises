#Defining function to calculate cost of stay
def hotel_cost(nights):
    cost_hotel = nights*140
    return cost_hotel
#Taking input from user and sending it to the function and printing results
stay = int(input("How many nights did you stay? "))
hotel_cost(stay)
print("Your stay will cost R"+str(hotel_cost(stay)))

#Defining function to determine flight cost by destination
def plane_ride_cost(city):

    if city.lower() == "cape town":
        price = 2500
    elif city.lower() == "durban":
        price = 2300
    elif city.lower() == "johannesburg":
        price = 2000
    elif city.lower() == "bloemfontein":
        price = 1800
    else:
        print("Entry not on list")
        price = 0
    return price
#Taking input from user and sending it to the function and printing results
user = input("Enter the city you want to travel to: ")
price1=plane_ride_cost(user)
print("Price of trip: R"+str(plane_ride_cost(user)))

#Defining function to calculate rental car cost
def rental_car_cost(days):
    cost = days*40
    if days>=7:
        cost=cost-50
    elif days>=3:
        cost=cost-20
    return cost
#Taking input from user to send to function
user_1=int(input("How many days was the car rented for: "))
rental_car_cost(user_1)
print("The cost of rental is: R"+str(rental_car_cost(user_1)))

#Defining function to deteremine total trip cost from above functions
#this function calls from 3 other functions to return a total cost value
def trip_cost(city,days,spending):
    total_cost = hotel_cost(days)+plane_ride_cost(user)+rental_car_cost(days)+spending
    return total_cost

#taking input for spending money and sending to trip_cost
spend = int(input("How much spending money will you need? "))
print("Total cost of trip: R"+str(trip_cost(price1,user_1,spend)))