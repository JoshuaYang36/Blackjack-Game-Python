from tkinter import *
from Deck import *
from CardLabel import *
from random import randint

d = Deck()
d.shuffle()

player_hand = [ ]
dealer_hand = [ ]

d_score = 0
p_score = 0

clicks = 4

def score(card):
	global d_score, p_score
	values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 
	'Q':10, 'K':10, 'A':11}
	
	result = 0
	numAce = 0
	
	result += card.points()
	if card == 'A':
		numAces += 1
	
	while result > 21 and numAces > 0:
		result -= 10
		numAces -= 1

	return result

def deal():
	global d, d_score, p_score
	d.shuffle()
	# Turns over the three cards that are at the beginning of the game
	D_card1.display('back', d[0]._id)  # Dealer's face down card
	D_card2.display('front', d[1]._id) # Dealer's face up card

	for i in range(6):
		i+=2
		if i < 4:
			P_card.display('front', d[i]._id) # first two cards you see
		else:
			P_card.display('blank', d[i]._id)
	'''
	P_card1.display('front', d[2]._id)
	P_card2.display('front', d[3]._id)
	
	
	P_card3.display('blank', d[4]._id)
	P_card4.display('blank', d[5]._id)
	P_card5.display('blank', d[6]._id)
	P_card6.display('blank', d[7]._id)
	'''
	dealer_hand.append(d[0])
	dealer_hand.append(d[1])
	
	print("this is the id of player 1 card", d[2]._id)
	print("this is card number...", d[2])
	d_score += score(d[0]) + score(d[1])
	print(d_score)
	d_score = d[0].rank() + d[1].rank()
	print(d_score)

	p_score += score(d[2]) + score(d[2])
	print(p_score)
	p_score = d[2].rank() + d[3].rank()
	print(p_score)
	
def hit():
	global d_score, p_score, clicks, player_hand
	for hand in player_hand:
		hand.display('front', d[clicks]._id)
	clicks += 1

	print("inside the function hit")

def Pass():
	global d_score, p_score
	card1_dealer = d.pop()
	D_card1.display('front', card1_dealer._id)

	print("inside the function pass")

root = Tk()

CardLabel.load_images()

#Dealer's two beginning cards
D_card1 = CardLabel(root)
D_card1.grid(row=0, column=0, padx=15)
D_card2 = CardLabel(root)
D_card2.grid(row=0, column=1, padx=15)

'''
#Player's cards
P_card1 = CardLabel(root)
P_card1.grid(row=1, column=1, padx=15)
P_card2 = CardLabel(root)
P_card2.grid(row=1, column=2, padx=15)
P_card3 = CardLabel(root)
P_card3.grid(row=1, column=3, padx=15)
P_card4 = CardLabel(root)
P_card4.grid(row=1, column=4, padx=15)
P_card5 = CardLabel(root)
P_card5.grid(row=1, column=5, padx=15)
P_card6 = CardLabel(root)
P_card6.grid(row=1, column=6, padx=15)
'''

player_hand = [ ]
x = 0
while x <= 6:
	card = CardLabel(root)
	card.grid(row=1, column=x, padx=15)
	player_hand.append(card)
	x+=1


# Turns over the dealers cards that are at the beginning of the game
i = 0
while i < 6:
	if i < 2:
		card.display('front', d[i]._id) # first two cards you see
	else:
		card.display('blank', d[i]._id)

D_card1.display('back', d[0]._id)
D_card2.display('front', d[1]._id)


#Deal button
Deal = Button(root, text='Deal', command=deal)
Deal.grid(row=3, column=2, pady = 10)
#Hit button
Hit = Button(root, text='Hit', command=hit)
Hit.grid(row=3, column=3, pady = 10)
#Pass button
Pass = Button(root, text='Pass', command=Pass)
Pass.grid(row=3, column=4, pady = 10)

root.mainloop()