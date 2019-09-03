from oof import Mover


def setup():
    size(640, 360)
    global mover
    mover = Mover()


def draw():
    background(255)
    print(mover.acceleration.x, mover.velocity.x)
    mover.update()
    mover.checkEdges()
    mover.display()
