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

#Creates the Leaderboard scene which shows the Fastest cars
class LeaderboardScene(spyral.Scene):
    def __init__(self):
        super(LeaderboardScene, self).__init__(SIZE)

        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)

        #self.background = spyral.Image("images/Leaderboard.png")
        #creates a back button to go back to the main menu
        class RegisterForm(spyral.Form):
            BackButton = spyral.widgets.Button("Go Back")
		
        self.my_form = RegisterForm(self)

        self.my_form.focus()
        self.my_form.BackButton.pos = ((WIDTH/2)-50, (HEIGHT/2) + 300)

        spyral.event.register("form.RegisterForm.BackButton.clicked", self.goToMenu)

	#Pops the leaderboard scene and pushes the MainMenu scene forward
    def goToMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu()) 





