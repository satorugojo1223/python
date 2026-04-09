import pygame

pygame.init()
SWIDTH = 500
SHEIGHT = 400
screen = pygame.display.set_mode((SWIDTH,SHEIGHT))
mspeed = 1
backgroung_image = pygame.transform.scale(pygame.image.load("Focus_Cherry.png"),(SWIDTH,SHEIGHT))
font = pygame.font.SysFont("Impact",72)
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,h,w):
        super().__init__()
        self.image = pygame.Surface([w,h])
        self.image.fill(color)
        self.rect=self.image.get_rect()
    def move(self,xchange,ychange):
        self.rect.x = max(min(self.rect.x +xchange,SWIDTH -self.rect.w),0)
        self.rect.y = max(min(self.rect.y +ychange,SHEIGHT -self.rect.h),0)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
Sprite1 = Sprite("green",20,20)
Sprite1.rect.x = 200
Sprite1.rect.y = 200
all_sprites.add(Sprite1)

Sprite2= Sprite("Red",20,20)
Sprite2.rect.x = 100
Sprite2.rect.y = 50
all_sprites.add(Sprite2)

while True :
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    keys = pygame.key.get_pressed()

    xchange = (keys[pygame.K_RIGHT]-keys[pygame.K_LEFT]) *mspeed
    ychange = (keys[pygame.K_UP]-keys[pygame.K_DOWN]) *mspeed
    Sprite1.move(xchange,ychange)
    screen.blit(backgroung_image,(0,0))
    all_sprites.draw(screen)
    if Sprite1.rect.colliderect(Sprite2.rect):
        win_text = font.render("you win!",True,pygame.Color('purple'))
        screen.blit(win_text,(200,200))
        all_sprites.remove(Sprite2)
    pygame.display.flip()
    clock.tick(90)