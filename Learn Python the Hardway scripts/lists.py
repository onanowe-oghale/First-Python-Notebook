#Lists 

#snack list 

drinks = ["coke", "fanta", "Ribena", "Hollandia", "pulpy" , "sprite", "Caprrisonne" , "Fresh-yo", "Sosa", "Savanah", "Malt"]
drinks_not_ordered = "5Alive Active Evap Rcsoda Teem Schweeps"

print(len(drinks))
print(drinks[4])

for drink in drinks:
    print(f"This is a drink named {drink}")

now_we = drinks_not_ordered.split(' ')
print(now_we)

we_win = now_we.pop()
drinks.append(we_win)
print(drinks)

rexed = '#'.join(drinks[3:5])

print(rexed)