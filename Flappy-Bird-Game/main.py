import sys
from playsound import playsound
import pygame as pg
from Bird import Bird
from Pipe import Pipe
import time 
pg.init()
WIDTH=500
HEIGHT=850
WIN=pg.display.set_mode((WIDTH,HEIGHT))
SCORE=0
start_monitor=False

clock=pg.time.Clock()
bg_img=pg.transform.scale(pg.image.load("bg.png"),(WIDTH,HEIGHT))
bg_rect=bg_img.get_rect()

base_img=pg.transform.scale(pg.image.load("base.png"),(WIDTH+23,167))
base_rect=base_img.get_rect()
base_rect.y=HEIGHT-167

font=pg.font.Font("arial.ttf",24)
label_score=font.render("Score: 0",(0,0,0),(0,0,0))
label_rect=label_score.get_rect()
label_rect.center=(60,10)

label_gameover=font.render("!! GAME OVER !!",(0,0,0),(255,0,0))
label_rect_gameover=label_gameover.get_rect()
label_rect_gameover.center=(250,650)

label_restart=font.render(" RESTART ",(0,0,0),(255,0,0))
label_rect_restart=label_restart.get_rect()
label_rect_restart.center=(250,750)

def playingSound():
    playsound("C:\\Users\\asus\\Downloads\Python Course with Notes\\gameover.wav")


def checkBirdCollision(bird_obj,pipes):
    if bird_obj.rect.y<0:
        bird_obj.velocity.y=0
    elif bird_obj.rect.y>=680:
        bird_obj.velocity.y=0
        bird_obj.gravity=0
        return True
    if bird_obj.rect.colliderect(pipes[0].rect) or bird_obj.rect.colliderect(pipes[1].rect):
        return True
    return False
     
def checkScore(bird_obj,pipe):
    global SCORE,start_monitor,label_score
    if start_monitor==False:
        if bird_obj.rect.left>pipe.rect.left and bird_obj.rect.right<pipe.rect.right:
            start_monitor=True
            # print(start_monitor)
    elif start_monitor==True:
        if bird_obj.rect.left>pipe.rect.right:
            start_monitor=False
            SCORE+=1
            label_score=font.render(f"Score: {SCORE}",(0,0,0),(0,0,0))
            
            
def main():
    global SCORE,start_monitor,label_score
    bird_obj=Bird()
    pipes_list=[]
    start_monitor=False
    SCORE=0
    game_over=False
    run=True
    label_score=font.render("Score: 0",(0,0,0),(0,0,0))
    last_time=time.time()
    while run:
        #Handling Events
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type==pg.MOUSEBUTTONDOWN and game_over==True:
                mousepos=event.pos
                if label_rect_restart.collidepoint(mousepos):
                    run=False

        #If game is not yet over then keep doing the stuff        
        if game_over==False:
            #Create Delta Time
            new_time=time.time()
            dt=new_time-last_time
            last_time=new_time

            #Condition for adding new pipes
            if len(pipes_list)==0:
                temp_list=[]
                temp_list.append(Pipe(500,1))
                temp_list.append(Pipe(500,-1,temp_list[0].rect.bottom))
                pipes_list.append(temp_list)
            elif len(pipes_list)<3:
                temp_list=[]
                temp_list.append(Pipe(pipes_list[-1][0].rect.right,1))
                temp_list.append(Pipe(pipes_list[-1][0].rect.right,-1,temp_list[0].rect.bottom))
                pipes_list.append(temp_list)

            #Getting Pressed Keys
            keys=pg.key.get_pressed()

            #MOVEMENT##############################################################
            #Moving the Bird
            if keys[pg.K_SPACE]:
                bird_obj.moveBird(dt)

            #Moving the pipes and checking for out of screen
            for pipes in pipes_list:
                pipes[0].rect.x-=50*dt
                pipes[1].rect.x-=50*dt
            if pipes_list[0][0].rect.left<=0:
                pipes_list.pop(0)


            #Moving the base
            if base_rect.x<=-23:
                base_rect.x=0
            else:
                base_rect.x-=150*dt
            
            #Checking the Collisions###################################################
            game_over=checkBirdCollision(bird_obj,pipes_list[0])

            #Checking the SCore
            checkScore(bird_obj,pipes_list[0][0])

            #Blitting everything on Screen###########################################
            WIN.blit(bg_img,bg_rect)

            for pipes in pipes_list:
                WIN.blit(pipes[0].image,pipes[0].rect)
                WIN.blit(pipes[1].image,pipes[1].rect)
                
            WIN.blit(base_img,base_rect)
            WIN.blit(label_score,label_rect)
            if game_over==True:
                WIN.blit(label_gameover,label_rect_gameover)
                playingSound()
            bird_obj.update(dt)
            WIN.blit(bird_obj.image,bird_obj.rect)

        elif game_over==True:
            WIN.blit(label_restart,label_rect_restart)


        pg.display.update()
        clock.tick(60)
    main()
main()