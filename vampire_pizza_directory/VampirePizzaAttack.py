#setup game

#import libraries
import pygame
from pygame import*
from random import randint
#initialize pygame
pygame.init()

#-------------------------------------------------------
#define constant varibles

#define the parameters of the game window
window_width=1100
window_height=600
window_res=(window_width,window_height)

#define tile parameters
width=100
height=100

#define colors
WHITE=(255,255,255)
#set spawn rate
spawn_rate=360

#-------------------------------------------------------
#load assets

#create window
GAME_WINDOW= display.set_mode(window_res)
display.set_caption('Attack of the Vampire Pizzas!')

#set up the background_img
background_image=image.load("gameassets/restaurant.jpg")
background_surf=Surface.convert_alpha(background_image)
background=transform.scale(background_surf,window_res)

#set up the enemy image
#load image into program
pizza_image=image.load("gameassets/vampire.png")
#convert image to a surface
pizza_surf=Surface.convert_alpha(pizza_image)
vampire_pizza=transform.scale(pizza_surf,(width,height))

#-------------------------------------------------------
#set up classes
class VampireSprite(sprite.Sprite):
    #def the vampiresprite setup method
    def __init__(self):
# take all the behavior rules from Sprite class and use them for vampire Sprite
        super().__init__()
        #Set default movement speed
        self.speed=2  
        #Randomly Select lane Between 0 and 4
        self.lane=randint(0,4)
        # add all vampire pizza sprites to a group called all_vampires
        all_vampires.add(self)
        # use vampire_pizza image as the image for vampire pizza sprites
        self.image=vampire_pizza.copy()
        # set each sprites y coordinate at the middle of the selected Lane
        y=50 + self.lane*100
        # create a rectangle for each Sprite and place it just off the right side of the screen in the correct lane
        self.rect=self.image.get_rect(center=(1100,y))
    def update(self,GAME_WINDOW):
        GAME_WINDOW.blit(self.image,(self.rect.x,self.rect.y))
        # blit the vampire pizza image here

#-------------------------------------------------------
# create class instances and groups
# create a group for all the VampireSprite instances
all_vampires=sprite.Group()
#-------------------------------------------------------
#init and draw background grid
tile_color=WHITE
for row in range(6):
    for column in range(11):
        draw.rect(background,tile_color,(width*column,height*row,
                  width,height),1)

GAME_WINDOW.blit(background,(0,0)) 
#-------------------------------------------------------
#start main game loop
#game loop
game_running=True
while game_running:

#-------------------------------------------------------
#check for events

#checking for and handling evens
    for event in pygame.event.get():

        #exit loop on quit
        if event.type==QUIT:
            game_running=False

#-------------------------------------------------------
#spawn sprites
#spawn vampire pizza sprites

    if randint(1,spawn_rate)==1:
        VampireSprite()
#-------------------------------------------------------
# update displays 
# update enemies
    for vampire in all_vampires:
        vampire.update(GAME_WINDOW)
#update display.
    display.update()


#close main game loop
#-------------------------------------------------------

#clean up game
pygame.quit()