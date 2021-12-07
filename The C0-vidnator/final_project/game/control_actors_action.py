from game.action import Action
from game.sanitizer import Sanitizer
from game.point import Point
from game.action import Action
from game import constants
from game.attack import Attack


class ControlActorsAction(Action):

    def __init__(self, input_service):

        self._input_service = input_service
        self.timer = 0
        

    def execute(self,cast):

        self.timer += 1


        direction = self._input_service.get_direction()
        space = self._input_service.is_space_pressed()
        sanitizer = cast["sanitizer"][0]
        sanitizer.set_velocity(direction.scale(constants.SANITIZER_SPEED)) 
        

        if space == True and self.timer % 12 == 0:
            
            bulled_position = sanitizer.get_position()
            bullet_x = bulled_position.get_x()
            bulley_y = bulled_position.get_y()
            attack = Attack(bullet_x,bulley_y)
            cast["attacks"].append(attack)
        