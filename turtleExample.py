import math
import turtle as tr

tr.hideturtle()
tr.delay(0)
tr.pensize(4)

def set_cursor(x, y):
    tr.up()
    tr.setpos(x, y)
    tr.down()

def main():
    for i in range(1, 3000):
        tr.setpos(((i / 100) * 55 - 500), 55 * math.sin(i / 100))

set_cursor(-500, 0)

main()

tr.exitonclick()

