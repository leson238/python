from cs1graphics import *
from time import *


class Particle():
    
    def __init__(self, radius, velocity, color, position):
        
        self._radius = radius
        self.velocity = 0
        self.color = color        
        self.position = position
        
        particle =  Square(radius, position)
        particle.setFillColor(color)
        
    def draw1(self, radius, color):
        
        '''this section is made to draw the particle on the canvas, at positon (0,0), using a color input by the user and a radius'''
        
        initX = 0
        initY = 0        
        position = Point(initX,initY)
        
        particle =  Square(radius, position)
        particle.setFillColor(color)        
        canvas.add(particle)
        
    def move1(self, x, y, velocity):
    
        '''this section is made to make the particle move across the screen, leaving a path behind it. IT CANNOT WORK WITHOUT THE PREVIOUS FUNCTION BEING CALLED FIRST '''
        
        if x != 0:
            prevX = x
        elif y != 0:
            prevY = y
        
        i = 0
        y = 0
        
        while i < x or j < y :
            
            # i = x adn j = y
            
            particle.move(velocity,0); particle.move(0,velocity)
            sleep(0.1)
            
            path = Path(Point(initX, initY))
            path.setBorderColor('red')
            path.setBorderWidth(5)
            canvas.add(path)   
            
            i = i+1 ; j = j+1
            
            while True:
                
                path.addPoint(i,j)
                        
    def getPrevious(self, position):
        
        if x != initX or y != initY:
            
            position = Point(prevX, prevY)
            print('Previous position: ', position)
            
        else:
            
            raise ValueError("Before getting previous position, move function must be called")
    
    def setVelocity(self, velocity):
        
        velocity = int(input('Enter velocity at which you want your particle to move: '))
        print("Your particle will now travel at ", velocity, "per frame.")
        
    def setInitialPosition(self, x,y):
        
        position = Point(x, y)
    
    def spiral(self):
        
        print('Are you ready to see the spiral? Click anyhwere')
        canvas.wait()
        
        particle.setInitialPosition(150,150)
        particle.setVelocity(10)
        
        g = particle.getReferencePoint()
        g = Point(x,y)
        
        i = 0
        f = 1
        
        while g != Point(250,250):
            
            particle.move(prevX ,velocity+i, 10)
            particle.move(velocity+i, prevY, 10)
            particle.move(prevX, -(velocity+f), 10)
            particle.move(-(velocity+f), prevY, 10)
            
            i = i + 1
            f = f + 1
            
            
            
            
            
            
# TESTING 
canvas = Canvas(300,300,'white','Animation')
p = Point(0,0)
particle = Particle(5, 10, 'red', p)
particle.draw1(5, 'red')
particle.move1(80,270,10)
particle.spiral()
