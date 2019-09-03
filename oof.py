# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com


class Mover(object):
    def draw():
        fill(value)
    def __init__(self):
        self.location = PVector(320,180)
        self.velocity = PVector(0,0)
        self.acc = 0
        self.acceleration = PVector(self.acc,0)
        
    def update(self):
        self.location.add(self.velocity)
        self.acceleration = PVector(self.acc,0)
        self.velocity.add(self.acceleration)

        if keyPressed:
            if keyCode == 38:
                self.acc = 0.1
            elif keyCode == 40 and self.acc > 0:
                self.acc = -0.1
        if self.velocity.x <= 0 and self.acc < 0:
            self.acc = 0
            self.velocity.x = 0
    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(127)
        ellipse(self.location.x, self.location.y, 48, 48)

    def checkEdges(self):
        if self.location.x > width:
            self.location.x = 0
        elif self.location.x < 0:
            self.location.x = width

        if self.location.y > height:
            self.location.y = 0
        elif self.location.y < 0:
            self.location.y = height
