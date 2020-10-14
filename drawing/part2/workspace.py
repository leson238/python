from turtle import Screen
from particles import Particle
from random import random
from math import pi, cos, sin


class WorkSpace:
    def __init__(self, size, r, c, v):
        self.canvas = Screen()
        self.size = size
        self.canvas.setup(width=size, height=size)
        self.canvas.setworldcoordinates(-1, -1, size, size)
        self._add_particles(2, r, c, v)
        self.v = v

    def _add_particles(self, n, r, c, v):
        self.particles = []
        for i in range(n):
            self.particles.append(Particle(radius=r, color=c, velocity=v))
        self.particles[0].set_initial_pos((self.size // 2 - 20, self.size / 2))
        self.particles[1].set_initial_pos((self.size // 2 + 20, self.size / 2))

    def move_all(self, step):
        while step > 0:
            for p in self.particles:
                self._move_one(p)
                p.draw()
                if p.color == 'blue':
                    self.particles.remove(p)
            for p in self.particles:
                self.change_color(p)
            step -= 1
        self.canvas.exitonclick()

    def _move_one(self, p):
        pos = p.get_current_pos()
        while True:
            offset = self._generate_new_pos()
            x, y = int(pos[0] + offset[0]), int(pos[1] + offset[1])
            if 0 <= x <= self.size and 0 <= y <= self.size:
                p.move((x, y))
                break

    def change_color(self, curr):
        curr_pos = curr.get_current_pos()
        for p in self.particles:
            if p == curr:
                continue
            if self.collide(curr_pos, p.get_current_pos()):
                curr.set_color('blue')
                p.set_color('blue')

    def collide(self, pos1, pos2):
        if (pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2 < (self.v)**2:
            return True
        return False

    def _generate_new_pos(self):
        random_angle = random() * pi * 2
        return (self.v * cos(random_angle), self.v * sin(random_angle))


ws = WorkSpace(500, 5, 'red', 10)
ws.move_all(200)
