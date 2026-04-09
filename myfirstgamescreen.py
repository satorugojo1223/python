import pygame

pygame.init()

# Screen
screen = pygame.display.set_mode((600, 400))

# Load your image (save as bg.png)
bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (600, 400))

# Player
player = pygame.Rect(50, 200, 30, 30)
speed = 5

# Goal area (right side)
goal = pygame.Rect(500, 0, 100, 400)

running = True
win = False

while running:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not win:
        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= speed
        if keys[pygame.K_RIGHT]:
            player.x += speed
        if keys[pygame.K_UP]:
            player.y -= speed
        if keys[pygame.K_DOWN]:
            player.y += speed

        # Check win
        if player.colliderect(goal):
            win = True

    # Draw player
    pygame.draw.rect(screen, (0, 255, 255), player)

    pygame.display.update()

pygame.quit()