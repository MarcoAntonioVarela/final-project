from game.actor import Actor
from game.point import Point
from game import constants
import random

class Covid(Actor):
    def __init__(self,x_location,y_location):
        super().__init__()
        self._image = constants.IMAGE_COVID
        self._height = constants.COVID_WIDTH
        self._width = constants.COVID_HEIGHT


        self._position = Point(x_location,y_location) 


#We are using polymorphism here, same function, same name, but with a different function
    def get_velocity(self):
        x = random.randint(-4,4)
        y = random.randint(-5,5)
        velocity = Point(x,y)

        

        return velocity

    
        
    
    

