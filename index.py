from graphics import *
import numpy

class circleGenerator:
    def __init__(self, r, x, y, offset):
        self.radius = r
        self.x_center = x
        self.y_center = y
        self.angle = 0
        self.offset = offset
        self.starting_px = self.x_center + numpy.cos(self.angle) * self.radius
        self.starting_py = self.y_center + numpy.sin(self.angle) * self.radius

    def updateAngle(self):
        self.angle += self.offset
    def updateCenterCoordinates(self, x, y):
        self.x_center = x
        self.y_center = y
    def updatePCoordinates(self):
        self.starting_px = self.x_center + numpy.cos(self.angle) * self.radius
        self.starting_py = self.y_center + numpy.sin(self.angle) * self.radius

def main():
    win = GraphWin("Fourier Square wave visualization", 800, 700, autoflush=False)

    c1radius = 150
    c2radius = 50
    c3radius = 17

    c1 = circleGenerator(c1radius, 300, 350, 0.1)
    c1Graph = Circle(Point(c1.x_center,c1.y_center), c1radius)
    c1Graph.draw(win)

    # Create a point that will move along the circle
    p = Circle(Point(c1.starting_px, c1.starting_py), 4)
    p.setFill("purple")
    p.draw(win)

    c2 = circleGenerator(c2radius, c1.starting_px, c1.starting_py, 0.3)


    c2Graph = Circle(Point(c2.x_center, c2.y_center), c2radius)
    c2Graph.draw(win)

    p2 = Circle(Point(c2.starting_px, c2.starting_py), 2)
    p2.setFill("purple")
    p2.draw(win)

    c3 = circleGenerator(c3radius, c2.starting_px, c2.starting_py, 0.5)

    c3Graph = Circle(Point(c3.x_center, c3.y_center), c3radius)
    c3Graph.draw(win)

    p3 = Circle(Point(c3.starting_px, c3.starting_py), 1)
    p3.setFill("purple")
    p3.draw(win)

    # create a line that points to rotating point on circle from center
    r_line = Line(Point(c1.x_center, c1.y_center), Point(c1.starting_px, c1.starting_py))
    r_line.draw(win)

    r_line2 = Line(Point(c2.x_center, c2.y_center), Point(c2.starting_px, c2.starting_py))
    r_line2.draw(win)

    r_line3 = Line(Point(c3.x_center, c3.y_center), Point(c3.starting_px, c3.starting_py))
    r_line3.draw(win)

    wave_arrow = Line(Point(c3.starting_px, c3.starting_py), Point(600, 350))
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
        c2Graph.undraw()
        p2.undraw()
        c3Graph.undraw()
        p3.undraw()

        c1.updateAngle()
        c1.updatePCoordinates()
        c2.updateAngle()
        c2.updateCenterCoordinates(c1.starting_px, c1.starting_py)
        c2.updatePCoordinates()
        c3.updateAngle()
        c3.updateCenterCoordinates(c2.starting_px, c2.starting_py)
        c3.updatePCoordinates()
        # get px,py coordinates from polar

        p.move(c1.starting_px - p.getCenter().getX(), c1.starting_py - p.getCenter().getY())


        c2Graph = Circle(Point(c2.x_center, c2.y_center), c2radius)
        c2Graph.draw(win)

        p2 = Circle(Point(c2.starting_px, c2.starting_py), 2)
        p2.setFill("purple")
        p2.draw(win)

        c3Graph = Circle(Point(c3.x_center, c3.y_center), c3radius)
        c3Graph.draw(win)

        p3 = Circle(Point(c3.starting_px, c3.starting_py), 1)
        p3.setFill("purple")
        p3.draw(win)
    
        r_line = Line(Point(c1.x_center, c1.y_center), Point(c1.starting_px, c1.starting_py))
        r_line.draw(win)
        r_line2 = Line(Point(c2.x_center, c2.y_center), Point(c2.starting_px, c2.starting_py))
        r_line2.draw(win)
        r_line3 = Line(Point(c3.x_center, c3.y_center), Point(c3.starting_px, c3.starting_py))
        r_line3.draw(win)

        wave_arrow = Line(Point(c3.starting_px, c3.starting_py), Point(600, c3.starting_py))
        wave_arrow.setArrow("last")
        wave_arrow.draw(win)

        translation = 5
        translaterCount = 0
        wave_points.insert(0, [600, c3.starting_py])
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