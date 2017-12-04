#Preparing Snake game basing on Wormy by Al Sweigart
#http://inventwithpython.com/pygame

import random, pygame, sys
from pygame.locals import *

FPS = 15
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE ==0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH/CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT/CELLSIZE)

# R G B
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
DARKGREEN = (0,155,0)
DARKGRAY = (40,40,40)
BGCOLOR = BLACK

UP ='up'
DOWN ='down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 # syntacitc sugar: index of the worm`s head

def main():
  global FPSCLOCK, DISPLAYSURF, BASICFONT
  
  pygame.init()
  FPSCLOCK = pygame.time.Clock()
  DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
  BASICFONT = pygame.font.Font('freesansbold.ttf, 18)
  pygame.display.set_caption('Snake')
  
  showStartScreen()
  while True:
    runGame()
    showGameOverScreen()
    
def runGame():
  #Set random start point
  startx = raindom.randint(5, CELLWIDTH - 6)
  starty = random.randint(5, CELLHEIGHT - 6)
  wormCoords = [{'x': startx, 'y': starty},
      {'x': startx - 1, 'y': starty},
      {'x': startx - 2, 'y': starty}]
  direction = RIGHT
  
  #Start the apple in a random place.
  apple = getRandomLocation()
  
  while True:# main game loop
    for event in pygame.event.get(): #event handling loop
      if event.type == QUIT:
        terminate()
      elif event.type ==KEYDOWN:
        if(event.key == K_LEFT or event.key ==K_a) and direction != RIGHT:
          direction = LEFT
        elif (event.key == K_RIGTH or event.key == K_d) and direction !=LEFT:
          direction = RIGHT
        elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
          direction = UP
        elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
          direction = DOWN
        elif event.key == K_ESCAPE:
          terminate()
          
