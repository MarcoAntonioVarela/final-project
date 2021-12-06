from game.action import Action
from game.sanitizer import Sanitizer
from game.point import Point
from game.action import Action
from game import constants


class ControlActorsAction(Action):

    def __init__(self, input_service):

        self._input_service = input_service
        

    def execute(self,cast):

        direction = self._input_service.get_direction()
        sanitizer = cast["sanitizer"][0]
        sanitizer.set_velocity(direction.scale(constants.SANITIZER_SPEED)) 
        
        