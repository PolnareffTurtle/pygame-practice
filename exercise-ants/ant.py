import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

wood = pygame.image.load('wood.jpg').convert()
ant = pygame.image.load('ant.png').convert_alpha()
ant_rect = ant.get_rect(topleft=(0,0))
new_font = pygame.font.Font(None,50)
text = new_font.render('The ant is crawling on your mouse!',True,'white')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(wood,(0,0))


    mouse_vector = pygame.math.Vector2(pygame.mouse.get_pos())

    # checks if the mouse has not yet gone on the screen, defaults the ant to move towards the center
    if mouse_vector.length() == 0:
        mouse_vector = pygame.math.Vector2(screen.get_size())//2

    # checks if the mouse is close enough to the ant, it will reset the ant's position to (0,0)
    if (mouse_vector - pygame.math.Vector2(ant_rect.center)).length() < 3:
        ant_rect.center = (0,0)

    # directional vector from ant to mouse
    ant_vector = (mouse_vector-pygame.math.Vector2(ant_rect.center)).normalize()

    # moves the ant in x,y directions of ant_vector * 2
    ant_rect.x += ant_vector[0] * 2
    ant_rect.y += ant_vector[1] * 2

    # gets the angle from the vector; as_polar returns the vector in (radius,angle) form
    ant_angle = ant_vector.as_polar()[1]
    # creating a new surface: you have to use 270-ant_angle to make it face towards the mouse
    ant_rotated = pygame.transform.rotate(ant,270-ant_angle)
    # creating a new rect from the new surface, make sure that the center is still the same
    ant_rotated_rect = ant_rotated.get_rect(center=ant_rect.center)

    # if the ant is touching the mouse, blit the text
    if ant_rect.collidepoint(mouse_vector):
        screen.blit(text,(300,300))

    screen.blit(ant_rotated,ant_rotated_rect)

    pygame.display.update()
    clock.tick(60)
