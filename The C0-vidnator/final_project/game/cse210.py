from game.actor import Actor
from game.point import Point
from game import constants

class CSE210(Actor):
    def __init__(self,x_location,y_location):
        super().__init__()
        self._image = constants.IMAGE_CSE210
        self._height = constants.CSE210_WIDTH
        self._width = constants.CSE210_HEIGHT


        self._position = Point(x_location,y_location) 

    def get_position(self):
        return self._position
    
        
    
    

