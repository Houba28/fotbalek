import pygame, sys, os
from pygame.locals import *
###########################################################################
#os.putenv('SDL_FBDEV', '/dev/fb1')

pygame.init()

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
 
# draw on the surface object
screen.fill(WHITE)

myfont = pygame.font.SysFont("monospace", 15)
# set up the window
screen = pygame.display.set_mode((480, 320))
label = myfont.render("Some text!", 1, (255,255,0))
screen.blit(label, (1, 1))

pygame.draw.polygon(screen, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# run the game loop
while True:
    for event in pygame.event.get():
            if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
    pygame.display.update()