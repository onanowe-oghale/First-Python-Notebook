#EX30: Else If

#list of variable used to test 
people = 30
cars = 40
trucks = 15

#if cars are more than people
if cars > people:
#prints this if cars are more than people    
    print("We should take the cars.")
#asks if cars are less than people    
elif cars < people:
#prints this if cars are less than people   
    print("We should not take the cars.")
#prints what is in the block if the if and elif blocks above are not true.    
else:
    print("We can't decide.")
#asks if trucks are more than cars
if trucks > cars:
#prints if trucks are more than cars    
    print("That's to many trucks.") 
#prints if trucks are less than cars   
elif trucks < cars:
    print("Maybe we could take the trukcs.")
#prints if the statements above are all false    
else:
    print("We still can't decide.")

#asks if people are more than trucks
if people > trucks:
    print("Alright, let's just take the trucks.")
#prints when the if statement is not true.    
else:
    print("Fine, let's stay home then.")     



#complex booleans 

#1-------------------
if cars > people or trucks < cars:
    print("The cars are greater than the people already but the trucks aren't greater than the cars..")


#2-------------------
if people > trucks and people > cars:
    print("We can see.")
elif people > trucks or people > cars:
    print("The OR has saved the day and this is true..")
else:
    print("Suitable solution not found.")    

#3-------------------------
if trucks > people and (not(people > cars)):
    print("Well look what we have here.")
else:
    print("That's the end then.")
