import pygame
from sys import exit
from random import randint
from enum import Enum

class GameState(Enum):
    GAME_MENU = 0
    GAME_RUNNING = 1

class Game:
    ENEMY_SPAWN_EVENT = pygame.USEREVENT + 1

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()
        self.game_state = GameState.GAME_RUNNING
        self.total_time = 0
        pygame.time.set_timer(Game.ENEMY_SPAWN_EVENT,1000) # every 1 second the event triggers

    def enemy_spawn(self):
        enemy_rect = self.enemy_animation[0].get_rect()
        enemy_rect.bottomleft = (self.screen.get_width()+randint(0,100),self.screen.get_height()-30)
        self.enemy_list.append(enemy_rect)
    
    def enemy_update(self):
        for enemy_rect in self.enemy_list:
            enemy_rect.x -= 5
            if enemy_rect.right < 0:
                self.enemy_list.remove(enemy_rect)

    def enemy_render(self):
        for enemy_rect in self.enemy_list:
            #pygame.draw.rect(self.screen,'red',enemy_rect)
            self.screen.blit(self.enemy_animation[self.enemy_index],enemy_rect)
        
    def game_running(self):
        floor_rect = pygame.Rect((0, 0, self.screen.get_width(), 30))
        floor_rect.bottom = self.screen.get_height()
        player_image1 = pygame.image.load('chapter 3-6/graphics/Player/player_walk_1.png').convert_alpha()
        player_image1 = pygame.transform.scale_by(player_image1,2)
        player_image2 = pygame.image.load('chapter 3-6/graphics/Player/player_walk_2.png').convert_alpha()
        player_image2 = pygame.transform.scale_by(player_image2,2)
        self.enemy_animation = [pygame.image.load('chapter 3-6/graphics/snail/snail1.png').convert_alpha(),pygame.image.load('chapter 3-6/graphics/snail/snail2.png').convert_alpha()]
        self.enemy_animation = [pygame.transform.scale_by(enemy_image,2) for enemy_image in self.enemy_animation]
        self.enemy_index = 0
        
        self.player_animation = [player_image1,player_image2]
        self.player_animation_index = 0
        player_rect = player_image1.get_rect(bottomleft=(0,floor_rect.top))
        player_rect.bottom = floor_rect.top
    
        self.new_font = pygame.font.Font(None, 50)
        y_velocity = 0
        movement = [False, False]
        self.points = 0
        self.is_collided = False

        self.enemy_list = []

        start_ticks = pygame.time.get_ticks()

        animation_index = 0

        while self.game_state == GameState.GAME_RUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == Game.ENEMY_SPAWN_EVENT:
                    self.enemy_spawn()
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
            for enemy_rect in self.enemy_list:
                if player_rect.colliderect(enemy_rect):
                    self.game_state = GameState.GAME_MENU
                    self.total_time = seconds
                    break
            if self.game_state != GameState.GAME_RUNNING:
                continue
    
            # then move player down vertically to check collisions + points
            y_velocity += 1
            player_rect.y += y_velocity
            for enemy_rect in self.enemy_list:
                if player_rect.colliderect(enemy_rect):
                    self.enemy_list.remove(enemy_rect)
                    self.points+=1
    
    
    
            if player_rect.bottom > floor_rect.top:
                y_velocity = 0
                player_rect.bottom = floor_rect.top
            if player_rect.left < 0:
                player_rect.left = 0
            if player_rect.right >self.screen.get_width():
                player_rect.right =self.screen.get_width()
    

    
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000
            seconds_text = self.new_font.render(f'Time: {seconds}',True,'black')
            self.screen.blit(seconds_text,(self.screen.get_width()-250,50))
            
    
            points_text = self.new_font.render(f'Points: {self.points}',True,'black')
            self.screen.blit(points_text,(50,50))
    
            pygame.draw.rect(self.screen,'green',floor_rect)
            #pygame.draw.rect(self.screen,'blue',player_rect)
            self.screen.blit(self.player_animation[self.player_animation_index],player_rect)

            animation_index += 0.05
            
            self.player_animation_index = int(animation_index) % 2
            self.enemy_index = int(animation_index) % 2
            
            self.enemy_update()
            self.enemy_render()
    
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

            seconds_text = self.new_font.render(f'Time: {self.total_time}',True,'black')
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
