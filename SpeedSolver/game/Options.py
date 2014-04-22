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


class OptionScene(spyral.Scene):
    def __init__(self):
        super(OptionScene, self).__init__(SIZE)

        self.load_style("game/style.spys")

        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)

        self.background = spyral.Image("images/Option_Menu.png")


        class RegisterForm(spyral.Form):
            BackButton = spyral.widgets.Button("Go Back")
            EasyBox = spyral.widgets.Checkbox()

        my_form = RegisterForm(self)
        my_form.focus()

        my_form.EasyBox.pos = (300, 300)
        my_form.BackButton.pos = (1100, 800)

        spyral.event.register("form.RegisterForm.BackButton.clicked", self.goToMenu)
	
    def goToMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu())
