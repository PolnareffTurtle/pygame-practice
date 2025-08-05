import pygame
from scripts.enums import GameState
from random import randint

BASE_PATH = 'current_game/graphics/'

class Player:
    def __init__(self,game):
        self.game = game
        self.image = pygame.image.load(BASE_PATH + 'Player/walk/player_walk_1.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image,2)
        self.rect = self.image.get_rect(bottomleft = (0,self.game.floor_rect.top))
        self.y_velocity = 0

    def update(self,x_movement):
    # first move player horizontally to check for collisions + points
        self.rect.x += 10*x_movement
        for enemy in self.game.enemy_list:
            if self.rect.colliderect(enemy.rect):
                self.game.game_state = GameState.GAME_MENU
                break
    
    # then move player down vertically to check collisions + points
        self.y_velocity += 1
        self.rect.y += self.y_velocity
        for enemy in self.game.enemy_list:
            if self.rect.colliderect(enemy.rect):
                self.game.enemy_list.remove(enemy)
                self.game.points+=1
        
        if self.rect.bottom > self.game.floor_rect.top:
            self.y_velocity = 0
            self.rect.bottom = self.game.floor_rect.top
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > self.game.screen.get_width():
                self.rect.right = self.game.screen.get_width()

    def render(self,surf):
        surf.blit(self.image,self.rect)

    def jump(self):
        if self.y_velocity == 0:
            self.y_velocity = -25

class Enemy:
    def __init__(self,game):
        self.game = game
        self.image = pygame.image.load(BASE_PATH + 'snail/snail1.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image,2)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.game.screen.get_width()+randint(0,100),self.game.floor_rect.top)

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            return True     # remove all the enemies in game.enemy_list that return true
    
    def render(self,surf):
        surf.blit(self.image,self.rect)
