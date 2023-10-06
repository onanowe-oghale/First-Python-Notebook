#building a python dictionary based on heroes and their sides and their abbreviations and also a list connecting the heroes to their sidekicks using their abbreviations

heroes = {
    'superman' : 'SPM',
    'batman' : 'BTM',
    'wonderwoman' : 'WW',
    'aqua-man' : 'AQM',
    'flash' : 'FL'
}

sides_kicks = {
    'SPM' : 'superboy',
    'BTM' : 'robin',
    'WW' : 'wondergirl',
    'AQM' : 'aqualad',
    'FL' : 'kidflash'
}


for hero, abbrev in (heroes.items()):
    print(f"For each hero named {hero} their abbreviation is {abbrev}")


for hero, secondvar in (heroes.items()):
    print(f"For each heroes abbrevaition {secondvar} their fullname is {hero}") 
    print(f"Their sidekick is also {sides_kicks[secondvar]}")  


hero = heroes.get('superman')    
if not hero:
    print("That doesn't exist")
else:
    print("Yhupp he's here check the dictionary")  


a = ['Time', 'chance', 'peace', 'war'] 

n = 5 
while n > 0:
    n-=1
    if n==2:
       continue
    print(n)


super_powers = dict(
    superman = 'heat',
    wonderwoman = 'speed'
)

print(super_powers['superman'])