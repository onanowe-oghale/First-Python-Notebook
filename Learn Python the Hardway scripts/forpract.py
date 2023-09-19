#make a list

baked_snacks = ['Buns', 'Eggrolls', 'Pie', 'Breadrolls']
fried_snacks = ["Fries", 'Pringles', 'Crisps', 'Cheetos']
grilled_snack = ['Chicken', 'Turkey', 'Beef cuts', 'Peppered Gizz']

for b_snack in baked_snacks:
    print(f"We have some baked snacks of choice we have {b_snack}")

for f_snakcs in fried_snacks:
    print(f"We have some fried snacks of choice, we have {f_snakcs}")  

for g_snacks in grilled_snack:
    print(f"We have some baked snacks of choice, we have {g_snacks}") 


empty = []

#empty = list(range(0,6))------------(Alternative way to add numbers to list without the for loop)

for num in range (20, 26):
    print(f"A new number will be added and it will be {num}.")    
    empty.append(num)


for new in empty:
    print(f"This now holds the number {new}")        