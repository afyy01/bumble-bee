import pgzrun
from random import randint 

WIDTH = 800
HEIGHT = 600

Score = 0
Game_over = False

Bee = Actor("bee")
Bee.pos=100,100

Flower = Actor("flower")
Flower.pos=600,500

def draw():
    screen.blit("background",(0,0))
    Flower.draw()
    Bee.draw()
    screen.draw.text("Score: "+str(Score),color = "Red", topright = (500,30), fontsize = 60)

    if Game_over:
        screen.fill("Blue")
        screen.draw.text("Game over! Your final score is: "+str(Score),color = "White", midtop = (250,50), fontsize = 40)

def place_flower():
    Flower.x = randint(70,(WIDTH - 70))
    Flower.y = randint(70,(HEIGHT - 70))

def time_up():
    global Game_over 
    Game_over = True

def update():
    global Score
    if keyboard.left:
        Bee.x = Bee.x-2
    if keyboard.right:
        Bee.x = Bee.x+2
    if keyboard.up:
        Bee.y = Bee.y-2
    if keyboard.down:
        Bee.y = Bee.y+2
    
    Flower_collected = Bee.colliderect(Flower)

    if Flower_collected:
        Score = Score+10
        place_flower()

clock.schedule(time_up,10.0)
pgzrun.go()