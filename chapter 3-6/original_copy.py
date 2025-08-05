import pygame
from sys import exit
from random import randint
from scripts.enums import GameState
from scripts.entities import Player, Enemy

class Game:
    ENEMY_SPAWN_EVENT = pygame.USEREVENT + 1

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()
        self.game_state = GameState.GAME_RUNNING
        self.total_time = 0
        pygame.time.set_timer(Game.ENEMY_SPAWN_EVENT,1000) # every 1 second the event triggers
        
    def game_running(self):
        self.floor_rect = pygame.Rect((0, 0, self.screen.get_width(), 30))
        self.floor_rect.bottom = self.screen.get_height()

    
        self.new_font = pygame.font.Font(None, 50)
        movement = [False, False]
        self.points = 0

        self.enemy_list = []

        start_ticks = pygame.time.get_ticks()

        animation_index = 0

        self.player = Player(self)

        while self.game_state == GameState.GAME_RUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == Game.ENEMY_SPAWN_EVENT:
                    self.enemy_list.append(Enemy(self))
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_SPACE,pygame.K_UP]:
                        self.player.jump()
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
            pygame.draw.rect(self.screen,'green',self.floor_rect)

            self.player.update(movement[1]-movement[0])
            self.player.render(self.screen)

            self.enemy_list = [enemy for enemy in self.enemy_list if not enemy.update()]
            for enemy in self.enemy_list:
                enemy.render(self.screen)

            if self.game_state != GameState.GAME_RUNNING:
                continue
    
            self.seconds = (pygame.time.get_ticks() - start_ticks) / 1000
            seconds_text = self.new_font.render(f'Time: {self.seconds}',True,'black')
            self.screen.blit(seconds_text,(self.screen.get_width()-250,50))
            points_text = self.new_font.render(f'Points: {self.points}',True,'black')
            self.screen.blit(points_text,(50,50))
    
            pygame.display.update()
            self.clock.tick(60)
    
    def game_menu(self):
        while self.game_state == GameState.GAME_MENU:
            self.screen.fill('yellow')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.game_state = GameState.GAME_RUNNING

            seconds_text = self.new_font.render(f'Time: {self.seconds}',True,'black')
            self.screen.blit(seconds_text,(200,200))
            points_text = self.new_font.render(f'Points: {self.points}',True,'black')
            self.screen.blit(points_text,(200,400))
            pygame.display.update()
            self.clock.tick(60)

    def run(self):
        while True:
            if self.game_state == GameState.GAME_RUNNING:
                self.game_running()
            if self.game_state == GameState.GAME_MENU:
                self.game_menu()

if __name__ == '__main__':
    game = Game()
    game.run()
