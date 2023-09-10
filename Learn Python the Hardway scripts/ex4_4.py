#Study drill for EX.4
#The reason there was an error 'car_pool_capacity' is not defined if because most likely it was spelt wrongly or one of the variable in it was also not rightly spelt and therefore the right value could not be assigned.

#The amount of cars
cars = 100

#The space in each car
space_in_a_car = 4

#The amount of drivers available to drive the given cars
drivers = 30

#The total amount of passengers on ground
passengers = 90

#Thw number of cars not driven 
cars_not_driven = cars - drivers

#The numbers of cars driven which is equal to the amount of drivers available
cars_driven = drivers

# The total number capacity all the cars can take
carpool_capacity = cars_driven * space_in_a_car

# The average amount of people that can enter a given car.
average_passengers_per_car = passengers / cars_driven

print ("There are", cars, "cars available.")
print ("We are only", drivers, "drivers available.")
print ("There will be ", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity,"people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")