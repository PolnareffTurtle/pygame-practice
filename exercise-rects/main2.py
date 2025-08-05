import pygame
from sys import exit

class Game:
    GAME_MENU = 0
    GAME_RUNNING = 1
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()
        self.game_state = Game.GAME_RUNNING
        
    def game_running(self):
        floor_rect = pygame.Rect((0, 0, self.screen.get_width(), 30))
        floor_rect.bottom = self.screen.get_height()
        player_rect = pygame.Rect((0, 50, 200, 300))
        player_rect.bottom = floor_rect.top
        enemy_rect = pygame.Rect((self.screen.get_width(), 0, 100, 100))
        enemy_rect.bottom = floor_rect.top
    
        self.new_font = pygame.font.Font(None, 50)
        y_velocity = 0
        movement = [False, False]
        self.points = 0
        self.is_collided = False

        while self.game_state == Game.GAME_RUNNING:
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
    
            self.screen.fill('white')

            # first move player horizontally to check for collisions + points
            player_rect.x += 10*(movement[1] - movement[0])
            if player_rect.colliderect(enemy_rect):
                self.game_state = Game.GAME_MENU
                continue
    
            # then move player down vertically to check collisions + points
            y_velocity += 1
            player_rect.y += y_velocity
            if player_rect.colliderect(enemy_rect):
                enemy_rect.left = self.screen.get_width() + 1
                self.points+=1
    
    
    
            if player_rect.bottom > floor_rect.top:
                y_velocity = 0
                player_rect.bottom = floor_rect.top
            if player_rect.left < 0:
                player_rect.left = 0
            if player_rect.right >self.screen.get_width():
                player_rect.right =self.screen.get_width()
    
            enemy_rect.x -= 5
            if enemy_rect.right < 0:
                enemy_rect.left =self.screen.get_width()
    
    
    
            points_text = self.new_font.render(f'Points: {self.points}',True,'black')
            self.screen.blit(points_text,(50,50))
    
            pygame.draw.rect(self.screen,'green',floor_rect)
            pygame.draw.rect(self.screen,'blue',player_rect)
            pygame.draw.rect(self.screen,'red',enemy_rect)
    
            pygame.display.update()
            self.clock.tick(60)
    
    def game_menu(self):
        while self.game_state == Game.GAME_MENU:
            self.screen.fill('yellow')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.game_state = Game.GAME_RUNNING

            pygame.display.update()
            self.clock.tick(60)

    def run(self):
        while True:
            if self.game_state == Game.GAME_RUNNING:
                self.game_running()
            if self.game_state == Game.GAME_MENU:
                self.game_menu()

if __name__ == '__main__':
    game = Game()
    game.run()
