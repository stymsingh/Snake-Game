import pygame
x = pygame.init()
#init() -> (numpass, numfail)
#Initialize all imported Pygame modules. No exceptions will be raised if a module fails, but the total number if successful and failed inits will be returned as a tuple.

gameDisplay = pygame.display.set_mode((800,600))
# setting the canvas height to 800px wide and 600 px tall

pygame.display.update()
#used to update entire frame

pygame.quit()
#uninitialize all pygame modules
#quit() -> None
#Uninitialize all pygame modules that have previously been initialized.
quit()