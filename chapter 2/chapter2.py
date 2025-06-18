import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200,800))
clock = pygame.time.Clock()

cloud = pygame.image.load('clouds.jpg').convert()
floor = pygame.image.load('floor.jpeg').convert()
floor_rect = floor.get_rect(bottomleft=(0,800))
goomba = pygame.image.load('goomba.png').convert_alpha()
goomba_rect = goomba.get_rect(bottomleft=(1200,floor_rect.top))
mario = pygame.image.load('mario.png').convert_alpha()
mario_rect = mario.get_rect(bottomleft=(200,floor_rect.top))
goomba_xpos = 1500

test_font = pygame.font.Font(None,50)


surf = pygame.surface.Surface((400,200))
surf.fill('#98FB98')
goomba_collisions = 0
mouse_collisions = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(cloud,(0,0)) # rgb tuples, strings, hex codes
    screen.blit(floor, floor_rect)
    goomba_text = test_font.render(f'Goomba collisions: {goomba_collisions}', False, 'white')
    mouse_text = test_font.render(f'Mouse collisions: {mouse_collisions}', False, 'white')
    #screen.blit(goomba_text,(400,400))
    #screen.blit(mouse_text,(400,450))

    goomba_rect.x-=4
    mouse_pos = pygame.mouse.get_pos()
    if goomba_rect.right < 0:
        goomba_rect.left = 1200
    if goomba_rect.colliderect(mario_rect):
        goomba_collisions +=1
    if mario_rect.collidepoint(mouse_pos):
        mouse_collisions+=1
    screen.blit(goomba,goomba_rect)
    screen.blit(mario, mario_rect)


    pygame.display.update()
    clock.tick(60)
