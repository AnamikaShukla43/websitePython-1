import numpy as np
import pygame, sys
import time
import random

from pygame.locals import * 
from tkinter import *
# thisis a simple pongame for one person. Left player uses a en z keys to move the left paddle and right
# player use  k en m keys to move right paddle each paddle bounce gives a point. with every bounce speed of the 
# ball increases with one. When ball goes beyond paddle player looses one life of start total of 3. With 3 game ends. 

pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()
screenWidth= 750
screenHeight= 500
counter = 0
# bijhouden van score dmv score variable
scoreLeftPaddle = 0
scoreRightPaddle = 0
buttonX=50
buttonY=50
x = 50
y = 50
paddle1X = 20
paddle1Y = 200
paddle2X = 710
paddle2Y = 200
paddleWidth = 20
paddleHeight = 100
# ball coordinates, size, speed
ballPosX  = 375 
ballPosY = 250
ballMovementX = 3
ballMovementY = 2
ballSize = 20
totalBouncesPaddles=0
livesLeft=3 
move = 5
vel = 5
run = True
#catImg = pygame.image.load('cat.png')
win = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Pong")

# myButton= Button(root, text="show dutch")
# myButton.pack()
# set up the colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
NAVYBLUE = ( 60, 60, 100)
YELLOW = (255, 255, 0)
button_color= BLUE



font = pygame.font.SysFont('comicsans', 40, True )


fontObj = pygame.font.Font('freesansbold.ttf', 32)
fontObj1 = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render("paddel", True, BLACK, YELLOW)
textSurfaceObj1 = fontObj1.render("paddel2", True, BLACK, YELLOW)

textRectObj = textSurfaceObj.get_rect()
textRectObj1 = textSurfaceObj1.get_rect()

textRectObj.center = (700, 150)
textRectObj1.center = (700, 400)


#soundObj = pygame.mixer.Sound('badswap.wav')
#soundObj.play()

#time.sleep(1) # wait and let the sound play for 1 second
#soundObj.stop()

direction="right"

while run:
    # mouse postion
    mouse = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
     
            
    if direction == "right":
        x = x+3
        if x > screenWidth - 100:
            #soundObj.play()
            direction = "down"
            counter+=1
            #print(counter)
            
        


    if direction == "down":
        y = y+3
        if y > screenHeight - 100:
            direction = "left"
            #counter += 1
            
    if direction == "left":
        x = x-3
        if x < 0 :
            direction="up"
            counter += 1
    if direction == "up":
        y = y - 3
        if y < 0:
            direction="right"


    
    keys = pygame.key.get_pressed()
    
    # movement of the paddles 
    # for the leftpaddle  keys a and z
    # for the rightpaddle  keys k and m  
    if keys[pygame.K_a]:
        paddle1Y-= move
        #paddle2Y-= move
    
    if keys[pygame.K_k]:
        #paddle1Y-= move
        paddle2Y-= move
   
    if keys[pygame.K_z]:
        paddle1Y += move
        #paddle2Y += move
    
    if keys[pygame.K_m]:
        #paddle1Y += move
        paddle2Y += move

    if paddle1Y < 0:
        paddle1Y = 0
    if paddle1Y  > screenHeight - paddleHeight:
        paddle1Y = screenHeight - paddleHeight
    if paddle2Y < 0:
        paddle2Y = 0
    if paddle2Y  > screenHeight - paddleHeight:
        paddle2Y = screenHeight - paddleHeight
    #if x > screen_width - 25 or x < 0:
    #    vel=-vel
    #if y > screen_height - 25 or y < 0:
    #    vel=-vel
    
    win.fill(NAVYBLUE)

    if mouse[0] > buttonX  and mouse[0] < buttonX + 25:
            if mouse[1]> buttonY and mouse[1] < buttonY + 25:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("fool")
                    textSurfaceObj1 = fontObj1.render("67", True, BLACK, YELLOW)
                    textRectObj1 = textSurfaceObj1.get_rect()
                    textRectObj1.center = (700, 400)
                    win.blit(textSurfaceObj1, textRectObj1)
                    button_color = YELLOW
                    print(counter)

    textSurfaceObj = fontObj.render("yes", True, BLACK, YELLOW)
    
    textRectObj = textSurfaceObj.get_rect()
   
    textRectObj.center = (700, 150)

    
    # drawing paddles
    pygame.draw.rect(win, WHITE , (paddle1X, paddle1Y, paddleWidth, paddleHeight))
    pygame.draw.rect(win, WHITE , (paddle2X, paddle2Y, paddleWidth, paddleHeight))
    
    # movement of the ball 
    ballPosX += ballMovementX
    ballPosY += ballMovementY
    
    if ballPosX > screenWidth - ballSize:
        # ballMovementX = - ballMovementX
        #restart ball in middle
        ballPosX  = 375 
        ballPosY = 250
        # loose one life
        livesLeft -=1
        #scoreLeftPaddle +=1
        #print(scoreLeftPaddle)
    if ballPosX < 0 + ballSize:
        #ballMovementX = - ballMovementX
        #restart ball in the middle
        ballPosX  = 375 
        ballPosY = 250
        #scoreRightPaddle += 1
        #print(scoreRightPaddle)
        livesLeft -= 1
    if livesLeft <= 0:
        run = False


    if ballPosY > screenHeight - ballSize:
        ballMovementY = - ballMovementY
    if ballPosY < 0 + ballSize:
        ballMovementY = - ballMovementY 
    
    # when ball hits paddle left
    if ballPosX < 20 + paddleWidth + ballSize and ballPosY + ballSize > paddle1Y  and ballPosY - ballSize < paddle1Y + paddleHeight:
        ballMovementX = - ballMovementX
        totalBouncesPaddles+=1
        #increase speed
        FPS +=2
    # when ball hits paddle right
    if ballPosX + ballSize > paddle2X and ballPosY + ballSize > paddle2Y and ballPosY - ballSize < paddle2Y + paddleHeight :
        ballMovementX = - ballMovementX
        totalBouncesPaddles += 1
        #increase speed
        FPS +=2
    # drawing ball
    pygame.draw.circle(win, YELLOW,(ballPosX,ballPosY), ballSize, 0)
    # draw score on the screen
    text = font.render('Score:' + str (totalBouncesPaddles), 1, (0,0,0) )
    textLivesLeft = font.render('Lives:' + str (livesLeft), 1, (0,0,0) )
    

    win.blit(textLivesLeft,(540,10))
    win.blit(text,(390,10))
    # win.blit(catImg, (x, y))
    win.blit(textSurfaceObj, textRectObj)
    
    pygame.display.update()
    # put the variable to true,  for the next loop 
    next_word = True
    button_color = BLUE
    #call the tick() method once per iteration through 
    #the game loop at the end of the loop
    fpsClock.tick(FPS)

pygame.quit()
sys.exit()


