#  programme to calculate a user’s total holiday cost,
#  which includes the plane cost, hotel cost,and car-rental cost

#  city and respective cost for flight

city_costs = {"London": 100, "Paris": 120, "Madrid": 150, "Rome": 170}

#  ideally below I wanted to include error validation if int not entered, but was not sure how to do it?
#  so have prompted user instead

num_nights = int(input("Please enter number of nights you will be staying at a hotel as a number e.g. 1,2,3...: "))
rental_days = int(input("Please enter number of days you will hire a car for as a number e.g. 1,2,3...: "))

def hotel_cost (num_nights, nightly_rate=100):
    hotel_stay = num_nights * nightly_rate
    return hotel_stay

def plane_cost (city):
    if city in city_costs:
        cost_for_flight = city_costs[city]
    else:
        cost_for_flight = 200  # Default cost for other city not in dict
    return cost_for_flight
    
def car_cost (rental_days, daily_rate=50):
    tot_car_rental = rental_days * daily_rate
    return tot_car_rental

# Let the user choose a city
selected_city = input("Please enter the city you will be visiting (London, Paris, Madrid, Rome): ")

# Calculate individual costs
hotel_stay = hotel_cost(num_nights)
plane_cost = plane_cost(selected_city)
tot_car_rental = car_cost(rental_days)

# Calculate total holiday cost
total_holiday_cost = hotel_stay + plane_cost + tot_car_rental

print("Total Holiday Cost: $" + str(total_holiday_cost))