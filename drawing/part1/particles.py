from turtle import Screen, Turtle
import os


class Particle:
    def __init__(self, velocity=5, radius=5, color='red', speed=0):
        self.radius = radius
        self.velocity = velocity
        self.color = color
        self.speed = speed
        self.pos = [(0, 0), (0, 0)]
        self.t = Turtle()
        self.t.ht()
        self.t.resizemode(rmode='auto')
        self._reset_pen()

    def _reset_pen(self):
        self.t.pen(pencolor=self.color, fillcolor=self.color,
                   pensize=self.radius, speed=self.speed)

    def draw(self):
        self.move(self.t.pos())

    def move(self, new_pos):
        self.pos[0] = self.pos[1]
        self.pos[1] = new_pos
        self.t.setposition(new_pos)

    def get_current_pos(self):
        return self.pos[1]

    def get_prev_pos(self):
        return self.pos[0]

    def set_initial_pos(self, init_pos):
        self.pos = [init_pos, init_pos]
        self.t.speed(0)
        self.t.pu()
        self.t.setposition(init_pos)
        self.t.pd()
        self._reset_pen()

    def set_velocity(self, v):
        self.velocity = v


def driver_func():
    s = Screen()
    s.setup(width=300, height=300)
    p = Particle()
    print("Are you ready?")
    os.system("pause")
    p.draw()
    kx = 0
    ky = 0
    p.set_velocity(10)
    v = p.velocity
    for i in range(20):
        sx = (-1)**kx
        sy = (-1)**ky
        pos = p.get_current_pos()
        x, y = pos
        if i % 2 == 0:
            y += i * v * sy
            ky += 1
        else:
            x += i * v * sx
            kx += 1
        p.move((x, y))
    s.exitonclick()


driver_func()
