import turtle
def rectangle (dino,a,b,he,wi):
    dino.up()
    dino.goto(a,b-100)
    dino.down()
    for i in range(2):
        dino.forward(wi)
        dino.right(90)
        dino.forward(he)
        dino.right(90)

win=turtle.Screen()
win.title("My dino")
my_dino=turtle.Turtle()
my_dino.fillcolor("pink")
my_dino.pensize(3)
my_dino.speed(10)
my_dino.color("pink")
my_dino.hideturtle()

my_dino.begin_fill()
rectangle(my_dino,0,250,10,100)
my_dino.end_fill()

my_dino.begin_fill()
rectangle(my_dino,-10,240,60,120)
my_dino.end_fill()

# eye
my_dino.fillcolor("white")
my_dino.begin_fill()
rectangle(my_dino,10,240,15,15)
my_dino.end_fill()

my_dino.fillcolor("pink")
my_dino.begin_fill()
rectangle(my_dino,-10,180,15,65)
my_dino.end_fill()

my_dino.begin_fill()
rectangle(my_dino,-10,165,7,100)
my_dino.end_fill()

my_dino.begin_fill()
rectangle(my_dino,-20,158,10,65)
my_dino.end_fill()

my_dino.begin_fill()
rectangle(my_dino,-30,148,10,75)
my_dino.end_fill()
# arm
my_dino.begin_fill()
rectangle(my_dino,-40,138,7,110)
my_dino.end_fill()
 
my_dino.begin_fill()
rectangle(my_dino,70,138,20,7)
my_dino.end_fill()

my_dino.begin_fill()
rectangle(my_dino,-50,128,10,95)
my_dino.end_fill()

my_dino.begin_fill()
rectangle(my_dino,-70,128,40,30)
my_dino.end_fill()

my_dino.begin_fill()
rectangle(my_dino,-80,138,50,10)
my_dino.end_fill()

my_dino.begin_fill()
rectangle(my_dino,-90,148,50,10)
my_dino.end_fill()

my_dino.begin_fill()
rectangle(my_dino,-100,168,60,10)
my_dino.end_fill()

my_dino.begin_fill()
rectangle(my_dino,-60,88,30,10)
my_dino.end_fill()

my_dino.begin_fill()
rectangle(my_dino,-50,118,20,95)
my_dino.end_fill()

#stomach
def stomach():
    y=98
    width=85
    for i in range (0,40,10):
        my_dino.begin_fill() 
        rectangle(my_dino,-50,y-i,10,width-i)
        my_dino.end_fill()
stomach()        


#left leg
my_dino.begin_fill()
rectangle(my_dino,-50,58,10,27)
my_dino.end_fill()

my_dino.begin_fill()
rectangle(my_dino,-50,48,10,20)
my_dino.end_fill()

my_dino.begin_fill()
rectangle(my_dino,-50,38,18,7)
my_dino.end_fill()

my_dino.begin_fill()
rectangle(my_dino,-50,18,7,25)
my_dino.end_fill()

# right leg
my_dino.begin_fill()
rectangle(my_dino,-8,58,10,13)
my_dino.end_fill()

my_dino.begin_fill()
rectangle(my_dino,-2,48,28,7)
my_dino.end_fill()

my_dino.begin_fill()
rectangle(my_dino,-2,20,7,25)
my_dino.end_fill()

my_dino.up()
my_dino.goto(0,-150)
my_dino.down()
my_dino.color("lightblue")
my_dino.write("I love you",align="center",font=("comic Sans MS", 50, "normal") )
win.exitonclick()

