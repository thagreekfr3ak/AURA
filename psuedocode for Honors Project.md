#psuedocode for markdown
## Overview
this program
1. creates a screen with a backgrownd and redraws it each frame
2. creates a charector that can move with wasd and shoot with space
3. creates enemies that can deal contact damage and die to the gun
4. creates a death screen

### Functions:
```plaintext
DEFINE screenchange(dir of screenchange)
    change=dir
    changebg=dir
    enemyspawn=1
DEFINE getimage(img file, strwidth, width, height, scale, border color to remove)
    TAKES image file 
    CROPS it to desired size
    TRANSFORMS it
    REMOVES border color
```
### Classes:
```plaintext
CLASS Doorlock()
    DEFINE ___init___(self,side)
        CREATES surface rect and image depending on which side was passed
CLASS Background()
    DEFINE ___init___(self)
        CREATES surface and rect for background
    DEFINE screenchange()
        if called moves background
            no args
            returns none

CLASS Player()
    DEFINE ___init___(self)
        CREATES surface and rect for player charector
    DEFINE die(self)
        if touch enemy die
    DEFINE shotgun(self)
        if space pressed start shooting
        animate shooting
        cause knockback
    DEFINE animate(self)
        animate walking
    DEFINE currentscreenchange(self)
        if screenchange happening move to opposite side of screen
    DEFINE movement(self,pressed_keys)
        if wasd pressed move
    DEFINE screeninitiate(self)
        if touching edge of screen call screenchange

CLASS Bullet()
    DEFINE ___init___(self)
        CREATES surface and rect fo player projectiles
    DEFINE shoot(self)
        animates explosion/bullets when you shoot
        creates rect

CLASS Enemy()
    DEFINE ___init___(self)
        CREATES surface and rect for enemies
        in random location not ontop of player in first screen
    DEFINE animate(self)
        animates slime enemy for walking based on direction
    DEFINE die(self)
        if hits bullets self.kills from group
    DEFINE move(self)
        randomly moves around
    DEFINE wallstop(self)
        stops enemy from walking through walls or walking against a wall

CLASS Pickupitem()
    DEFINE __init__(self)
        creates a surface half the size of the charector
    DEFINE place(self,x,y,picture)
        places it at x,y and sets image arg to the picture
    DEFINE collected(self)
        if player touches it it gets removed and added to the inv list

```
# instructions
```plaintext
import login if login game
CREATE screen
IMPORT images
```

## overall loop
while Game True
DEFINE variables 
DEF how many enemies are in each room
CREATE inv list
CREATE images for title screen key hearts and background
CREATE GROUPS
playergroup 
enemies 
projectiles 
keys 
lockgroup 
CREATE player background key and hearts



## title screen
```plaintext
WHILE title true
    if escape or quit break
    if key pressed enter
    play=true
    title equals false
    screen blit title and press enter to play
```
## gameloop
```plaintext
while play
    if escape or quit play false
    GET button presses

    CREATE locks of doors depending on whih ones are locked
    
    DEF clock and fps

    CREATE enemies for room your in

    SET moving direction to idol

    INITIATE screenchange

    CALL classes of charector background

    CALL functions of these classes:
    player.die/attack/screenchange/move/animate
    background.screenchange
    enemies.move/animate/die/wallstop
    key.place/collect


    PLACE background then items/projectiles/locks then player

    STORE gunshot if in second half of current gun shot



    COUNT frames for animation
```
## gameover
```plaintext
WHILE died true
    if escape or quit break
    screen blit you died
    play again button
```