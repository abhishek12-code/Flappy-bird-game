import pygame as pg
import random

class Pipe(pg.sprite.Sprite):
    def __init__(self,last_pipe_right,position,last_pipe_bottom=None):
        super(Pipe,self).__init__()
        
        self.gap=200
        if position==1:
            self.image=pg.transform.scale(pg.transform.flip(pg.image.load("pipe.png"),False, True),(80,500))
            self.rect=self.image.get_rect()
            self.rect.top=random.randint(-400,0)
        else:
            self.image=pg.transform.scale(pg.image.load("pipe.png"),(80,500))
            self.rect=self.image.get_rect()
            self.rect.top=last_pipe_bottom+self.gap
        self.rect.left=last_pipe_right+180
           
    