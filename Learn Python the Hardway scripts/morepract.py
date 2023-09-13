print("I'm going to be testing everything I've learnt so far with football analgoies")
print("The biggest football club by miles in Germany is")
print("------BAYERN MUNICH------")
print('The big boys of the \'BUNDESLIGA\' ')

reason = """
And here's the reason why: \n 
\t The Bavarians have the most league titles in the country
they have also won 10 straight bundesliga titles on the bounce
they have the best player available in the country in the likes of:
Harry Kane
Joshua Kimmich
Manuel Neuer
\n \t \t Their home is the Allianz Arena in Munich
"""
print(reason)
print("Lets calculate the number of UCL finals they've lost")

finals_Attend = 11
finals_Won = 6
print("Bayern have made it to", finals_Attend, "UCL finals")
print("And have won {}".format(finals_Won), 'of those')#

finals_lost = finals_Attend - finals_Won

print(f"So they have lost {finals_lost} UCL finals too")

#This section is of no fact and for playing arounf purposes only

clubsnum = 1000

def club(into):
    german = into * 2
    englandm = german / 2
    spainm = englandm - 100
    return german, englandm , spainm 

print("The base number of clubs in a certain place is usually over {}".format(clubsnum) )

germany , england , spain = club(clubsnum)

numully = club(clubsnum)
print("In Germany there are over {} club also about {} in England and {} in spain." .format(*numully))

clubsnume = clubsnum *10
club(clubsnume)
print(f"it would be an exageration to say germany has {germany} clubs with England having {england} clubs and Spain has {spain} clubs")

#trying the multiple formatting one last thing

clubsnum = clubsnum - 10
real = club(clubsnum)
print("Real values should be about {} for Germany {} for the English and {} for the Spainards". format(*real))