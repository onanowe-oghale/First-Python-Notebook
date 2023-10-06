#study drill: Making a Dictionary(mapping) of 10 states and Nigeria and cities in them.

#states

States = {
   # 'Abuja' : 'Abj',
    'Delta' : 'Del',
    'Lagos' : 'Lag',
    'Crossriver': 'CR',
    'Rivers' : 'Rv',
    'Oyo' : 'Oy',
    'Kwara' : 'Kw',
    'Ondo' : 'Oo',
    'Enugu' : 'Enu',
    'Imo' : 'Im'
}

cities = {
  #  'Abj' : 'Gwarimpa',
    'Del' : 'Asaba',
    'Lag' : 'Lekki',
    'CR' : 'Calabar',
    'Rv' : 'Port-Harcourt',
    'Oy' : 'Ibadan',
    'Kw' : 'Ilorin',
    'Oo' : 'Akure',
    'Enu' : 'Enugu',
    'Im' : 'Owerri'
}

cities_Abbrev = {
    #'Gwarimpa' : 'Gwa',
    'Asaba' : 'Asb',
    'Lekki' : 'Lek',
    'Calabar' : 'Cal',
    'Port-Harcourt' : 'PH',
    'Ibadan' : 'IB',
    'Ilorin' : 'Il',
    'Akure' : 'AK',
    'Enugu': 'En',
    'Owerri': 'Owe'
}

print(f"{States['Delta']} state has : {cities['Del']}")
print(f"{States['Rivers']} state has : {cities['Rv']}")

print('!' * 30)
print("Delta's abbreviation is :", States['Delta'])
print("Kwara's abbreviation is :", States['Kwara'])

print('$' * 30)
#print("Gwarimpa is abbreviated as : ", cities_Abbrev[cities['Abj']]) 
print(f"{cities['Del']} is abbreviated as : ", cities_Abbrev[cities['Del']])
print(f"Port Harcourt is abbreviated as : ", cities_Abbrev[cities['Rv']])
print(f"{cities['Oy']} is abbreviated as :", cities_Abbrev[cities['Oy']])

print('--' * 30)
#print(f"{States['Abuja']} has the city {cities['Abj']}")
print(f"{States['Lagos']} has the city {cities[States['Lagos']]}")
print(f"{States['Rivers']} has the city {cities[States['Rivers']]}")

print('#' *10)
for state ,abbrev in list(States.items()):
    print(f"The abbreviated form of {state} is {abbrev}")

for city, citys_abbrev in list(cities.items()):
    print(f"The abbreviated city {city} has {citys_abbrev}")    

for state , abbrev in list(States.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city named {cities[abbrev]}")
    print(f"and the city is abbreviated as {cities_Abbrev[abbrev]}")

print('^' *40)

state = States.get('Kogi')

if not state:
    print("Sorry, no Kogi.")

city = cities.get('KG','Does Not Exit')
print(f"The city for the state 'KG' is: {city}") 



