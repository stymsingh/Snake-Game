import pygame

x = pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('snaky!!!!')#game title


pygame.display.update()
gameExit = False

#event handler in python
while not gameExit:
    #LOOP THROUGH ALL THE EVENTS AND THEN PRINTS IT
    for event in pygame.event.get():#used to get events from the queue
        #print(event)
        if event.type == pygame.QUIT:
            gameExit = True


pygame.quit()

quit()