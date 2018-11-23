import turtle


def draw_spiral(mt, ll):
    if ll > 0:
        mt.forward(ll)
        mt.right(90)
        draw_spiral(mt, ll-10)


def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    line_length = 211

    my_turtle.up()
    my_turtle.backward(line_length // 2)
    my_turtle.left(90)
    my_turtle.backward(line_length // 2)
    my_turtle.down()

    draw_spiral(my_turtle, line_length)
    my_win.exitonclick()


if __name__ == '__main__':
    main()
