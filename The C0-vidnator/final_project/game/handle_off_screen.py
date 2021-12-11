from game.point import Point
from game.constants import MAX_X
from game.constants import MAX_Y
from game.action import Action
from game import constants
import random


class Handle_Off_Screen_Action(Action):
    
    def execute(self,cast):
        
        bouncing_covids = cast['covids']

        for covid in bouncing_covids:


            position = covid.get_position()
            x = position.get_x()
            y = position.get_y()

            if x <= 10:
                
                new_x =12
                new_y = y
                new_position =Point(new_x,new_y)
                covid.set_position(new_position)

            if x >= 960:
                
                new_x =955
                new_y = y
                new_position =Point(new_x,new_y)
                covid.set_position(new_position)

            if y <= 10:
                
                new_x = x
                new_y = 10
                new_position =Point(new_x,new_y)
                covid.set_position(new_position)

