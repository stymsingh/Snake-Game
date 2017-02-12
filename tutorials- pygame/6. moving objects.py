import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')

gameExit = False

lead_x = 300
lead_y = 300
#lead_x and lead_y are the location of the head of the snake

lead_x_change = 0 #initially set to zero

while not gameExit:
    for event in pygame.event.get():#used to get events from the queue
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10 #move by segmnts of 10 to left
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10 #move by segmnts of 10 to ryt

    lead_x += lead_x_change
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,10,10])
    pygame.display.update() #to update the background color from black to white


pygame.quit()
quit()





