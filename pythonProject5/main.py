import turtle
import random
score = 0

wn = turtle.Screen()
wn.setup(800, 600)
wn.bgcolor("black")
wn.title("Space Shooter")
wn.tracer(0)

# PEN score board
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 ", align="center", font=("Courier", 12, "normal"))


class Player():
    def __init__(self):
        self.color="red"
        self.x=-350
        self.y=0
        self.shape="triangle"
        self.dy = 0
        self.dx=0


    def up(self):
        self.dy = 0.6


    def down(self):
        self.dy = -0.6

    def left(self):
        self.dx=-0.4

    def right(self):
        self.dx=0.4


    def move(self):
        self.y=self.y+self.dy
        self.x=self.x+self.dx


        # Check for Border Collisions
        if self.y>290:
           self.y=290
           self.dy=0

        elif self.y<-290:
            self.y=-290
            self.dy=0

        if self.x<-390:
            self.x=-390
            self.dx=0

        elif self.x>-290:
            self.x=-290
            self.dx=0


    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.shapesize(0.3, 0.3, 0)

        pen.stamp()





class Missile():
    def __init__(self):
        self.color="yellow"
        self.x=0
        self.y=-340
        self.shape="circle"
        self.size=0.2
        self.dx = 0

    def fire(self):
        self.x=player.x
        self.y=player.y
        self.dx=0.9

    def move(self):
        self.x=self.x+self.dx

    def distance(self, other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()

class Enemy():
    def __init__(self):
        colors=["green", "gray", "blue", "white", "purple"]
        self.color=random.choice(colors)
        self.x=400
        self.y=random.randint(-290, 290)
        self.shape="square"
        self.dx = random.randint(1, 5)/-10
    def move(self):
        self.x=self.x+self.dx

        #Border Check
        if self.x<-400:
            self.x=400
            self.y=random.randint(-350, 350)
            self.dx *=1.2

    def distance(self, other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.shapesize(1, 1, 0)
        pen.stamp()

#Creating Gaming Objects
player = Player()
missile = Missile()

#Create multiple Enemies
enemies=[]
for _ in range(5):
    enemies.append(Enemy())




#Keyboard Binding
wn.listen()
wn.onkeypress(player.up, "Up")
wn.onkeypress(player.down, "Down")
wn.onkeypress(missile.fire,"space")
wn.onkeypress(player.right, "Right")
wn.onkeypress(player.left, "Left")



#Main Game Loop
while True:
    wn.update()
    pen.clear()
    player.move()
    missile.move()

    player.render(pen)
    missile.render(pen)


    for enemy in enemies:
        enemy.move()

        #Check for collision
        if enemy.distance(missile)<13:
            enemy.x=400
            enemy.y=random.randint(-350, 350)
            missile.dx=0
            missile.x=0
            missile.y=1000

            score += 10






        if enemy.distance(player)<20:
            print("Game Over!")
            print(score)
            exit()
        enemy.render(pen)


wn.mainloop()
