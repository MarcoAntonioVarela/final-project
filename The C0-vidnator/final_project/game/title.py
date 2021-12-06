from game.actor import Actor
from game.point import Point
from game import constants

class Title(Actor):
    def __init__(self,x_location,y_location):
        super().__init__()
        self._image = constants.IMAGE_TITLE
        self._height = constants.TITLE_WIDTH
        self._width = constants.TITLE_HEIGHT


        self._position = Point(x_location,y_location) 

    def get_position(self):
        return self._position
    
        
    
    

