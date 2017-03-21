def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city = raw_input()):
    if city == "Charlotte":
        return 183
    if city == "Tampa":
        return 220
    if city == "Pittsburgh":
        return 222
    if city == "Los Angeles":
        return 475
def rental_car_cost(day):
    if day >= 7:
        return 40 * day - 50
    elif day < 3:
        return 40 * day
    elif day >= 3 and day < 7:
        return 40 * day - 20
        
def trip_cost(city, days):
    notreal = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)
    return notreal