players = "Neymar Rashford Mbappe Di-maria Sancho"

newskillers = players.split(' ')

skillers_upgrade = ["Ronaldinho", "Dembele", "ASM", "Ziyech", "Depay", "Nkunku", "Musiala"]

while len(newskillers) != 12:
    print(f"We are at {len(newskillers)} but we need 12")
    next_skiller = skillers_upgrade.pop()
    print(next_skiller, "is being added")
    newskillers.append(next_skiller)
    print(f"Now we have {len(newskillers)} of the 5 star skillers we need.")

print("Now here's the list", newskillers)
print("We will do some operations now....")
print(newskillers[0])
print(newskillers[3])
print(newskillers[-1])
print(newskillers.pop())
print(' '.join(newskillers))
print(' Skilling '.join(newskillers[3:6:]))    