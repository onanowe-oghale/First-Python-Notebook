#testing

#the top 6
Manutd = 20
Mancity = 5
Chelsea = 5
Liverpool = 19
Arsenal = 14
Tottenham = 8

#Manutd Liverpool--------------------------------------
print("The condition has asked About Manutd and Liverpool.")
if Manutd > Liverpool:
    print("Manutd have the most PL titles\n")
else: 
    print("Liverpool dominate English football\n")


#Mancity Arsenal---------------------------------------
print("This section asks about Mancity and Arsenal.")
if Mancity > Arsenal:
    print("Mancity are bigger then arsenal\n") 
elif Mancity == Arsenal:
    print("They are quite equal and on the same level in terms of titles won.\n")
elif Mancity >= Arsenal:
    print(f"Mancity either have more with {Mancity} or they similar\n")
elif Arsenal > Mancity:
    print(f"Arsenal have more PL titles with {Arsenal} as againt Mancity's {Mancity}.\n")
else:
    print("No suitable solution in the comparison was found.\n")


#Chelsea and Mancity----------------------------------------
print("This section asks about Chelsea and Mancity.")
if Chelsea > Mancity:
    print("Chelsea have more PL titles than Mancity\n")
elif Chelsea == Mancity:
    print("They both have equal PL titles.\n")
elif Chelsea >= Mancity:
    print(f"They either have the same or Chelsea have more with Chelsea having {Chelsea} and City having {Mancity}.\n")    
else:
    print("No suitable solution can be found\n")

#Tottenham and Arsenal
print("This section asks about Tottenham and Arsenal.")
if Tottenham > Arsenal:
    print("Tottenham are the biggest club in London\n")
else:
    print("We'll get back to you on this\n")    