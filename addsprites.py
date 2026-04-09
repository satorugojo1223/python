import pygame

pygame.init()

# Screen
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Cursed Hands Game")

# Load image (put your image in same folder as 'bg.png')
bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (600, 400))

# Player
player = pygame.Rect(50, 180, 30, 30)
speed = 5

running = True
while running:
    screen.blit(bg, (0, 0))  # draw background

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

    # Draw player
    pygame.draw.rect(screen, (0, 255, 255), player)

    pygame.display.update()

pygame.quit()