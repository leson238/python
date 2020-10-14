import pygame
import random

class Particle(object):
    
    def __init__(self, radius, velocity, color, x, y):
        
        self._radius = radius
        self.velocity = 0
        self.color = color        
        self.x = x
        self.y = y
        self.position = (self.x,self.y)
        
           
    def draw(self, win, x, y):
        
        self.position = (x,y)
        pygame.draw.circle(win, self.color, (int(x), int(y)), radius)
        
        
class WorkSpace(object):
    
    global radius, length, velocity, color
    
    def __init__(self, Particle1, Particle2, color):
        self.color=color
        self.Particle1 = Particle(radius, velocity, self.color, length//2-20, length//2)
        self.Particle2 = Particle(radius, velocity, self.color, length//2+20, length/2)                       
        
    def move_all(self):
        
        global win
        
        pygame.init()
                
        win = pygame.display.set_mode((length, length))        
        i = 0
        
        x1 = length//2-20
        y1 = length//2
        x2 = length//2+20
        y2 = length/2
        
            
        while i < 200:
           
            if (x1+10==x2-10 and y1==y2) or (x1-10==x2+10 and y1==y2) or (x1==x2 and y1+10==y2-10) or (x1==x2 and y1-10==y2+10): 
                
                self.change_color()
                
                print('yes')
                
            move1 = random.choice(['up', 'down', 'left', 'right'])
            move2 = random.choice(['up','down','left', 'right'])
            win.fill((0,0,0))
                        
            if move1 == 'up':
                            
                if y1 >= 0:
                    y1 -= 20
                else:
                    y1 += 20
                                
                            
            if move1 == 'down':
                            
                if y1 <= length:
                    y1 += 20
                else:
                    y1 -= 20
                            
            if move1 == 'left':       
                if x1 >= 0:
                    x1 -= 20
                else:
                    x1 += 20
                                
            if move1 == 'right':
                            
                if x1 <= length:
                    x1 += 20
                else:
                    x1 -= 20
                                
            if move2 == 'up':
                                                
                if y2 >= 0:
                    y2 -= 10
                else:
                    y2 += 10
                                                    
                                                
            if move2 == 'down':
                                   
                if y2 <= length:
                    y2 += 10
                else:
                    y2 -= 10
                                                
            if move2 == 'left':
                                                
                if x2 >= 0:
                    x2 -= 10
                else:
                    x2 += 10
                                                    
            if move2 == 'right':
                                    
                if x2 <= length:
                    x2 += 10
                else:
                    x2 -= 10                       
            self.Particle1.draw(win, x1, y1)
            self.Particle2.draw(win, x2, y2)
                                   
            pygame.time.delay(100)  
            
            pygame.display.update()
            
            
            i += 1
            
    def change_color(self):   
        
        self.color=(0, 0, 255)
            
    
        
        
def main():
    
    global radius, length, velocity, color
    length = 300
    radius = 5
    velocity = 10
    
    Particle1 = ''
    Particle2 = ''
    canvas = WorkSpace(Particle1,Particle2, (255, 0, 0))
    canvas.move_all()


main()