from game.point import Point
from game.actor import Actor
from game import constants




class Attack(Actor):
    def __init__(self,x_location,y_location):
        super().__init__()
        self._image = constants.IMAGE_ATTACK
        self._height = constants.ATTACK_HEIGHT
        self._width = constants.ATTACK_WIDTH

        point = Point(-7,-5)
        self._velocity = point

        self._position = Point(x_location,y_location)

    def get_position(self):
        return self._position
