import pygame.key
import pygame 
import random
import math
from pygame import mixer


#Initialize
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#background
background = pygame.image.load('7756629.jpg')

#Background sound
mixer.music.load('background.wav')
mixer.music.play(-1)
mixer.music.set_volume(0.3)

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
enemyImg= []
enemyX= []
enemyY= []
enemyX_change= []
enemyY_change= []
num_of_enemies=6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)



#bullet

#Ready - You cant see the bullet on the screen
#Fire - The bullet is currently working

bulletImg= pygame.image.load('bullet.png')
bulletX= 0
bulletY= 480
bulletX_change=0
bulletY_change=1
bullet_state= "ready"

#Score

score_value=0;
font = pygame.font.Font('freesansbold.ttf', 32)

textX=10
textY=10

#Game Over text
over_font= pygame.font.Font('freesansbold.ttf',64)

def game_over_text():
    over_text= over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200,250))

def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet (x,y):
    global bullet_state
    bullet_state= "fire"
    screen.blit(bulletImg, (x+16,y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow((enemyX-bulletX),2)+ math.pow((enemyY-bulletY),2))
    if distance < 27:
        return True
    else:
        return False


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
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound= mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX= playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            
                
    


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
    
    for i in range(num_of_enemies):
        
        #Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        
        enemyX[i]+= enemyX_change[i]

        if enemyX[i]< 0:
            enemyX_change[i]= 0.3
            enemyY[i]+= enemyY_change[i]
        elif enemyX[i] > 736:
            enemyX_change[i]= -0.3
            enemyY[i] += enemyY_change[i]
        
        #Collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            collision_sound= mixer.Sound('explosion.wav')
            collision_sound.play()
            collision_sound.set_volume(0.8)
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i]= random.randint(0,735)
            enemyY[i]= random.randint(50,150)
            
        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY<=0:
        bulletY = 480
        bullet_state= "ready"


    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        

    player(playerX, playerY)
    show_score(textX, textY)
    

    pygame.display.update()



