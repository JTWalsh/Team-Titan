import spyral 
import random
import math
import MainScreen


WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

class Garage(spyral.Sprite):
    def __init__(self, scene):
		super(Garage, self).__init__(scene)
        
		self.image = spyral.Image(size=(5, 5))
		self.image = spyral.Image("images/Garage.png")
		self.anchor = 'center'     #Default anchor is 'topleft'

class GarageScene(spyral.Scene):
	def __init__(self):
		super(GarageScene, self).__init__(SIZE)

		spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
		spyral.event.register("system.quit", spyral.director.quit)

		self.background = spyral.Image("images/Background.png")
                
		CarGarage = Garage(self)
                CarGarage.pos = ((WIDTH/2), (HEIGHT/2)-100)

		class RegisterForm(spyral.Form):
			BackButton = spyral.widgets.Button("Go Back to Main Menu")
    		self.my_form = RegisterForm(self)

		self.my_form.focus()
		self.my_form.BackButton.pos = ((WIDTH/2)-50, (HEIGHT/2) + 300)

		spyral.event.register("form.RegisterForm.BackButton.clicked", self.goToMenu)

	
	def goToMenu(self):
		spyral.director.pop
		spyral.director.push(MainScreen.MainMenu()) 
