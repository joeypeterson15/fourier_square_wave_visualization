from graphics import *
import numpy

def main():
    win = GraphWin("Fourier Square wave visualization", 800, 700, autoflush=False)
    radius = 150
    c2radius = 50
    c3radius = 17
    center_cx = 300
    center_cy = 350
    angle = 0
    angle2 = 0
    angle3 = 0
    c = Circle(Point(center_cx,center_cy), radius)
    c.draw(win)

    # Create a point that will move along the circle
    starting_px = center_cx + numpy.cos(angle) * radius
    starting_py = center_cy + numpy.sin(angle) * radius
    p = Circle(Point(starting_px, starting_py), 4)
    p.setFill("purple")
    p.draw(win)

    center_cx2 = starting_px
    center_cy2 = starting_py
    c2 = Circle(Point(center_cx2, center_cy2), c2radius)
    c2.draw(win)
    starting_px2 = center_cx2 + numpy.cos(angle) * c2radius
    starting_py2 = center_cy2 + numpy.sin(angle) * c2radius
    p2 = Circle(Point(starting_px2, starting_py2), 2)
    p2.setFill("purple")
    p2.draw(win)

    center_cx3 = starting_px2
    center_cy3 = starting_py2
    c3 = Circle(Point(center_cx3, center_cy3), c3radius)
    c3.draw(win)
    starting_px3 = center_cx3 + numpy.cos(angle) * c3radius
    starting_py3 = center_cy3 + numpy.sin(angle) * c3radius
    p3 = Circle(Point(starting_px3, starting_py3), 1)
    p3.setFill("purple")
    p3.draw(win)

    # create a line that points to rotating point on circle from center
    r_line = Line(Point(center_cx, center_cy), Point(starting_px, starting_py))
    r_line.draw(win)

    r_line2 = Line(Point(center_cx2, center_cy2), Point(starting_px2, starting_py2))
    r_line2.draw(win)

    r_line3 = Line(Point(center_cx3, center_cy3), Point(starting_px3, starting_py3))
    r_line3.draw(win)

    wave_arrow = Line(Point(starting_px3, starting_py3), Point(600, 350))
    wave_arrow.draw(win)

    wave_points = []
    wave_lines = []

    # create animation
    while True:
        for line in wave_lines:
            line.undraw()

        r_line.undraw()
        r_line2.undraw()
        r_line3.undraw()
        wave_arrow.undraw()
        c2.undraw()
        p2.undraw()
        c3.undraw()
        p3.undraw()

        angle += 0.1
        angle2 += 0.3
        angle3 += 0.5

        # get x,y coordinates from polar
        x = center_cx + numpy.cos(angle) * radius
        y = center_cy + numpy.sin(angle) * radius
        p.move(x - p.getCenter().getX(), y - p.getCenter().getY())

        center_cx2 = x
        center_cy2 = y
        c2 = Circle(Point(center_cx2, center_cy2), c2radius)
        c2.draw(win)
        starting_px2 = center_cx2 + numpy.cos(angle2) * c2radius
        starting_py2 = center_cy2 + numpy.sin(angle2) * c2radius
        p2 = Circle(Point(starting_px2, starting_py2), 2)
        p2.setFill("purple")
        p2.draw(win)

        center_cx3 = starting_px2
        center_cy3 = starting_py2
        c3 = Circle(Point(center_cx3, center_cy3), c3radius)
        c3.draw(win)
        starting_px3 = center_cx3 + numpy.cos(angle3) * c3radius
        starting_py3 = center_cy3 + numpy.sin(angle3) * c3radius
        p3 = Circle(Point(starting_px3, starting_py3), 1)
        p3.setFill("purple")
        p3.draw(win)
    
        r_line = Line(Point(center_cx, center_cy), Point(x, y))
        r_line.draw(win)
        r_line2 = Line(Point(center_cx2, center_cy2), Point(starting_px2, starting_py2))
        r_line2.draw(win)
        r_line3 = Line(Point(center_cx3, center_cy3), Point(starting_px3, starting_py3))
        r_line3.draw(win)

        wave_arrow = Line(Point(starting_px3, starting_py3), Point(600, starting_py3))
        wave_arrow.setArrow("last")
        wave_arrow.draw(win)

        translation = 5
        translaterCount = 0
        wave_points.insert(0, [600, starting_py3])
        for i in range(len(wave_points) - 1):
            x,y = wave_points[i]
            nextx, nexty = wave_points[i + 1]
            wave_line = Line(Point(x + translaterCount,y), Point(nextx + translaterCount + translation, nexty))
            translaterCount += translation
            wave_line.draw(win)
            wave_lines.append(wave_line)
        
        if (len(wave_points)) > 10:
            wave_points.pop()

        # win.update()
        time.sleep(0.15)

        if win.checkMouse():
            break

main()