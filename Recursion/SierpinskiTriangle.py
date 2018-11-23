import turtle


def draw_triangle(points, color, mt):
    mt.fillcolor(color)
    mt.up()
    mt.goto(points[0][0], points[0][1])
    mt.down()
    mt.begin_fill()
    mt.goto(points[1][0], points[1][1])
    mt.goto(points[2][0], points[2][1])
    mt.goto(points[0][0], points[0][1])
    mt.end_fill()


def get_midpoint(point1, point2):
    return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]


def sierpinski(points, degree, mt):
    colormap = ['blue', 'green', 'orange', 'violet', 'red', 'white', 'yellow']
    draw_triangle(points, colormap[degree], mt)
    if degree > 0:
        sierpinski([
            points[0],
            get_midpoint(points[0], points[1]),
            get_midpoint(points[0], points[2])
        ], degree - 1, mt)

        sierpinski([
            get_midpoint(points[1], points[0]),
            points[1],
            get_midpoint(points[1], points[2])
        ], degree - 1, mt)

        sierpinski([
            get_midpoint(points[2], points[0]),
            get_midpoint(points[2], points[1]),
            points[2]
        ], degree - 1, mt)


def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_points = [[-100, -50], [0, 100], [100, -50]]
    sierpinski(my_points, 6, my_turtle)
    my_win.exitonclick()


if __name__ == '__main__':
    main()
