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

    gameDisplay.fill(white)
    #to draw rectangles
    pygame.draw.rect(gameDisplay, black, [400,300,10,10])
    #parameters : where to draw recangle,color,list of( coordinates, and width and height)

    #another way of drawing rect, ittakes a list of coordinates, width and height
    gameDisplay.fill(red, rect=[200,200,50,50])



    pygame.display.update()#to update the background color from black to white




pygame.quit()

quit()