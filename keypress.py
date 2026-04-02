import pygame
pygame.init()
x = 100
y = 100
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("MY FIRST EVER HOLOLOW PURPLE")

done = False
while not done:
    screen.fill("white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        press = pygame.key.get_pressed()
        if press[pygame.K_UP]:
            y = y-10
        if press[pygame.K_DOWN]:
            y = y+10
        if press[pygame.K_LEFT]:
            x = x-10
        if press[pygame.K_RIGHT]:
            x = x+10 
    pygame.draw.rect(screen,'black',pygame.Rect(x,y,30,30))
    pygame.display.flip()