import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("MY FIRST EVER HOLOLOW PURPLE")
screen.fill("purple")

pygame.draw.rect(screen,'orange',pygame.Rect(100,300,60,100))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        pygame.display.flip()