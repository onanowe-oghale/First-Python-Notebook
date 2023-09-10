#EX.10 

#Variable named tabby_cat the \t in the string nakes the string to be tabbed to the right
tabby_cat = "\tI'm tabbed in."

#Variable called persian_cat where the string is made to continue on the next line with the use of /n
persian_cat = "I'm split\non a line"

#variable named backlash cat with two \\ where one \ makes the other in its pair not to show when printed.
backlash_cat = "I'm \\ a \\ cat. "

#Variable named fat_cat where the ''' makes the string to be written on more than one line. \t* makes the string on each line to be tabbed, appear in a list form and move to the next line. \n\t* Grass that appears on the before the ''' means what is written after it goes to the next line and is tabbed as well. 
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''

#Prints what is in variables tabby_cat, persian_cat, backlash_cat, fat_cat.

print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)


#Trial to use Escape Sequences and foramt strings to create a more complex format.

Balon_dor_winner_1 = "Ronaldo"
Balon_dor_winner_2 = "Lionel Messi"
top_fighter_1 = "Neymar"
top_fighter_2 = "Ribery"

print("The 2008 best player in the world was", Balon_dor_winner_1)
print("After that year the", Balon_dor_winner_2, "Won three on a bounce")

Verdict = 'There has been alot of debate for who is the GOAT between', Balon_dor_winner_2, 'and', Balon_dor_winner_1
print(Verdict)

opinion = "For every Balon d'or year there has been an outsider"

print = (opinion, f"in the year 2015 it was",top_fighter_1)
