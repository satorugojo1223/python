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

background = pygame.image.load("thebg.jpg")

playerimg = pygame.image.load("rocka.png")
playerx = PLAYER_X_START
playery  = PLAYER_Y_START
playerx_change = 0

def player(x,y):
    screen.blit(playerimg,(x,y))

#bullet
bulletimg = pygame.image.load("bull.png")
bulletx = 0
bullety = BULLET_SPEED_Y
bulletx_change = 0
bullety_change = BULLET_SPEED_Y
bullet_state = "ready"

def fire_bullet(x,y):
    bullet_state = "fire"
    screen.blit(bulletimg,(x + 16, y +10))

running = "True"
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.quit:
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
            if event.type == pygame.KEYUP and event.key in [pygame.K_lEFT,pygame.K_RIGHT]:
                playerx_change = 0
    playerx += playerx_change
    playerx - max(0,min(playerx,SCREEN_WIDTH-64))
    if bullety <= 0:
        bullety = PLAYER_Y_START
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletx,bullety)
        bullety -= bullety_change
    player(playerx,playery)

    pygame.display.flip()