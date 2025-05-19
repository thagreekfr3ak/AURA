
from random import randint
import pygame


#dictionaries used for animating and keeping track of enemies

boom_animate_frames={0:(2,1/2),1:(-.75,-.75),2:(1/2,-1),3:(1.75,-.75),4:(-.75,1.75),5:(1/2,2),6:(1.75,1.75),7:(-1,1/2),8:(2,1/2),9:(2,2),10:(-1,1),11:(2,1)}
char_animate_frames={7:(1,7,1,11,12,11),4:(1,7,1,11,12,11),9:(1,7,1,11,12,11),0:(2,8,2,13,14,13),8:(2,8,2,13,14,13),6:(2,8,2,13,14,13),10:(3,9,3,3,3,),1:(3,9,3,3,3,3),2:(3,9,3,3,3,3),3:(4,10,4,4,4,4),11:(4,10,4,4,4,4),5:(5,6,5,13,14,13)}
attack_animate_frames={0:(1,1),1:(14,15),2:(14,15),3:(12,13),4:(10,11),5:(8,9),6:(8,9),7:(6,7),8:(4,5),9:(2,2),10:(3,3),11:(16,16)}

#button presss
from pygame.locals import (K_w,K_d,K_a,K_s,K_ESCAPE,KEYDOWN,QUIT,K_SPACE,K_RETURN)

#defining variables


charfat=60
screenwide=700
screenhigh=700
screen = pygame.display.set_mode([screenwide,screenhigh])

#importing images
spritesheet=pygame.image.load("allmovekaboo.png")
grassheet=pygame.image.load("dungeonbg.png")
shotgunsheet=pygame.image.load("realkaboom.png")
slimesheet=pygame.image.load("realslimeenemy.png")
explode=pygame.image.load("bigboom.png")
heart=pygame.image.load("hearts.png")
dead=pygame.image.load("ded.png")
titletext=pygame.image.load("titlekaboom.png")
pressenter=pygame.image.load("pressentertoplay.png")
playagain=pygame.image.load("playagainbutton.png")
key=pygame.image.load("key.png")
lockeddoor=pygame.image.load("lockeddoor.png")
#basic functions

def screenchangedub(dir):
    """
    sets values for screen changing if charector hits door
    arg dir wich direction to screenchange
    returns none
    """
    global locks
    global enemyspawn
    global change
    global changebg
    change=dir
    changebg=dir
    enemyspawn=1
    locks=1

                 
            

def getimage(pic,strwidth,strheight,width,height,scale,bordcol):
    """
    takes image and makes it a sprite also can pick what part of the image too use(spritesheets)
    args the image file, starting width in the file where to put the bottom right(width,height) scale of the image and color to remove
    returns the new image
    """
    image=pygame.Surface((width,height)).convert_alpha()
    image.blit(pic, (0,0),(strwidth,0,width,height))
    image=pygame.transform.scale(image,(width*scale,height*scale))
    image.set_colorkey(bordcol) 
    return image

#define classes

class Background(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            global grimg
            self.image=grimg
            self.surf = pygame.Surface((screenwide*3,screenhigh*3))
            self.surf.fill((0,0,0))
            self.rect =self.surf.get_rect(center=(screenwide/2,screenhigh/2))
        
                       
        def screenchange(self):
            """
            if called moves background
            no args
            returns none
            """
            global changebg
            global horcount
            global vertcount
            if changebg==1:
                self.rect.move_ip(10,0)
                horcount+=10
                if horcount==screenwide:
                     changebg=0
                     horcount=0
            if changebg==2:
                self.rect.move_ip(-10,0)
                horcount+=10
                if horcount==screenwide:
                     changebg=0
                     horcount=0
            if changebg==3:
                self.rect.move_ip(0,10)
                vertcount+=10
                if vertcount==screenhigh:
                     changebg=0
                     vertcount=0
            if changebg==4:
                self.rect.move_ip(0,-10)
                vertcount+=10
                if vertcount==screenhigh:
                     changebg=0
                     vertcount=0
class Doorlock(pygame.sprite.Sprite):
        def __init__(self,side):
            pygame.sprite.Sprite.__init__(self)
            global inv
            global lockeddoor
            global enemycounter
            global currentroom
            global changebg
            global screenwide
            global screenhigh
            if side=="left" and currentroom not in (1,4,7):
                
                self.surf=pygame.surface.Surface((screenwide/10,screenhigh/5))
                self.rect=self.surf.get_rect()
                self.rect.left=0
                self.rect.top=screenhigh/10*4
                self.image=getimage(lockeddoor,128,0,128,256,.6,"white")
            if side=="right"and currentroom not in (3,6,9):
                
                self.surf=pygame.surface.Surface((screenwide/10,screenhigh/5))
                self.rect=self.surf.get_rect()
                self.rect.right=screenwide
                self.rect.top=screenhigh/10*4
                self.image=getimage(lockeddoor,0,0,128,256,.6,"white")
            if side=="top" and currentroom not in (1,2,3):
                
                self.surf=pygame.surface.Surface((screenwide/5,screenhigh/10))
                self.rect=self.surf.get_rect()
                self.rect.left=screenwide/10*4
                self.rect.top=0
                self.image=getimage(lockeddoor,256,128,256,128,.6,"white")
            if side=="bottom"and currentroom not in (7,8,9):
                
                self.surf=pygame.surface.Surface((screenwide/5,screenhigh/10))
                self.rect=self.surf.get_rect()
                self.rect.left=screenwide/10*4
                self.rect.bottom=screenhigh
                self.image=getimage(lockeddoor,256,0,256,128,.6,"white")
                
        def remove(self):
            if changebg!=0:
                self.kill()
            
            
class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.char = pygame.surface.Surface((charfat,charfat))
            self.rect = self.char.get_rect(center=(screenwide/2,screenhigh/2))
        def die(self):
             """
             if player touches an enemy helath -1 and causes knockback
             no args
             returns none
             """
             global iframes
             global health
             global enemies
             global tookhit
             global x,y
             global shoot_count
             knock=30
             if iframes>0:
                    iframes+=1
             if iframes==60:
                    iframes=0
                    
             for enemy in enemies:
            
                
            
                if pygame.Rect.colliderect(self.rect,enemy) and iframes==0:
                     tookhit=True
                     health-=1
                     iframes=1
                     x=0
                     y=0
                     
                     if self.rect.bottom-charfat/3>=enemy.rect.bottom:
                        y=knock
                     elif self.rect.top+charfat/3<=enemy.rect.top:
                        y=-knock
                     if self.rect.right-charfat/3>=enemy.rect.right:
                        x=knock
                     elif self.rect.left+charfat/3<=enemy.rect.left:
                        x=-knock
             if iframes>0:
                if iframes<2:
                    self.rect.move_ip(x,y)
                elif iframes<6:
                    self.rect.move_ip(x/10,y/10)
             if iframes>=10:
                  tookhit=False
                     
                
                
        def shotgun(self):
            """
            animates shotgun and craeates rect for damge
            no args
            returns true if shooting
            """
            global shooty
            global img
            global char_animate_frames
            global move
            global change
            global shoot_count
            global stored_shot
            global storedmove
            global tookhit
            global bullets
            if changebg!=0 or tookhit:
                 shooty=False
                 shoot_count=0
                 stored_shot=False
                 bullets.rect=bullets.surf.get_rect(center=(-500,-500))
            if changebg==0:
                if shoot_count==35:
                    if not stored_shot:
                        shooty=False
                    else:
                        move=storedmove
                        stored_shot=False
                    shoot_count=0
                if pressed_keys[K_SPACE] and shoot_count==0 and change==0:
                    shooty=True
                if shooty:
                    shoot_count+=1
                
                snum=shoot_count//6-6
                if snum==0:
                    snum=0
                
                if shoot_count>=7 and shoot_count<=9:
                    knock=30
                    if move==1:
                        self.rect.move_ip(knock,knock)
                    if move==2:
                            self.rect.move_ip(0,knock)
                    if move==3:
                            self.rect.move_ip(-knock,knock)
                    if move==4:
                            self.rect.move_ip(knock,-knock)
                    if move==5:
                            self.rect.move_ip(0,-knock)
                    if move==6:
                            self.rect.move_ip(-knock,-knock)
                    if move==7:
                            self.rect.move_ip(knock,0)
                    if move==8 or move==0:
                    
                            self.rect.move_ip(-knock,0)
            
                if shoot_count>=1:
                    img=getimage(shotgunsheet,(char_animate_frames[move][snum]-1)*32,0,32,32,2,"white")
                    self.image=img
                    
                    return True
            
              
                
            
        def animate(self):
            """
            animates walking
            no args
            returns current animation
            """
            global ancount
            global movean
            global spritesheet
            global img
            img=getimage(spritesheet,(attack_animate_frames[movean][ancount//3]-1)*32,0,32,32,2,"white")
            self.image=img
            
        def currentscreenchange(self):
            """
            causes charecter to move with wasd and causes screen change
            args pressed keys
            returns none
            """
            global move
            global movean
            global change
            global background
            if change!=0:
                if change==1:
                    self.rect.move_ip(10,0)
                    if self.rect.right>=screenwide:
                        self.rect.right=screenwide
                        change=0
                if change==2:
                    self.rect.move_ip(-10,0)
                    if self.rect.left<=0:
                        self.rect.left=0
                        change=0
                if change==3:
                    self.rect.move_ip(0,10)
                    if self.rect.bottom>=screenhigh:
                        self.rect.bottom=screenhigh
                        change=0
                if change==4:
                    self.rect.move_ip(0,-10)
                    if self.rect.top<=0:
                        self.rect.top=0
                        change=0
        def movement(self,pressed_keys):
            global move
            global movean
            global change
            global background
            if changebg==0:
                if pressed_keys[K_w]:
                        if pressed_keys[K_d] or pressed_keys[K_a]:
                            self.rect.move_ip(0, -4)
                        else:
                            self.rect.move_ip(0, -5)
                        movean=2
                        move=movean
                if pressed_keys[K_s]:
                        if pressed_keys[K_d] or pressed_keys[K_a]:
                            self.rect.move_ip(0, 4)
                        else:
                             self.rect.move_ip(0, 5)
                        movean=5
                        move=movean
                if pressed_keys[K_a]:
                        if pressed_keys[K_w] or pressed_keys[K_s]:
                            self.rect.move_ip(-4, 0)
                            movean-=1
                        else:
                            self.rect.move_ip(-5, 0)
                            movean=7
                        move=movean    
                if pressed_keys[K_d]:
                        if pressed_keys[K_w] or pressed_keys[K_s]:
                            self.rect.move_ip(4, 0)
                            movean+=1
                        else:
                            self.rect.move_ip(5, 0)
                            movean=8
                        move=movean 
        def screeninitiate(self):
                """
                initiates a screenchange if you hit a door and stops player from going off screen
                no args
                returns true if hit a door
                """
                global currentroom
                global move
                global movean
                global change
                global background
                if change==0:
                    if self.rect.right>screenwide and self.rect.top<screenhigh/2-1.5*charfat or self.rect.right>screenwide and self.rect.bottom>screenhigh/2+1.5*charfat or self.rect.right>screenwide and background.rect.right==screenwide:
                            self.rect.right=screenwide
                    if self.rect.left < 0 and self.rect.top<screenhigh/2-1.5*charfat or self.rect.left < 0 and self.rect.bottom>screenhigh/2+1.5*charfat or self.rect.left < 0 and background.rect.left==0:
                            self.rect.left=0   
                    if self.rect.top<0 and self.rect.left<screenwide/2-1.5*charfat or self.rect.top<0 and self.rect.right>screenwide/2+1.5*charfat or self.rect.top < 0 and background.rect.top==0:
                            self.rect.top=0
                    if self.rect.bottom>screenhigh and self.rect.left<screenwide/2-1.5*charfat or self.rect.bottom>screenhigh and self.rect.right>screenwide/2+1.5*charfat or self.rect.bottom>screenhigh and background.rect.bottom==screenhigh:
                            self.rect.bottom=screenhigh
            


                if self.rect.top<0 or self.rect.bottom>screenhigh or self.rect.right>screenwide or self.rect.left<0:
                        if self.rect.left < 0:
                            self.rect.left=0
                            screenchangedub(1)
                            currentroom-=1
                        if self.rect.right>screenwide:
                            self.rect.right=screenwide
                            screenchangedub(2)
                            currentroom+=1
                        if self.rect.top<0:
                            self.rect.top=0
                            screenchangedub(3)
                            currentroom-=3
                        if self.rect.bottom>screenhigh:
                            self.rect.bottom=screenhigh
                            screenchangedub(4)  
                            currentroom+=3

class Bullet(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.surf=pygame.surface.Surface((charfat,charfat))
        def shoot(self):
            global boom_location
            global player
            global shoot_count
            global move
            global boom_animate
            global tookhit
            if shoot_count==6:
                 boom_location=(player.rect.left+boom_animate_frames[move][0]*charfat,player.rect.top+boom_animate_frames[move][1]*charfat)
                 self.rect=self.surf.get_rect(center=boom_location)
            
            if shoot_count>=18:
                 self.rect=self.surf.get_rect(center=(-500,-500))
            
            self.image=getimage(explode,0,0,128,128,.5,"white")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
            global currentroom
            pygame.sprite.Sprite.__init__(self)
            self.surf=pygame.surface.Surface((charfat,charfat))
            spawncenter=randint(charfat,screenwide-charfat*2),randint(charfat,screenhigh-charfat*2)
            if currentroom==5:
                while spawncenter[0] in range(250,450) and spawncenter[1] in range(250,450):
                    
                    spawncenter=randint(charfat,screenwide-charfat),randint(charfat,screenhigh-charfat)
                    
            
            self.rect=self.surf.get_rect(center=spawncenter)
            self.surf.fill((0,0,0))
    def animate(self):
         global ancount
         if self.move_dir in (1,2,3):
              frames=(3,4)
         else:
              frames=(1,2)
         imageanimate=frames[ancount//3]-1
         animated=getimage(slimesheet,imageanimate*64,0,64,64,1,"white")
         self.image=animated
    def die(self):
        global changebg
        global currentroom
        global bullets
        global enemycounter
        if changebg>0:
             self.kill()

        try:
            if self.rect.colliderect(bullets.rect):
                self.kill()
                enemycounter[currentroom][0]-=1
                #add new animation here
        except:
             pass 
    def move(self):
        movespeed=2
        diagnolmod=.75
        dir_change=randint(1,50)
        if dir_change==50:
            self.move_dir=randint(0,8)
        if self.move_dir==1:
             self.rect.move_ip(-movespeed*diagnolmod,-movespeed*diagnolmod)
        if self.move_dir==2:
             self.rect.move_ip(0,-movespeed)
        if self.move_dir==3:
             self.rect.move_ip(movespeed*diagnolmod,-movespeed*diagnolmod)
        if self.move_dir==4:
             self.rect.move_ip(-movespeed*diagnolmod,movespeed*diagnolmod)
        if self.move_dir==5:
             self.rect.move_ip(0,movespeed)
        if self.move_dir==6:
             self.rect.move_ip(movespeed,movespeed*diagnolmod)
        if self.move_dir==7:
             self.rect.move_ip(-movespeed,0)
        if self.move_dir==8:
             self.rect.move_ip(movespeed,0)
    def wallstop(self):
        if self.rect.right>screenwide:
            self.rect.right=screenwide
            self.move_dir=7
        if self.rect.left < 0:
            self.rect.left=0 
            self.move_dir=8  
        if self.rect.top<0:
            self.rect.top=0
            self.move_dir=5
        if self.rect.bottom>screenhigh:
            self.rect.bottom=screenhigh
            self.move_dir=2
    
class Pickupitem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf=pygame.surface.Surface((charfat/2,charfat/2))
    def place(self,x,y,picture):
        self.rect=self.surf.get_rect(center=(x,y))
        self.image=picture
    def collected(self,name):
        global player
        if pygame.Rect.colliderect(player.rect,self.rect):
             inv.append(name)
             self.kill()


                
youdied=False                 
game=True               
title=True    
pygame.init()

while game:
    for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key== K_ESCAPE:
                    game=False
            elif event.type == QUIT:
                    game = False
        

    #background and time variables and constant images
    inv=[]
    y=0
    x=0
    storedmove=8
    stored_shot=False
    tookhit=False
    locks=1
    enemycounter={0:[3,"open"],1:[3,"open"],2:[3,"open"],3:[0,"locked","chariott"],4:[3,"open"],5:[3,"open"],6:[3,"open"],7:[3,"open"],8:[3,"open"],9:[3,"open"]}
    move=0
    boom_animate=0
    shooty=False
    shoot_count=0
    ancount=0
    movean=0
    enemyspawn=1
    currentroom=5
    iframes=0
    screendist=75
    health=3
    clock = pygame.time.Clock()
    FPS = 40
    changebg=0
    change=0
    dstitle=getimage(titletext,0,0,954,79,.733,"black")
    grimg=getimage(grassheet,0,0,2880,2880,.7291,"white")
    hearts=getimage(heart,0,0,16,16,4,"white")
    emptyhearts=getimage(heart,16,0,16,16,4,"white")
    keypic=getimage(key,0,0,64,64,.5,"white")
    #create player background and enemies
    background=Background()
    playergroup=pygame.sprite.Group()
    enemies=pygame.sprite.Group()
    projectiles=pygame.sprite.Group()
    keys=pygame.sprite.Group()
    lockgroup=pygame.sprite.Group()

    bullets=Bullet()

    player=Player()
    projectiles.add(bullets)
    playergroup.add(player)
    key1=Pickupitem()
    keys.add(key1)
    horcount=0
    vertcount=0

    #titlescreen
    
    while title:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key== K_ESCAPE:
                    title=False
                    
            elif event.type == QUIT:
                    title = False

        screen.fill((0,0,0))
        clock.tick(FPS)
        screen.blit(dstitle,(0,50))
        screen.blit(pressenter,(240,500))
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_RETURN]:
            play=True
            title=False
        pygame.display.flip()

    #game loop

    while play:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key== K_ESCAPE:
                    play=False
                    game=False
            elif event.type == QUIT:
                    play = False
                    game=False
        
        if health<=0:
            break
        
        clock.tick(FPS)
        pressed_keys = pygame.key.get_pressed()
        if changebg==0 and locks==1:
            locks=0
            try:
                if enemycounter[currentroom-1][1]==("locked")and currentroom not in (1,4,7):
                    lockleft=Doorlock("left")
                    lockleft.add(lockgroup)
            except:
                continue
            try:    
                if enemycounter[currentroom+1][1]==("locked")and currentroom not in (3,6,9):
                    lockright=Doorlock("right")
                    lockright.add(lockgroup)
                    
            except:
                continue
            try:
                if enemycounter[currentroom-3][1]==("locked")and currentroom not in (1,2,3):
                    locktop=Doorlock("top")
                    lockgroup.add(locktop)
            except:
                continue
            try:
                if enemycounter[currentroom+3][1]==("locked")and currentroom not in (7,8,9):
                    lockbottom=Doorlock("bottom")
                    lockgroup.add(lockbottom)
            except:
                continue
        
        #create enemies
        if enemyspawn==1 and changebg==0:
            enemyspawn=0
            if enemycounter[currentroom][0]==3:
                slime1=Enemy()
                slime2=Enemy()
                slime3=Enemy()
                enemies.add(slime1,slime2,slime3)
            if enemycounter[currentroom][0]==2:
                slime1=Enemy()
                slime2=Enemy()
                enemies.add(slime1,slime2)
            if enemycounter[currentroom][0]==1:
                slime1=Enemy()
                enemies.add(slime1)
            for enemy in enemies:
                enemy.move_dir=0

            for lock in lockgroup:
                continue



        if changebg==0:
            player.die()
        
        attack=player.shotgun()  

        if movean==3:
            movean=11
        if movean==1 or movean==2:
            movean=10
        if movean==4 or movean==7:
            movean=9
        if movean==6 or movean==8:
            movean=0
        if movean==5:
            movean=0
    
        

        # place sprites
        hit_door=player.screeninitiate()
        background.screenchange()
        player.currentscreenchange()

        for enemy in enemies:
                enemy.die()
                enemy.move()
                enemy.wallstop()
                enemy.animate()
        
        #if your not attacking animate walking 
        if not attack and not tookhit and changebg==0:

            player.movement(pressed_keys)
            player.animate()
        
        #place background and player
        screen.blit(grimg,background.rect)
        lockgroup.update()
        for lock in lockgroup:
            lock.remove()
        if len(lockgroup)>0:
            lockgroup.draw(screen)
        playergroup.update()
        if iframes<10 or ancount<4:            
            playergroup.draw(screen)

        enemies.update()
        enemies.draw(screen)
        if currentroom==7 and enemycounter[currentroom][0]==0:
            
            key1.place(350,350,keypic)
            key1.collected("key1")
            keys.update()
            keys.draw(screen)
            

        #stores space bar input and direction
        if shoot_count>6 and shoot_count<36:
                    if pressed_keys[K_w]:
                            storedmove=2
                    if pressed_keys[K_s]:
                            storedmove=5     
                    if pressed_keys[K_a]:
                            if pressed_keys[K_w] or pressed_keys[K_s]:
                                storedmove-=1
                            else:
                                storedmove=7
                    if pressed_keys[K_d]:
                            if pressed_keys[K_w] or pressed_keys[K_s]:
                                storedmove+=1
                            else:
                                storedmove=8 
                    if shoot_count>12 and shoot_count<36:
                        if pressed_keys[K_SPACE]:
                            stored_shot=True

        if attack and shoot_count>=6 and shoot_count<=18:
            bullets.shoot()
            projectiles.update()
            projectiles.draw(screen)
        if health==1:
            screen.blit(hearts,(screenwide-screendist*3,screenhigh-screendist))
            screen.blit(emptyhearts,(screenwide-screendist*2,screenhigh-screendist))
            screen.blit(emptyhearts,(screenwide-screendist*1,screenhigh-screendist))
        if health==2:
            screen.blit(hearts,(screenwide-screendist*3,screenhigh-screendist))
            screen.blit(hearts,(screenwide-screendist*2,screenhigh-screendist))
            screen.blit(emptyhearts,(screenwide-screendist*1,screenhigh-screendist))
        if health==3:
            screen.blit(hearts,(screenwide-screendist*3,screenhigh-screendist))
            screen.blit(hearts,(screenwide-screendist*2,screenhigh-screendist))
            screen.blit(hearts,(screenwide-screendist*1,screenhigh-screendist))
        #incrument the animation counter 
        ancount+=1
        if ancount==6:
            ancount=0
        pygame.display.flip()
    if health<=0:
        youdied=True
    while youdied:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key== K_ESCAPE:
                    youdied=False
                    play=False
                    game=False
            elif event.type == QUIT:
                    youdied = False
                    play=False
                    game=False
        clock.tick(FPS)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_RETURN]:
            play=True
            youdied=False
            title=False
            
        screen.fill((0,0,0))
        screen.blit(dead,(200,200))
        screen.blit(playagain,(160,500))

        pygame.display.flip()




pygame.quit()