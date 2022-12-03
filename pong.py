import turtle

PIXLE_SIZE = 20
BALL_SPEED = PIXLE_SIZE/10
DIFF = 2

score_a=0
score_b=0

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=800)
window.tracer(0)

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=1, stretch_wid=4)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1, stretch_wid=4)
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.moveCount = 60

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = 2
ball.dy = 2

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto (0, 360)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


def a_up():
    if paddle_a.ycor()+PIXLE_SIZE+40 <= 400:
        paddle_a.sety(paddle_a.ycor()+PIXLE_SIZE)
def a_down():
    if paddle_a.ycor()-PIXLE_SIZE-40 >= -400:
        paddle_a.sety(paddle_a.ycor()-PIXLE_SIZE)

def cpu_move():
    if paddle_b.moveCount == 0:
        if ball.ycor() < paddle_b.ycor():
            if paddle_b.ycor()-PIXLE_SIZE-40 >= -400:
                paddle_b.sety(paddle_b.ycor()-PIXLE_SIZE)
        elif ball.ycor() > paddle_b.ycor():
            if paddle_b.ycor()+PIXLE_SIZE+40 <= 400:
                paddle_b.sety(paddle_b.ycor()+PIXLE_SIZE)
        
        paddle_b.moveCount = 8
    else:
        paddle_b.moveCount -= 1

def write_score(a=0,b=0):
    pen.clear()
    pen.write("Player A: {} Player B: {}".format(a,b), align="center", font=("Courier", 24, "normal"))

window.listen()
window.onkeypress(a_up, "w")
window.onkeypress(a_down, "s")

while (1):
    window.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor() >= 390:
        ball.sety(390)
        ball.dy *= -1
    if ball.ycor() <= -390:
        ball.sety(-390)
        ball.dy *= -1
    if ball.xcor() >= 390:
        ball.goto(0,0)
        ball.dx *= -1
        ball.dy *= -1
        score_a += 10
        write_score(a=score_a,b=score_b)
    if ball.xcor() <= -390:
        ball.goto(0,0)
        ball.dx *= -1
        ball.dy *= -1
        score_b += 10
        write_score(a=score_a,b=score_b)
    
    if (ball.xcor() < -350 and ball.xcor() > -360) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-350)
        ball.dx *= -1
    if (ball.xcor() > 350 and ball.xcor() < 360) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(350)
        ball.dx *= -1
    cpu_move()