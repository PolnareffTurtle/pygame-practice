import pygame
import os 

BASE_PATH = 'current_game/graphics/'

def load_image(image_path,alpha=False):
    if alpha:
        return pygame.image.load(BASE_PATH + image_path).convert_alpha()
    return pygame.image.load(BASE_PATH + image_path).convert()

def load_images(folder_path,alpha=False):
    images = []
    for image_name in sorted(os.listdir(BASE_PATH+folder_path)):
        if image_name == '.DS_Store':
            continue
        images.append(load_image(folder_path + '/' + image_name,alpha))
    return images

