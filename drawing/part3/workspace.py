from turtle import Screen, Turtle
from particles import Particle
from random import random
from math import pi, cos, sin, ceil
import turtle
import os

turtle.tracer(0, 0)


class WorkSpace:
    def __init__(self, k, r, c, v):
        self.canvas = Screen()
        self.size = int(k / 4 * 6) * 10
        self.canvas.setup(width=self.size, height=self.size)
        self.canvas.setworldcoordinates(-1, -1, self.size, self.size)
        self._add_particles(k, r, c, v)
        self._active_list = self.particles.copy()
        self.v = v

    def _add_particles(self, k, r, c, v):
        self.particles = []
        init_pos = (self.size // 2, self.size // 2)
        for i in range(k):
            p = Particle(radius=r, color=c, velocity=v)
            self.particles.append(p)
        i = 0
        for p in self.particles:
            r = random()
            x = 0
            if i <= k // 4:
                p.set_initial_pos(
                    (init_pos[0] + i * 30 + r * x, init_pos[1] + i * 30 + r * x))
            elif i <= k // 2:
                p.set_initial_pos(
                    (init_pos[0] - (i - k // 4) * 30 - r * x, init_pos[1] - (i - k // 4) * 30 - r * x))
            elif i <= 3 * k // 4:
                p.set_initial_pos(
                    (init_pos[0] + (i - k // 2) * 30 + r * x, init_pos[1] - (i - k // 2) * 30 - r * x))
            else:
                p.set_initial_pos(
                    (init_pos[0] - (i - 3 * k // 4) * 30 - r * x, init_pos[1] + (i - 3 * k // 4) * 30 + r * x))
            i += 1
            p.draw()

    def move_all(self, step):
        t = Turtle()
        t.ht()
        s = step
        while step > 0:
            t.write(
                f'Step: {abs(step-s-1)} Active Red: {self._red_left()}')
            t.clear()
            for p in self.particles:
                self._move_one(p)
                p.draw()
            for p in self.particles:
                if p in self._active_list:
                    self.change_color(p)
            step -= 1
        os.system("pause")
        self.canvas.reset()

    def _move_one(self, p):
        cx, cy = p.get_current_pos()
        dx, dy = self._generate_vector()
        if cx + dx < p.radius or cx + dx > self.size - p.radius:
            dx = -dx
        if cy + dy < p.radius or cy + dy > self.size - p.radius:
            dy = -dy
        p.move((cx + dx, cy + dy))
        turtle.stamp()

    def _red_left(self):
        r = 0
        for p in self.particles:
            if p.color == 'red':
                r += 1
        return r

    def change_color(self, curr):
        curr_pos = curr.get_current_pos()
        self._active_list = [p for p in self._active_list if p.color != 'blue']
        for p in self._active_list:
            if p is curr:
                continue
            elif self.collide(curr_pos, p.get_current_pos()):
                curr.set_color('blue')
                p.set_color('blue')

    def collide(self, pos1, pos2):
        if (pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2 < (self.v)**2:
            return True
        return False

    def _generate_vector(self):
        random_angle = random() * pi * 2
        return (self.v * cos(random_angle), self.v * sin(random_angle))


def driver_function(k, step):
    ws = WorkSpace(k, 5, 'red', 10)
    ws.move_all(step)


turtle.update()


driver_function(20, 200)
driver_function(30, 150)
driver_function(50, 100)
