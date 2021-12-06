from game.point import Point
from game.constants import MAX_X
from game.action import Action
from game import constants


class Handle_Off_Screen_Action(Action):
    
    def execute(self,cast):
        
        bouncing_attacks = cast['attacks']

        for attack in bouncing_attacks:

            attack_point = attack.get_position()
            x = attack_point.get_x()
            y = attack_point.get_y()
            attack_velocity = attack.get_velocity()
            if x <= 0 or x >= 995:
                
                dx =attack_velocity.get_x()
                dx *= -1 
                #attack_velocity.set_x(dx)
                new_velocity =Point(dx,attack_velocity.get_y())
                attack.set_velocity(new_velocity)
            
            if y <= 0:
                dy =attack_velocity.get_y()
                dy *= -1 
                new_velocity =Point(attack_velocity.get_x(),dy)
                attack.set_velocity(new_velocity)
            





