import pygame

pygame.init()

# Screen
screen = pygame.display.set_mode((600, 400))

# Load image (save your image as bg.png)
bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (600, 400))

# Player
player = pygame.Rect(50, 50, 30, 30)

# Item to collect
item = pygame.Rect(400, 200, 20, 20)

speed = 5
score = 0

running = True
while running:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    # Collision (collect item)
    if player.colliderect(item):
        score = 1  # collected!

    # Draw
    pygame.draw.rect(screen, (0, 255, 255), player)
    if score == 0:
        pygame.draw.rect(screen, (255, 255, 0), item)

    pygame.display.update()

pygame.quit()