import pygame
import os 

BASE_PATH = 'graphics/'



def load_image(image_path,alpha=False,scale=1):
    if alpha:
        img = pygame.image.load(BASE_PATH + image_path).convert_alpha()
        return pygame.transform.scale_by(img,scale)
    img = pygame.image.load(BASE_PATH + image_path).convert()
    return pygame.transform.scale_by(img,scale)

def load_images(folder_path,alpha=False,scale=1):
    images = []
    for image_name in sorted(os.listdir(BASE_PATH+folder_path)):
        if image_name == '.DS_Store':
            continue
        images.append(load_image(folder_path + '/' + image_name,alpha,scale))
    return images

class Animation:
    def __init__(self,images,img_duration,loop=True):
        self.images = images
        self.img_dur = img_duration
        self.loop = loop
        self.frame = 0
        self.done = False
    
    def update(self):
        if self.loop:
            self.frame = (self.frame+1) % (self.img_dur * len(self.images))
        else:
            self.frame = min(self.frame+1, self.img_dur * len(self.images) - 1)
            if self.frame >= self.img_dur * len(self.images) - 1:
                self.done = True
    
    def img(self):
        frame_index = int(self.frame // self.img_dur)
        if frame_index >= len(self.images): 
            frame_index = len(self.images) - 1
        return self.images[frame_index]

    def copy(self):
        return Animation(self.images,self.img_dur,self.loop)

class Text:
    def __init__(self, text: str, color, size: int, font=None):
        self.text = text
        self.font = pygame.font.Font(font,size)
        self.image = self.font.render(text,True,color)

    def render(self,surf,pos: tuple[int,int]):
        surf.blit(self.image,pos)
