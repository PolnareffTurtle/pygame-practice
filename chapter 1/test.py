import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

surf = pygame.surface.Surface((300,400))
surf.fill((255,255,255))
dogs = pygame.image.load('dogs.jpeg')
test_font = pygame.font.Font(None,30)
dogs_text = test_font.render('I love dogs!!!',False,'red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0,0,0))
    screen.blit(dogs,(0,0))
    screen.blit(surf, (400, 100))
    screen.blit(dogs_text,(300,300))

    pygame.display.update()
    clock.tick(60)

