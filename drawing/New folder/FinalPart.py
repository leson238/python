import pygame
import random


class Particle(object):

    def __init__(self, radius, velocity, color, x, y):

        self._radius = radius
        self.velocity = 0
        self.color = color
        self.x = x
        self.y = y
        self.pos = (x, y)

    def draw(self, win, x, y):

        self.pos = (x, y)
        pygame.draw.circle(win, self.color, (int(x), int(y)), radius)


class WorkSpace(object):

    global length, velocity, color, radius

    def __init__(self):
        h = number/2
        self.width = int(((h * 30)**2/2)**0.5)

    def RandomParticle(self):

        self.particles = []

        for i in range(int(number/2)):

            leftx = int(i*30)+radius
            lefty = int(i*30)+radius

            particle = Particle(5, 7, (255, 0, 0), leftx, lefty)
            self.particles.append(particle)

        for i in range(int(number/2)):

            rightx = int(self.width - i*30)-radius
            righty = int(i*30)+radius

            particle = Particle(5, 7, (255, 0, 0), rightx, righty)
            self.particles.append(particle)

    def CheckCollision(self):

        for i in range(number):
            for j in range(number):
                if j == i or self.particles[i].color == (0, 0, 255) or self.particles[j].color == (0, 0, 255):
                    continue
                distx = self.particles[j].pos[0] - self.particles[i].pos[0]
                disty = self.particles[j].pos[1] - self.particles[i].pos[1]
                distance = (distx**2 + disty**2) ** 0.5
                if distance <= (radius*2):
                    self.particles[i].color = (0, 0, 255)
                    self.particles[j].color = (0, 0, 255)

    def move_all(self):
        global win
        pygame.init()
        win = pygame.display.set_mode((self.width, self.width))
        s = 0
        while s < steps:
            win.fill((0, 0, 0))
            self.CheckCollision()
            for i in range(number):
                move = random.choice(['up', 'down', 'left', 'right'])
                x, y = self.particles[i].pos
                if move == 'up':
                    if y >= 20 + 2*radius:
                        y -= 20
                    else:
                        y += 20

                if move == 'down':
                    if y <= width - 2*radius:
                        y += 20
                    else:
                        y -= 20

                if move == 'left':
                    if x >= 20 + 2*radius:
                        x -= 20
                    else:
                        x += 20

                if move == 'right':
                    if x <= width - 2*radius:
                        x += 20
                    else:
                        x -= 20
                self.particles[i].draw(win, x, y)
            pygame.time.delay(100)
            pygame.display.update()

            s += 1


def main():

    global radius, width, velocity, color, steps, number

    width = 500
    radius = 5
    velocity = 10

    u = input('Please enter 1 (20 particles, 200 steps), 2(30/150), 3(50/100): ')

    if u == '1':
        number = 20
        steps = 200
        canvas = WorkSpace()
        canvas.RandomParticle()
        canvas.move_all()

    if u == '2':

        number = 30
        steps = 150
        canvas = WorkSpace()
        canvas.RandomParticle()
        canvas.move_all()

    if u == '3':

        number = 50
        steps = 100
        canvas = WorkSpace()
        canvas.RandomParticle()
        canvas.move_all()


main()
