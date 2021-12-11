from game.actor import Actor
from game.point import Point
from game import constants

class Mask(Actor):
    def __init__(self,x_location,y_location):
        super().__init__()
        self._image = constants.IMAGE_MASK
        self._height = constants.MASK_WIDTH
        self._width = constants.MASK_HEIGHT


        self._position = Point(x_location,y_location) 

    def get_position(self):
        return self._position
    
        
    
    

