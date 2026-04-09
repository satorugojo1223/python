import pygame
import random

pygame.init()

# Screen
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Simple Sprites")

# Custom event (change color)
CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)  # every 2 seconds

# Sprite positions
sprite1 = pygame.Rect(100, 150, 50, 50)
sprite2 = pygame.Rect(300, 150, 50, 50)

# Starting colors
color1 = (255, 0, 0)
color2 = (0, 0, 255)

running = True
while running:
    screen.fill((0, 0, 0))  # background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == CHANGE_COLOR:
            # Change to random colors
            color1 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            color2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    # Draw sprites
    pygame.draw.rect(screen, color1, sprite1)
    pygame.draw.rect(screen, color2, sprite2)

    pygame.display.update()

pygame.quit()