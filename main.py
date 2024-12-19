# Example file showing a basic pygame "game loop"
from random import randint
import pygame
from triangulation import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
polygon = ()
mouseClicking = False
polygonDraw = False
clickIndex = -1


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    mousePos = pygame.mouse.get_pos()

    mouseClicked = pygame.mouse.get_pressed()

    if mouseClicking == False and mouseClicked[0] == True and polygonDraw == True:
        clickIndex += 1

    if mouseClicking == False and mouseClicked[0] == True and polygonDraw == False:
        # print(mouseClicked[0])
        polygon = ((mousePos) , ) + polygon 
        # print(polygon)
    


    if mouseClicked[0] == True:
        mouseClicking = True
    else:
        mouseClicking = False
    
    if mouseClicked[2] == True and polygonDraw == False:
        polygonDraw = True
        triangles = triangulate(polygon)
        # print(triangles)
        drawTriangels = []
        for triangel in triangles:
            drawTriangels.append((randint(0,255),randint(0,255),randint(0,255)))
    vindex = 0
    for vertex in polygon:
        pygame.draw.circle(screen, "black", vertex, 2)
        if len(polygon) >= 2:
            pygame.draw.line(screen,"black",vertex,polygon[vindex-1])
        vindex += 1
    
    if polygonDraw == True and len(polygon) >= 3:
        #pygame.draw.polygon(screen, "black",polygon )
        # print(triangles)
        index = 0
        pygame.draw.polygon(screen,"black",polygon)
        for triangel in triangles:
            
            if index <= clickIndex:
                pygame.draw.polygon(screen,drawTriangels[index],triangel)
            index += 1
    
    if mouseClicked[1] == True:
        polygon = ()
        mouseClicking = False
        polygonDraw = False
        drawTriangels = []
        clickIndex = -1
        
    



    
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
# Knuder = []
# kh = 1
# knude =

#     if knude ikke er på samme kæde som knuden før:
#         # Fjern første element i Q
#         while len(Q) >= 2 altså så længe Q er større eller lig med 2:
#             # Forbind første element af Q med knude og slet elementet.
#         # Forbind knude med eneste element af Q
#         Q.append(knude)









