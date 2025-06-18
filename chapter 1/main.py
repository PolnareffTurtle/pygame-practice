import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200,800))
clock = pygame.time.Clock()

dog = pygame.image.load('dog.jpeg')
test_font = pygame.font.Font(None,50)
text_surf = test_font.render('I love dogs!',False,'#008080')

surf = pygame.surface.Surface((400,200))
surf.fill('#98FB98')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('black') # rgb tuples, strings, hex codes
    midwidth = screen.get_width()/2
    midheight = screen.get_height()/2

    screen.blit(dog,((midwidth-dog.get_width()/2),midheight-dog.get_height()/2))
    screen.blit(surf,(midwidth-surf.get_width()/2,midheight-surf.get_height()/2))
    screen.blit(text_surf,(midwidth-text_surf.get_width()/2,midheight-text_surf.get_height()/2))

    pygame.display.update()
    clock.tick(60)
