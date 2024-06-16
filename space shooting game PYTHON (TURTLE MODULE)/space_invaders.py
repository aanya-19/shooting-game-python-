import turtle
import time
import math
import random

delay=0.1

wn=turtle.Screen()
wn.title("SPACE INVADERS BY @AANYA")
wn.bgcolor("black")
# wn.bgpic("https://giphy.com/gifs/94P1LEMyuVEeA")
wn.tracer(0)
wn.setup(width=900,height=600)

#register shapes
turtle.register_shape("/Users/aanyasingh/Desktop/space shooting game PYTHON (TURTLE MODULE)/invader.gif")
turtle.register_shape("/Users/aanyasingh/Desktop/space shooting game PYTHON (TURTLE MODULE)/player.gif")


#white border
pen=turtle.Turtle()
pen.speed(0)
pen.up()
pen.color("white")
pen.pensize(3)
pen.setposition(-405,-245)
pen.down()
pen.fd(800)
pen.lt(90)
pen.fd(500)
pen.lt(90)
pen.fd(800)
pen.lt(90)
pen.fd(500)
pen.lt(90)
pen.hideturtle()

sc=0
# hsc=0

#player turtle
player=turtle.Turtle()
player.penup()
player.speed(0)
player.color("blue")
player.shape("/Users/aanyasingh/Desktop/space shooting game PYTHON (TURTLE MODULE)/player.gif")
player.setposition(0,-220)
player.setheading(90)
player.shapesize(1.4,1.4)
player.direction="stop"

score=turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("SCORE:0", align="center", font=("Courier",30,"normal"))

game_ov=turtle.Turtle()
game_ov.speed(0)
game_ov.shape("square")
game_ov.color("white")
game_ov.penup()
game_ov.hideturtle()
game_ov.goto(0,0)
# game_ov.write("GAME OVER !!", align="center", font=("Courier",30,"normal"))
#enemy
# enemy=turtle.Turtle()
# enemy.speed(0)
# enemy.penup()
# enemy.color("red")
# enemy.shape("triangle")
# enemy.setposition(-170,235)
# enemy.shapesize(1.3,1.3)
# enemy.rt(90)


#bullet
bullet=turtle.Turtle()
bullet.speed(0)
bullet.up()
bullet.color("yellow")
bullet.shape("square")
bullet.shapesize(0.9,0.2)
bullet.setposition(0,0)
bullet.hideturtle()
bulletstate="ready"
bulletspeed=20

#enemies
total_enemies=5
enemies=[]
for i in range(total_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:  
    enemy.speed(0)
    enemy.penup()
    enemy.color("red")
    enemy.shape("/Users/aanyasingh/Desktop/space shooting game PYTHON (TURTLE MODULE)/invader.gif")
    x=random.randint(-260,260)
    y=random.randint(100,250)
    enemy.setposition(x,y)
    enemy.shapesize(1.3,1.3)
    enemy.rt(90)
    
  
def move():
    if player.direction=="left":
        x=player.xcor()
        if x<-370:
            x=-370
        player.setx(x-17)
        
    if player.direction=="right":
        x=player.xcor()
        if x>360:
            x=360
        player.setx(x+17)
  
def go_left():
    player.direction="left"

def go_right():
    player.direction="right"
def fire():
    
    global bulletstate
    if bulletstate=="ready":
      bulletstate="fire"
      x=player.xcor()
      y=player.ycor()
      bullet.setpos(x,y+20)
      bullet.showturtle()
      
def iscollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor() - t2.ycor(),2))
    if distance<30:
        return True
    else:
        return False
    
    
#keyboard 
wn.listen()
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")
wn.onkeypress(fire,"space")
enemyspeed=6


while True:
    wn.update()
    
    for enemy in enemies:
      x=enemy.xcor()
      x+=enemyspeed
      enemy.setx(x)
      
      if x>360:
        for enemy in enemies:
          y=enemy.ycor()
          enemy.sety(y-25)
        enemyspeed*=-1 
        
      if x<-370:
        for enemy in enemies:
         y=enemy.ycor()
         enemy.sety(y-25)
        enemyspeed*=-1
                
      if iscollision(bullet,enemy):
        bullet.hideturtle()
        bulletstate="ready"
        bullet.setposition(0,-500)
        # enemy.setpos(1000,1000)
        x=random.randint(-260,260)
        y=random.randint(100,190)
        enemy.setposition(x, y)
        sc=sc+10
        score.clear()
        score.write("SCORE:{} ".format(sc),align="center", font=("Courier",30,"normal"))   
           
      if iscollision(player,enemy):
         player.hideturtle()
         bullet.hideturtle()
         for enemy in enemies:
          enemy.hideturtle()
         score.clear()
         game_ov.write("GAME OVER !!", align="center", font=("Courier",30,"normal"))
        #  if onclick=="Enter":
        #      break
        #  enemy.hideturtle()
        
        
    # if len(enemies)==0:
        
        
    y=bullet.ycor()
    bullet.sety(y+35)
    y=bullet.ycor()
    if y>260:
        bulletstate="ready"
        bullet.hideturtle()
     
    move()
    
    time.sleep(delay)
    
wn.mainloop()