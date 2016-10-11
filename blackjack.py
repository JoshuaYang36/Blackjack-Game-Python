"""
Author: Joshua Yang
CIS 211, Project 5, UO, Spring 2014
"""
from tkinter import *
from Deck import *
from CardLabel import *
from tkinter.messagebox import showinfo
import time

d = Deck()
d.shuffle()

player_hand = [ ]
dealer_hand = [ ]
d_showing_cards = [ ]
p_showing_cards = [ ]

clicks = 2

amount_of_games = 1
win = 0
loss = 0


def score(hand):
	result = 0
	numAce = 0
	for card in hand:
		result += BlackjackCard(card._id).points()
		if card._id == 12 or card._id == 25 or card._id == 38 or card._id == 51:
			numAce += 1
	
	while result > 21 and numAce > 0:
		result -= 10
		numAce -= 1

	return result

def winners():
	global win
	win += 1
	winner.configure(state="normal")
	winner.delete(0,END)
	winner.insert(1,win)
	winner.configure(state="disabled")

def losing():
	global loss
	loss += 1
	loser.configure(state="normal")
	loser.delete(0, END)
	loser.insert(0, loss)
	loser.configure(state="disabled")

def deal():
	global d_showing_cards, p_showing_cards, clicks, dealer, player, amount_of_games
	Hit.configure(state='normal')
	Pass.configure(state='normal')
	clicks = 2
	d = Deck()
	d.shuffle()
	d_showing_cards = [ ]
	p_showing_cards = [ ]	
	
	total_games.configure(state="normal")
	amount_of_games += 1
	total_games.delete(0, END)
	total_games.insert(0, amount_of_games)
	total_games.configure(state="disabled")
	
	dealer = d.deal(6)
	player = d.deal(6)
	
	d_showing_cards.append(dealer[0])
	d_showing_cards.append(dealer[1])
	p_showing_cards.append(player[0])
	p_showing_cards.append(player[1])

	#Dealer's hand
	dealer_hand[0].display('back', dealer[0]._id)
	dealer_hand[1].display('front', dealer[1]._id)
	i = 2
	while i < 6:
		dealer_hand[i].display('blank', dealer[i]._id)
		i += 1

	#Player's hand
	player_hand[0].display('front', player[0]._id)
	player_hand[1].display('front', player[1]._id)

	p = 2
	while p < 6:
		player_hand[p].display('blank', player[p]._id)
		p += 1

	if score(p_showing_cards) == 21:
		winners()
		showinfo("Game Over", "YOU WIN!!! 21!!")
	
	if score(d_showing_cards) == 21:
		losing()
		showinfo("Game Over", "Dealer wins...")

		
def hit():
	global dealer, player, clicks, d_showing_cards, p_showing_cardsxs
	if clicks < 6:
		player_hand[clicks].display('front', player[clicks]._id)
		p_showing_cards.append(player[clicks])
		clicks += 1

	if score(p_showing_cards) == 21:
		dealer_hand[0].display('front', dealer[0]._id)
		showinfo("Game Over", "YOU win!!!")
		winners()
		Hit.configure(state='disable')
		Pass.configure(state='disable')

	elif score(p_showing_cards) > 21:
		dealer_hand[0].display('front', dealer[0]._id)
		losing()
		showinfo("Game Over", "Dealer wins...bummer!")
		
		Hit.configure(state='disable')
		Pass.configure(state='disable')

	if len(p_showing_cards) > 4 and score(p_showing_cards) <= 21:
		dealer_hand[0].display('front', dealer[0]._id)
		winners()
		showinfo("Game Over", "YOU win!!!")
	
	if len(d_showing_cards) > 4 and score(d_showing_cards) <= 21:
		dealer_hand[0].display('front', dealer[0]._id)
		losing()
		showinfo("Game Over", "Dealer winssss")			

def Pass():
	global d_showing_cards, p_showing_cards, dealer, player
	time.sleep(.5)
	dealer_hand[0].display('front', dealer[0]._id)

	Hit.configure(state='disable')
	Pass.configure(state='disable')
	
	for i in range(6):
		i += 2
		if score(d_showing_cards) < 17:
			dealer_hand[i].display('front', dealer[i]._id)
			d_showing_cards.append(dealer[i])
		i += 1

	if score(p_showing_cards) == 21 or (len(p_showing_cards) == 5 and score(p_showing_cards) < 21) or (score(d_showing_cards) > 21 and score(p_showing_cards) < 21):
		winners()
		showinfo("Game Over", "YOU WIN!!!")

	elif score(d_showing_cards) == 21 or (score(p_showing_cards) > 21 and score(d_showing_cards) > 21) or (score(p_showing_cards) > 21 and score(d_showing_cards) < 21):
		losing()
		showinfo("Game Over", "Dealer wins... you lost")

	if score(p_showing_cards) < 21 and score(d_showing_cards) < 21:
		if score(p_showing_cards) < score(d_showing_cards):
			losing()
			showinfo("Game Over", "Dealer wins...until next time!")
			
		if score(p_showing_cards) > score(d_showing_cards):
			winners()
			showinfo("Game Over", "YOU win!!!")

	if score(p_showing_cards) == score(d_showing_cards):
		showinfo("Game Over", "Whoa a tie game. Try again!")


root = Tk()

CardLabel.load_images()

# Dealer's card labels
for i in range(6):
	D_card = CardLabel(root)
	D_card.grid(row=0, column=i, padx=15)
	dealer_hand.append(D_card)

# Player's card labels
for i in range(6):
	P_card = CardLabel(root)
	P_card.grid(row=1, column=i, padx=15)
	player_hand.append(P_card)

# Turns over the cards at the beginning of the game
dealer = d.deal(6)
player = d.deal(6)

d_showing_cards.append(dealer[0])
d_showing_cards.append(dealer[1])
p_showing_cards.append(player[0])
p_showing_cards.append(player[1])

# Dealer's hand
dealer_hand[0].display('back', dealer[0]._id)
dealer_hand[1].display('front', dealer[1]._id)
i = 2
while i < 6:
	dealer_hand[i].display('blank', dealer[i]._id)
	i += 1

# Player's hand
p = 0
while p < 6:
	if p < 2:
		player_hand[p].display('front', player[p]._id)
	else:
		player_hand[p].display('blank', player[p]._id)
	p += 1

#Deal button
Deal = Button(root, text='Deal', command=deal)
Deal.grid(row=3, column=1, pady = 10)
#Hit button
Hit = Button(root, text='Hit me', command=hit)
Hit.grid(row=3, column=2, pady = 10)
#Pass button
Pass = Button(root, text='Pass', command=Pass)
Pass.grid(row=3, column=3, pady = 10)

total = Label(root, text="Total Games")
total.grid(row=4, column=0)
wins = Label(root, text="Wins")
wins.grid(row=4, column=1)
losses = Label(root, text="Loses")
losses.grid(row=4, column=2)

total_games = Entry(root)
total_games.grid(row=5, column=0)
total_games.configure(state="disabled")
winner = Entry(root)
winner.grid(row=5, column=1)
winner.configure(state="disabled")
loser = Entry(root)
loser.grid(row=5, column=2)
loser.configure(state="disabled")

total_games.delete(0, END)
total_games.insert(0, amount_of_games)

root.mainloop()