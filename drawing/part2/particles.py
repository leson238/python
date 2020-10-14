from turtle import Turtle


class Particle:
    def __init__(self, radius=5, color='red', velocity=10):
        self.radius = radius
        self.velocity = velocity
        self.color = color
        self.pos = [(0, 0), (0, 0)]
        self.t = Turtle()
        self.t.ht()
        self.t.resizemode(rmode='auto')
        self._reset_pen()
        self.t.pu()

    def _reset_pen(self):
        self.t.pen(pencolor=self.color, fillcolor=self.color,
                   pensize=self.radius, speed=3)

    def draw(self):
        self.t.pd()
        self.t.setposition(self.t.pos())
        self.t.pu()

    def move(self, new_pos):
        self.t.pen(pencolor="white", fillcolor="white",
                   pensize=self.radius, speed=3)
        self.t.pd()
        self.t.setposition(self.t.pos())
        self.t.pu()
        self._reset_pen()
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
        self._reset_pen()

    def set_color(self, c):
        self.color = c
        self._reset_pen()
