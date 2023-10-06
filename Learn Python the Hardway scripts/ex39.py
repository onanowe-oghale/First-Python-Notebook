#Dictionaries, oh lovely Dictionaries
#create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'Carlifornia': 'CA',
    'New York' : 'NY',
    'Michigan': 'MI'
}

#Create a basic set of states and some cities in them

cities = {
    'CA': 'San Franisco',
    'MI': 'Detriot',
    'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('>' *10)
print("NY State has: ", cities['NY'])
print("OR state has: ", cities['OR'])

#Print some states 
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abreviation is : ", states['Florida'])

#do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every state abbreviation
print('-' * 10)
for state , abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}") 

#print every city in state
print('-' *10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time
for state, abbrev in list(states.items()):
    print(f"{state} srate is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
#safely get a abbreviation by the state that might not b there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas")

# get a city with default value
city = cities.get('TX', 'Does Not Exist') 
print(f"The city for the state 'TX' IS: {city}")   