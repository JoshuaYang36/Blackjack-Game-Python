from tkinter import *

class CardLabel(Label):
	"""
	A CardLabel is a Tk Label that displays an image of a playing card.
	"""
	def __init__(self, parent):
		Label.__init__(self, parent, image=CardLabel.back_image)
	
	image_directory = './cardimages/'
	
	@staticmethod
	def load_images():
		"""
		Get the card images from files, save them in a list (a class variable)
		"""
		CardLabel.images = [PhotoImage(file=CardLabel.image_directory + "card{}.gif".format(i)) for i in range(52)]
		CardLabel.back_image = PhotoImage(file=CardLabel.image_directory + "back-red.gif")
		CardLabel.blank_image = PhotoImage(file=CardLabel.image_directory + "blank.gif")
	
	def display(self, side='back', id=0):
		"""
		"""
		if side == 'back':
			self.configure(image=CardLabel.back_image)
		elif side == 'front':
			self.configure(image=CardLabel.images[id]) #configure is how you change the textbox
		else:
			self.configure(image=CardLabel.blank_image)