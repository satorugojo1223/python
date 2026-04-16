import pygame
import random
import math
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_X_START = 370
PLAYER_Y_START = 380
EMEMY_START_Y_MIN = 50
EMEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 20
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

background = pygame.image.load("backgroundspace.png")

playerimg = pygame.image.load("player.png")
playerx = PLAYER_X_START
playery  = PLAYER_Y_START
playerx_change = 0

def player(x,y):
    screen.blit(playerimg,(x,y))

enemyImg = []
enemyX = []
enemyY = []
enemyX_CHANGE = []
enemyY_CHANGE = []
num_of_enemys = 6

for _i in range(num_of_enemys):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,SCREEN_WIDTH-64))
    enemyY.append(random.randint(EMEMY_START_Y_MIN,EMEMY_START_Y_MAX))
    enemyX_CHANGE.append(ENEMY_SPEED_X)
    enemyY_CHANGE.append(ENEMY_SPEED_Y)
#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

def show_score(x,y):
    score = font.render("Score :" +str(score_value), True,(255,255,255))
    screen.blit(score,(x,y))
overfont = pygame.font.Font('freesansbold.ttf',64)

def game_over_text():
    game_over_text = font.render("GAME OVER HAHA" +str(score_value), True,(255,255,255))
    screen.blit(game_over_text,(200,250))

#see da enemy
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

#bullet
bulletimg = pygame.image.load("bullet.png")
bulletx = 0
bullety = BULLET_SPEED_Y
bulletx_change = 0
bullety_change = BULLET_SPEED_Y
bullet_state = "ready"

def fire_bullet(x,y):
    bullet_state = "fire"
    screen.blit(bulletimg,(x + 16, y +10))

def isCollision(enemyX,enemyY,bulletx,bullety):
    distance = math.sqrt((enemyX-bulletx) **2 + (enemyY-bullety)**2)
    return distance < COLLISION_DISTANCE

running = "True"
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletx = playerx
                bullet_state = "fire"
                fire_bullet(bulletx,bullety)
            if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
                playerx_change = 0
    playerx += playerx_change
    playerx - max(0,min(playerx,SCREEN_WIDTH-64))

    for i in range(num_of_enemys):
        if enemyY[i] > 340:
            for j in range (num_of_enemys):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_CHANGE[i]
        if enemyX[i] <=0 or enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_CHANGE[i] *= -1
            enemyY[i] += enemyY_CHANGE[i]

        if isCollision(enemyX[i],enemyY[i],bulletx,bullety):
            bullety = PLAYER_X_START
            bullet_state = "ready"
            score_value +=1
            enemyX[i] = random.randint(0,SCREEN_WIDTH -64)
            enemyY[i] = random.randint(EMEMY_START_Y_MIN,EMEMY_START_Y_MAX)

        enemy(enemyX[i],enemyY[i],i)


    if bullety <= 0:
        bullety = PLAYER_Y_START
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletx,bullety)
        bullety -= bullety_change
    player(playerx,playery)
    show_score(10,10)
    pygame.display.flip()