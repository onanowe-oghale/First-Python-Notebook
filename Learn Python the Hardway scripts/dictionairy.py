#this to help understand the concept of dictionaries

ballers = {
    'Ronaldo' : 'CR7',
    'Messi' : 'LM10',
    'Neymar' : 'Neyjr', 
    'Rooney' : 'WR10',
    'Mbappe' : 'KM10',
    'Rashford' : 'MR10',
    'Pogba' : 'PP6',
    'Modric' : 'LM10',
    'Benzema' : 'KB9',
    'Debruyne' : 'KDB',
    'pele' : 1
}

boot_link = {
    'CR7' :'Superfly',
    'Neyjr': 'Hypervenom',
    'WR10': 'Wazza',
    'LM10' : 'Predator'
}

print(ballers['Debruyne'])
print(ballers)

print(boot_link['CR7'])


print("Ronaldo uses the : ", boot_link['CR7'] )
print("Neymar uses the : ",boot_link['Neyjr'])

print('-' *10)
print("Rooney's abbreviation is", ballers['Rooney'])
print("Pogba's abbreviation is", ballers['Pogba'])

print('-'*10)
print("Ronaldo has: ", boot_link[ballers['Ronaldo']])
print(ballers['pele'])



#list side 2
Boys_age = {
    'Keem' : 4,
    'Joe' : 6,
    'Clem' : 3,
    'Tony' : 5
}

shoes = {
    4 : 'Airforce',
    6 : 'Offwhite',
    3 : 'NBs',
    5 : 'Yeezy'
}

print("Clem has: ", shoes[Boys_age['Clem']])

print("Keem has: ", shoes[Boys_age['Keem']])

print("Tony has: ", shoes[Boys_age['Tony']])

print('>><' *100)
for boy_name, age in list(Boys_age.items()):
    print(f"{boy_name} is {age} years old")


print('*' *20)
for age , shoe in list(shoes.items()):
    print(f"The owner is {age} years old and his shoe is {shoe}") 

print('🎃' *10)
for boyage, age in list(Boys_age.items()):
    print(f"{boyage} is {age}") 
    print(f"and has shoe {shoes[age]}")        

#to safely get the age of every boy that might not be there....
boy_age = Boys_age.get('Larry')

if not boy_age:
    print("Sorry, no Larry !")

#get a shoe with a default value
shoe = shoes.get('Lar', 'Does Not Exist')
print(f"The shoe for the boy 'LAR' {shoe} ")    