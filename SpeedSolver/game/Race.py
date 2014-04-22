import spyral 
import random
import math
import MainScreen
import Vehicle
import pygame
import time
import TextInterface

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"


class RaceScene(spyral.Scene):
    def __init__(self):
        super(RaceScene, self).__init__(SIZE)
        global timeStart
        timeStart = time.time() 

        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)

        self.background = spyral.Image("images/Background.png")

        playerVehicle = Vehicle.Vehicles(self)
        playerVehicle.pos = (WIDTH/4, (HEIGHT/2)+200)

        class RegisterForm(spyral.Form):
            QuitButton = spyral.widgets.Button("Quit")
            
        self.my_form = RegisterForm(self)

        self.my_form.focus()
        self.my_form.QuitButton.pos = ((WIDTH-100), (HEIGHT-50))

        spyral.event.register('director.update', self.update)
        self.timeText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (255, 255, 255)), (WIDTH - 100, 100), str(time.time() - timeStart))
        #spyral.event.register('director.update', timeText.update(str(time.time() - timeStart))) 

        spyral.event.register("form.RegisterForm.QuitButton.clicked", self.goToMenu)

    def update(self): 
        print(time.time() - timeStart)
       
    def goToMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu())
        print(time.time() - timeStart)


        
