from graphics import *
import numpy

COLOR = "purple"

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

def main(n, startingRadius):
    win = GraphWin("Fourier Square wave visualization", 800, 700, autoflush=False)

    pointColor = "purple"

    radii = [startingRadius]
    offsets = [0.1]
    circleInstants = [circleGenerator(radii[0], 300, 350, 0.1)]
    for i in range(1, n):
        radius = startingRadius/(i * 3)
        radii.append(radius)
        offset = offsets[i - 1] + 2 / 10
        offsets.append(offset)

        c = circleGenerator(radius, circleInstants[i - 1].starting_px, circleInstants[i - 1].starting_py, offset)
        circleInstants.append(c)

    circleGraphs = []
    for c in circleInstants:
        graph = Circle(Point(c.x_center,c.y_center), c.radius)
        graph.draw(win)
        circleGraphs.append(graph)

    # Create a point that will move along the circle
    rotatingPoints = []
    for c in circleInstants:
        p = Circle(Point(c.starting_px, c.starting_py), 1)
        p.setFill(pointColor)
        p.draw(win)
        rotatingPoints.append(p)

    # create a line that points to rotating point on circle from center
    r_lines = []
    for c in circleInstants:
        r_line = Line(Point(c.x_center, c.y_center), Point(c.starting_px, c.starting_py))
        r_line.draw(win)
        r_lines.append(r_line)

    wave_arrow = Line(Point(circleInstants[len(circleInstants) - 1].starting_px, circleInstants[len(circleInstants) - 1].starting_py), Point(600, 350))
    wave_arrow.draw(win)

    wave_points = []
    wave_lines = []

    # create animation
    while True:
        for line in wave_lines:
            line.undraw()

        for rLine in r_lines:
            rLine.undraw()

        wave_arrow.undraw()

        for i in range(1, n):
            circleGraphs[i].undraw()

        for i in range(n):
            rotatingPoints[i].undraw()

            circleInstants[i].updateAngle()
            if i >= 1:
                circleInstants[i].updateCenterCoordinates(circleInstants[i - 1].starting_px, circleInstants[i - 1].starting_py)
            circleInstants[i].updatePCoordinates()

        # KEEP THIS
        # p.move(c1.starting_px - p.getCenter().getX(), c1.starting_py - p.getCenter().getY())

        for i in range(1, n):
            cGraph = Circle(Point(circleInstants[i].x_center, circleInstants[i].y_center), radii[i])
            cGraph.draw(win)
            circleGraphs[i] = cGraph

        for i in range(n):
            p = Circle(Point(circleInstants[i].starting_px, circleInstants[i].starting_py), 1)
            p.setFill(COLOR)
            p.draw(win)
            rotatingPoints[i] = p

            r_line = Line(Point(circleInstants[i].x_center, circleInstants[i].y_center), Point(circleInstants[i].starting_px, circleInstants[i].starting_py))
            r_line.draw(win)
            r_lines[i] = r_line

        wave_arrow = Line(Point(circleInstants[len(circleInstants) - 1].starting_px, circleInstants[len(circleInstants) - 1].starting_py), Point(600, circleInstants[len(circleInstants) - 1].starting_py))
        wave_arrow.setArrow("last")
        wave_arrow.draw(win)

        translation = 5
        translaterCount = 0
        wave_points.insert(0, [600, circleInstants[len(circleInstants) - 1].starting_py])
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

n = 20
outerRadius = 150
main(n, outerRadius)