import pygame.key
import pygame 
import random


#Initialize
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#background
background = pygame.image.load('7756629.jpg')

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#player
playerImg= pygame.image.load('space-invaders.png')
playerX= 370
playerY= 480
playerX_change=0
playerY_change=0

#enemy
enemyImg= pygame.image.load('alien.png')
enemyX= random.randint(0,800)
enemyY= random.randint(50,150)
enemyX_change=0.3
enemyY_change=40


def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y):
    screen.blit(enemyImg, (x, y))


#Game Loop
running= True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
         # if key stroke is pressed check whether its right or left 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                playerX_change = -0.4
            if event.key == pygame.K_RIGHT: 
                playerX_change = 0.4
            if event.key == pygame.K_UP: 
                playerY_change = -0.2
            if event.key == pygame.K_DOWN: 
                playerY_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerY_change = 0
                
    


    #RGB - Red, Green, Blue
    screen.fill((0,0,0))
    #background
    screen.blit(background, (0,0))

    #checking players boundary
    playerX += playerX_change

    if playerX< 0:
        playerX= 0
    elif playerX > 736:
        playerX= 736

    playerY += playerY_change

    #Enemy's movement

    enemyX += enemyX_change

    if enemyX< 0:
        enemyX_change= 0.3
        enemyY += enemyY_change
    elif enemyX > 736:
        enemyX_change= -0.3
        enemyY += enemyY_change


    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()



