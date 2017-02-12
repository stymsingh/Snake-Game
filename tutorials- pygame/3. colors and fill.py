import pygame

x = pygame.init()

#defining colorss in rgb format
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Snaky!!!!')#game title

gameExit = False

#event handler in python
while not gameExit: #game loop
    #event handler loop
    for event in pygame.event.get():#used to get events from the queue
        #print(event)
        if event.type == pygame.QUIT:
            gameExit = True

    # .fill is used to set color
    gameDisplay.fill(white)
    pygame.display.update()#to update the background color from black to white




pygame.quit()

quit()