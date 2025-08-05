import pygame
from sys import exit
import enum

class GameState(enum.Enum):
    GAME_RUNNING = 0
    MENU = 1

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()
        self.game_state = GameState.MENU
        self.new_font = pygame.font.Font(None, 50)
        self.points = 0

    def menu(self):
        menu_text = self.new_font.render('MENU',True,'black')
        points_text = self.new_font.render(f'Points: {self.points}',True,'black')
        space_text = self.new_font.render('Press SPACE to play',True,'black')
        while self.game_state == GameState.MENU:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.game_state = GameState.GAME_RUNNING

            self.screen.fill((255,255,255))
            pygame.draw.rect(self.screen,'lightblue',pygame.Rect(100,100,1000,600))
            self.screen.blit(menu_text,(640,360))
            self.screen.blit(points_text,(600,410))
            self.screen.blit(space_text,(600,self.screen.get_height()-100))



            pygame.display.update()
            self.clock.tick(60)



    def game_running(self):
        self.floor_rect = pygame.Rect((0,0,self.screen.get_width(),30))
        self.floor_rect.bottom = self.screen.get_height()
        self.player_rect = pygame.Rect((0,0,200,300))
        self.player_rect.bottom = self.floor_rect.top
        self.enemy_rect = pygame.Rect((0,0,100,100))
        self.enemy_rect.bottomleft = (self.screen.get_width(),self.floor_rect.top)


        self.y_velocity = 0
        self.movement = [False,False]
        self.points = 0
        self.is_collided = False

        while self.game_state == GameState.GAME_RUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_SPACE,pygame.K_UP]:
                        if self.y_velocity == 0:
                            self.y_velocity = -25
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            self.screen.fill('white')

            # first move player horizontally to check for collisions + points
            self.player_rect.x += 10*(self.movement[1] - self.movement[0])
            if self.player_rect.colliderect(self.enemy_rect):
                self.game_state = GameState.MENU
                break
                # self.player_rect.topleft = (0,100)
                # self.enemy_rect.left = self.screen.get_width() + 1
                # self.points-=1

            # then move player down vertically to check collisions + points
            self.y_velocity += 1
            self.player_rect.y += self.y_velocity
            if self.player_rect.colliderect(self.enemy_rect):
                self.enemy_rect.left = self.screen.get_width() + 1
                self.points+=1



            if self.player_rect.bottom > self.floor_rect.top:
                self.y_velocity = 0
                self.player_rect.bottom = self.floor_rect.top
            if self.player_rect.left < 0:
                self.player_rect.left = 0
            if self.player_rect.right > self.screen.get_width():
                self.player_rect.right = self.screen.get_width()

            self.enemy_rect.x -= 5
            if self.enemy_rect.right < 0:
                self.enemy_rect.left = self.screen.get_width()



            points_text = self.new_font.render(f'Points: {self.points}',True,'black')
            self.screen.blit(points_text,(50,50))

            pygame.draw.rect(self.screen,'green',self.floor_rect)
            pygame.draw.rect(self.screen,'blue',self.player_rect)
            pygame.draw.rect(self.screen,'red',self.enemy_rect)

            pygame.display.update()
            self.clock.tick(60)

    def run(self):
        while True:
            if self.game_state == GameState.GAME_RUNNING:
                self.game_running()
            if self.game_state == GameState.MENU:
                self.menu()

if __name__ == '__main__':
    game = Game()
    game.run()