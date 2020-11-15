"""
This programm paints a regular Star!
"""
import turtle
import math
import typing as ty


Point = ty.Tuple[float, float]


def find_points(radius: int, vertices_count: int) -> ty.List[Point]:
    """
    Calculates
    coordinates of vertices
    of a regular polygon with
    a Radius equal to Radius and number
    of vertices equal to vertices_count
    (= of a star). Returns list with coords.
    """
    points: ty.List[Point] = []
    # Central Angle between two nearest vertices
    central_angle = 2 * math.pi / vertices_count
    # Calculating the coords
    for i in range(vertices_count):
        axis = -radius * math.sin(central_angle * i)
        ordinate = radius * math.cos(central_angle * i)
        points.append((axis, ordinate))
    return points


def make_star_odd(vertices_count: int, vertices_points: ty.List[Point]) -> None:
    """
    Paints a star if the number
    of the vertices is odd.
    """
    vertex = step = vertices_count // 2
    while vertex != 0:
        turtle.goto(*vertices_points[vertex])
        vertex += step
        if vertex >= vertices_count:
            vertex -= vertices_count
    turtle.goto(*vertices_points[vertex])


def make_star_div_4(vertices_count: int, vertices_points: ty.List[Point]) -> None:
    """
    Paints a star if
    `vertices_count % 4 == 0`.
    """
    vertex = step = (vertices_count - 1) // 2
    while vertex != 0:
        turtle.goto(*vertices_points[vertex])
        vertex += step
        if vertex >= vertices_count:
            vertex -= vertices_count
    turtle.goto(*vertices_points[vertex])


def make_star_notdiv_4(vertices_count: int, vertices_points: ty.List[Point]) -> None:
    """
    Paints a star if
    `vertices_count % 2 == 0` and
    `vertices_count % 4 != 0`
    """
    vertex = step = (vertices_count - 1) // 2  
    while vertex != 0:  # The first part of the star
        turtle.goto(*vertices_points[vertex])
        vertex += (vertices_count - 1) // 2
        if vertex >= vertices_count:
            vertex -= vertices_count
    turtle.goto(*vertices_points[vertex])
    # Go to the "bottom point"
    turtle.penup()
    turtle.goto(vertices_points[0][0], -vertices_points[0][1])
    turtle.pendown()
    # The second part of the star
    vertex = (vertices_count - 1) // 2
    while vertex != 0:
        turtle.goto(-vertices_points[vertex][0], -vertices_points[vertex][1])
        vertex += step
        if vertex >= vertices_count:
            vertex -= vertices_count
    turtle.goto(-vertices_points[vertex][0], -vertices_points[vertex][1])


def decide_what_to_paint() -> None:
    """
    Asks user which star to paint.
    """
    print("Hello! I can paint n-sided regular star!")
    print("Pls, point out the number of the sides:")
    vertices_count = int(input())
    while vertices_count < 5:
        print("pls, input number > 4")
        vertices_count = int(input())

    radius = 300
    vertices_points = find_points(radius, vertices_count)

    turtle.penup()
    turtle.goto(*vertices_points[0])
    turtle.pendown()

    if vertices_count % 2 != 0:
        make_star_odd(vertices_count, vertices_points)
    elif vertices_count % 4 == 0:
        make_star_div_4(vertices_count, vertices_points)
    else:
        make_star_notdiv_4(vertices_count, vertices_points)

if __name__ == "__main__":
    decide_what_to_paint()
