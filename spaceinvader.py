import pygame
import random

# Initialize pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader Project - Part 1")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Player setup
player = pygame.Rect(370, 480, 50, 50)

# Enemy setup (7 random enemies)
enemies = []
for i in range(7):
    x = random.randint(0, 750)
    y = random.randint(50, 300)
    enemies.append(pygame.Rect(x, y, 50, 50))

# Score
score = 0
font = pygame.font.Font(None, 36)

# Collision check
def check_collision():
    global score
    for enemy in enemies[:]:  # copy list to avoid iteration issues
        if player.colliderect(enemy):
            score += 1
            enemies.remove(enemy)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # 60 FPS
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.x < 750:
        player.x += 5
    
    # Collision
    check_collision()
    
    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, player)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
    
    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()

pygame.quit()
