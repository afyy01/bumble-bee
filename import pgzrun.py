import pgzrun
from random import randint 

WIDTH = 600
HEIGHT = 500

Score = 0
Game_over = False

Ash = Actor("ash")
Ash.pos=100,100

Pikachu = Actor("pikachu")
Pikachu.pos=300,300

def draw():
    screen.blit("background",(0,0))
    Pikachu.draw()
    Ash.draw()

pgzrun.go()