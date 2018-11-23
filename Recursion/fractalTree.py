import turtle
import random


def tree(mt, branch_length):
    if branch_length > 1:
        mt.forward(branch_length)
        x = random.randrange(0, 45)
        mt.right(x)
        tree(mt, branch_length-20)
        y = random.randrange(0, 45)
        mt.left(x + y)
        tree(mt, branch_length-20)
        mt.right(y)
        mt.backward(branch_length)


def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()

    my_turtle.left(90)
    my_turtle.up()
    my_turtle.backward(150)
    my_turtle.down()
    my_turtle.color('green')

    tree(my_turtle, 100)
    my_win.exitonclick()


if __name__ == '__main__':
    main()
