from graphics import *
import numpy

def main():
    win = GraphWin("Fourier Square wave visualization", 1500, 700)
    radius = 150
    center_cx = 300
    center_cy = 350
    angle = 0
    c = Circle(Point(center_cx,center_cy), radius)
    c.draw(win)

    # Create a point that will move along the circle
    starting_px = center_cx + numpy.cos(angle) * radius
    starting_py = center_cy + numpy.sin(angle) * radius
    p = Circle(Point(starting_px, starting_py), 5)
    p.setFill("red")
    p.draw(win)

    # create a line that points to rotating point on circle from center
    r_line = Line(Point(center_cx, center_cy), Point(starting_px, starting_py))
    r_line.draw(win)

    wave_arrow = Line(Point(starting_px, starting_py), Point(600, 350))
    wave_arrow.draw(win)

    wave_points = []
    wave_lines = []

    # create animation
    while True:
        p.undraw()
        r_line.undraw()
        wave_arrow.undraw()

        angle += 0.1
        # get x,y coordinates from polar
        x = center_cx + numpy.cos(angle) * radius
        y = center_cy + numpy.sin(angle) * radius
        p = Circle(Point(x,y), 5)
        p.setFill("red")
        p.draw(win)

        r_line = Line(Point(center_cx, center_cy), Point(x, y))
        r_line.draw(win)
        wave_arrow = Line(Point(x, y), Point(600, y))
        wave_arrow.setArrow("last")
        wave_arrow.draw(win)

        # remove lines to improve performance
        if len(wave_lines) > 30:
            for wl in wave_lines[-5:]:
                wl.undraw()
            # wave_points = wave_points[:-5]
            wave_lines = wave_lines[:-5]

        # now append each point that the arrow points to and add to beginning of wave_points array. 
        # draw a line that connects each wave_point
        x_wave_point = 600 + (angle * 50)
        wave_points.append([x_wave_point, y])
        for i in range(len(wave_points) - 1):
            x, y = wave_points[i]
            nextx, nexty = wave_points[i + 1]
            l = Line(Point(nextx, nexty), Point(x, y))
            l.draw(win)
            wave_lines.append(l)

        win.update()
        # time.sleep(0.5)

        if win.checkMouse():
            break

main()