import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

floor_rect = pygame.Rect((0,0,screen.get_width(),30))
floor_rect.bottom = screen.get_height()
player_rect = pygame.Rect((0,0,200,300))
player_rect.bottom = floor_rect.top
enemy_rect = pygame.Rect((0,0,100,100))
enemy_rect.bottom = floor_rect.top

new_font = pygame.font.Font(None,50)
y_velocity = 0
movement = [False,False]
points = 0
is_collided = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_SPACE,pygame.K_UP]:
                if y_velocity == 0:
                    y_velocity = -25
            if event.key == pygame.K_LEFT:
                movement[0] = True
            if event.key == pygame.K_RIGHT:
                movement[1] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                movement[0] = False
            if event.key == pygame.K_RIGHT:
                movement[1] = False

    screen.fill('white')



    # first move player horizontally to check for collisions + points
    player_rect.x += 10*(movement[1] - movement[0])
    if player_rect.colliderect(enemy_rect):
        player_rect.topleft = (0,100)
        enemy_rect.left = screen.get_width() + 1
        points-=1

    # then move player down vertically to check collisions + points
    y_velocity += 1
    player_rect.y += y_velocity
    if player_rect.colliderect(enemy_rect):
        enemy_rect.left = screen.get_width() + 1
        points+=1
    

    
    if player_rect.bottom > floor_rect.top:
        y_velocity = 0
        player_rect.bottom = floor_rect.top
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > screen.get_width():
        player_rect.right = screen.get_width()

    enemy_rect.x -= 5
    if enemy_rect.right < 0:
        enemy_rect.left = screen.get_width()
    
    

    points_text = new_font.render(f'Points: {points}',True,'black')
    screen.blit(points_text,(50,50))

    pygame.draw.rect(screen,'green',floor_rect)
    pygame.draw.rect(screen,'blue',player_rect)
    pygame.draw.rect(screen,'red',enemy_rect)

    pygame.display.update()
    clock.tick(60)