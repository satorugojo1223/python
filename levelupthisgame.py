import pygame
import random

pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader - No Assets")

# Player
player_x = 370
player_y = 500
player_speed = 0

# Stars (background effect)
stars = []
for _ in range(80):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    speed = random.randint(1, 3)
    stars.append([x, y, speed])

running = True
while running:
    screen.fill((5, 5, 20))  # dark space color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed = -5
            if event.key == pygame.K_RIGHT:
                player_speed = 5

        if event.type == pygame.KEYUP:
            player_speed = 0

    player_x += player_speed

    # Keep player inside screen
    if player_x < 0:
        player_x = 0
    if player_x > 740:
        player_x = 740

    # Draw stars (moving background)
    for star in stars:
        pygame.draw.circle(screen, (255, 255, 255), (star[0], star[1]), 2)
        star[1] += star[2]
        if star[1] > 600:
            star[1] = 0
            star[0] = random.randint(0, 800)

    # Draw player (spaceship using shapes)
    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, 60, 20))
    pygame.draw.polygon(screen, (0, 200, 0), [
        (player_x, player_y),
        (player_x + 30, player_y - 20),
        (player_x + 60, player_y)
    ])

    pygame.display.update()

pygame.quit()