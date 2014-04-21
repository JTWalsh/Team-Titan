import spyral 
import random
import math
import Vehicle
import Options
import Garage


WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

class MainMenu(spyral.Scene):
	def __init__(self):
		super(MainMenu, self).__init__(SIZE)

		spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
		spyral.event.register("system.quit", spyral.director.quit)

		self.background = spyral.Image("images/Background.png")
                self.image = spyral.Image("images/Garage.png")
                
		playerVehicle = Vehicle.Vehicles(self)
		playerVehicle.pos = (WIDTH/2, (HEIGHT/2)+200)


                CarGarage = Garage.Garage(self)
                CarGarage.pos = ((WIDTH/2), (HEIGHT/2)-200)

		class RegisterForm(spyral.Form):
			StartGame = spyral.widgets.Button("Start Game")
			OptionButton = spyral.widgets.Button("Options")
                        GarageButton = spyral.widgets.Button("Enter Garage")
    		self.my_form = RegisterForm(self)

		self.my_form.focus()
		self.my_form.StartGame.pos = ((WIDTH/2)-50, (HEIGHT/2) + 200)
		self.my_form.OptionButton.pos = ((WIDTH/2)-50, (HEIGHT/2) + 300)
                self.my_form.GarageButton.pos = ((WIDTH/2)-50, (HEIGHT/2) - 200)

		spyral.event.register("form.RegisterForm.OptionButton.clicked", self.goToOptions)
                spyral.event.register("form.RegisterForm.GarageButton.clicked", self.goToGarage)


                #spyral.event.register("input.mouse.down.left", self.goToGarage)
                
		
	def goToOptions(self):
		spyral.director.pop
		spyral.director.push(Options.OptionScene()) 

        def goToGarage(self):
               # if pos.x > 300 and pos.x < 600 and pos.y > 350 and pos.y < 500:
               spyral.director.pop
               spyral.director.push(Garage.GarageScene())


