import pygame, sys, os
from pygame.locals import *
###########################################################################
#os.putenv('SDL_FBDEV', '/dev/fb1')

pygame.init()
screen = pygame.display.set_mode((480, 320))
# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
 
# draw on the surface object
screen.fill(BLACK)

myfont = pygame.font.SysFont("monospace", 15)
# set up the window
screen = pygame.display.set_mode((480, 320))
label = myfont.render("Some text!", 1, (255,255,0))
screen.blit(label, (1, 1))

# run the game loop
while True:
    for event in pygame.event.get():
            if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
            if event.type == MOUSEBUTTONDOWN:
            	pos = pygame.mouse.get_pos()
            	label = myfont.render(str(pos), 1, (255,255,0))
            	screen.fill(BLACK)
            	screen.blit(label, (1, 1))

    pygame.display.update()