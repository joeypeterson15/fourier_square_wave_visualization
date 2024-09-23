from graphics import *
import numpy

def main():
    win = GraphWin("My Circle", 1500, 700)
    radius = 150
    center_cx = 300
    center_cy = 350
    angle = 0
    c = Circle(Point(center_cx,center_cy), radius)
    c.draw(win)

    # Create a point that will move along the circle
    p = Circle(Point((center_cx + numpy.cos(angle) * radius), center_cy + numpy.sin(angle) * radius), 5)
    p.setFill("red")
    p.draw(win)

    while True:
        p.undraw()
        angle += 0.01
        # get x,y coordinates from polar
        x = center_cx + numpy.cos(angle) * radius
        y = center_cy + numpy.sin(angle) * radius
        p = Circle(Point(x,y), 5)
        p.setFill("red")
        p.draw(win)

        # time.sleep(0.015)

        if win.checkMouse():
            break # pause for click in window

main()