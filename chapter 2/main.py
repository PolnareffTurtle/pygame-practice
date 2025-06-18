import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption('mario game practice')
clock = pygame.time.Clock()

clouds = pygame.image.load('clouds.jpg').convert()
floor = pygame.image.load('floor.jpeg').convert()
floor_rect = floor.get_rect(bottomleft=(0,800))
goomba = pygame.image.load('goomba.png').convert_alpha()
goomba_rect = goomba.get_rect(bottomleft=(1200,floor_rect.top))
mario = pygame.image.load('mario.png').convert_alpha()
mario_rect = mario.get_rect(bottomleft=(200,floor_rect.top))

new_font = pygame.font.Font(None,50)
goomba_collisions = 0
mouse_collisions = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(clouds, (0, 0))

    pygame.Rect(120,120,120,120)

    goomba_text = new_font.render(f'goomba collisions: {goomba_collisions}',True,'white')
    mouse_text = new_font.render(f'mouse colllisions: {mouse_collisions}',True,'white')

    goomba_rect.x -= 5
    if goomba_rect.right < 0:
        goomba_rect.left = 1200

    screen.blit(goomba_text,(400,400))
    screen.blit(mouse_text,(400,450))
    screen.blit(floor,floor_rect)
    screen.blit(mario,mario_rect)
    screen.blit(goomba,goomba_rect)

    mouse_pos = pygame.mouse.get_pos()

    if mario_rect.colliderect(goomba_rect):
        goomba_collisions+=1
        print('goomba collided')
    if mario_rect.collidepoint(mouse_pos):
        mouse_collisions+=1
        print('mouse collided')


    clock.tick(60)
    pygame.display.update()
