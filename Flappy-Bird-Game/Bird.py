import pygame as pg

class Bird(pg.sprite.Sprite):
    def __init__(self):
        super(Bird,self).__init__()
        self.imageIndex=0
        self.sprite_list=[pg.transform.scale(pg.image.load("birddown.png"),(40,30)),
        pg.transform.scale(pg.image.load("birdup.png"),(40,30))]
        self.image=self.sprite_list[self.imageIndex]
        self.rect=pg.Rect(100,340,70,50)
        self.velocity=pg.Vector2((0,0))
        self.gravity=30
        self.countdown=0

    def update(self,dt):
        cooldown=5
        if self.countdown>cooldown:
            self.countdown=0
            if self.imageIndex==0:
                self.imageIndex=1
                self.image=self.sprite_list[self.imageIndex]
            elif self.imageIndex==1:
                self.imageIndex=0
                self.image=self.sprite_list[self.imageIndex]
        else:
            self.countdown+=1

        self.velocity.y+=self.gravity*dt
        self.rect.y+=self.velocity.y

    def moveBird(self,dt):
        self.velocity.y-=80*dt
