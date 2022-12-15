from __future__ import annotations
from typing import Tuple
import pygame
from sys import argv
import random
import time

from point import Point, cross_product, mapping_point
from slope import Slope

# Colors
point_color = (0, 0, 0)
hull_color = (246, 53, 220)
line_color = (146, 38, 253)
background_color = (255, 255, 255)


def initializer(name, points):
    pygame.init()
    window = pygame.display.set_mode((1500, 800))
    pygame.display.set_caption(name)

    # Changing background color
    window.fill(background_color)
    pygame.display.flip()

    # Plotting the plane
    for p in points:
        pygame.draw.circle(window, point_color, mapping_point(p), 5)
    pygame.display.update()
    return window


def jarvis_march(points):
    coords = []
    hull = []

    for p in points:
        coords.append([p.x, p.y])

    # get the start time
    st = time.process_time()

    # Find bottommost point, considering only y coordinate
    bottommost_y = min([coord[1] for coord in coords])
    bottommost_point = [p for p in points if bottommost_y is p.y][0]
    # pygame.draw.circle(window, hull_color, mapping_point(bottommost_point), 4)
    # pygame.display.update()

    # The first point in the hull
    current_point = bottommost_point

    while True:
        hull.append(current_point)
        next_point = points[(points.index(current_point) + 1) % len(points)]
        for check_point in points:
            # pygame.draw.line(window, (255, 0, 94), mapping_point(current_point), mapping_point(check_point), 1)
            # clock.tick(5)
            # pygame.display.update()
            if cross_product(current_point, next_point, check_point) < 0:  # clockwise
                next_point = check_point
        # pygame.draw.line(window, line_color, mapping_point(current_point), mapping_point(next_point), 4)
        # pygame.display.update()
        current_point = next_point
        if current_point == hull[0]:
            break

    # get the end time and execution time
    et = time.process_time()
    elapsed_time = et - st
    print('Execution time for Jarvis March algorithm is:\t', elapsed_time, 'seconds')

    return hull


def graham_scan(points):

    coords = []
    for p in points:
        coords.append([p.x, p.y])

    # get the start time
    st = time.process_time()

    # Find bottommost point, considering only y coordinate
    bottommost_y = min([coord[1] for coord in coords])
    bottommost_point = [p for p in points if bottommost_y is p.y][0]
    points.remove(bottommost_point)
    # pygame.draw.circle(window, hull_color, mapping_point(bottommost_point), 3)
    # pygame.display.update()

    # Sort by polar angle
    def key(p: Point) -> Tuple[Slope, int]:
        d = p - bottommost_point
        return Slope(d.x, d.y), d.len2()
    points.sort(key=key)

    stack = [bottommost_point]
    for p in points:
        # pygame.draw.line(window, (255, 0, 94), mapping_point(p), mapping_point(stack[-1]), 1)
        while len(stack) > 1 and cross_product(stack[-2], stack[-1], p) <= 0:  # if right turn
            # pygame.draw.line(window, (255, 255, 255), mapping_point(p), mapping_point(stack[-1]), 1)
            # clock.tick(5)
            # pygame.display.update()
            stack.pop()
            # point = stack.pop()
            # pygame.draw.line(window, (255, 255, 255), mapping_point(point), mapping_point(stack[-1]), 1)
            # clock.tick(5)
            # pygame.display.update()
            # pygame.draw.line(window, (255, 0, 94), mapping_point(p), mapping_point(stack[-1]), 1)
            # clock.tick(5)
            # pygame.display.update()
        stack.append(p)
        # ch_point = stack[-1]
        # pygame.draw.line(window, line_color, mapping_point(ch_point), mapping_point(stack[-2]), 1)
        # clock.tick(5)
        # pygame.display.update()

    # get the end time and execution time
    et = time.process_time()
    elapsed_time = et - st
    print('Execution time for Graham Scan algorithm is:\t', elapsed_time, 'seconds')

    # for p in stack:
    #     pygame.draw.circle(window, hull_color, mapping_point(p), 3)
    #     pygame.display.update()
    # pygame.draw.line(window, line_color, mapping_point(stack[-1]), mapping_point(stack[0]), 1)
    # clock.tick(5)
    # pygame.display.update()
    # print("stack", stack)
    return stack


def main():
    if argv[1].isnumeric():  # case of random points
        n = int(argv[1])  # number of points
        points = []
        for i in range(n):  # case of testfile
            points.append(int(random.triangular(20, 1480) * 10000) / 10000)
            points.append(int(random.triangular(20, 780) * 10000) / 10000)
        points = [Point(points[i], points[i + 1]) for i in range(0, len(points) - 1, 2)]
    else:
        with open(argv[1]) as f:
            points = [Point(*[int(c) for c in line.split()]) for line in f]

    window = initializer("Finding the Convex Hull Using Jarvis March Algorithm", points)

    # hull is result of convex hull vertices

    hull = jarvis_march(points)

    # Showing the convex vertices for Jarvis March algorithm
    for p in hull:
        pygame.draw.circle(window, hull_color, mapping_point(p), 5)
    pygame.display.update()

    x = True
    while x:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                x = False

    window2 = initializer("Finding the Convex Hull Using Graham's Scan Algorithm", points)
    hull = graham_scan(points)

    # Showing the convex vertices for graham's scan algorithm
    for p in hull:
        pygame.draw.circle(window2, hull_color, mapping_point(p), 5)
        pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


if __name__ == "__main__":
    main()