from game.action import Action
from game.sanitizer import Sanitizer
from game.point import Point
from game.action import Action
from game import constants
from game.attack import Attack
from game.covid_attack import Covid_Attack
import random

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
        
         
        

        if space == True and self.timer % 8 == 0:
            
            bullet_position = sanitizer.get_position()
            bullet_x = bullet_position.get_x()
            bulley_t = bullet_position.get_y()
            attack = Attack(bullet_x,bulley_t)
            cast["attacks"].append(attack)



### Making the covids to randonmly shoot miny covids


        if self.timer % 7 == 0:

            total_covids = len(cast["covids"]) -1


            random_modulo = random.randint(0,total_covids)
            covid_direction = self._input_service.get_direction()
            covid = cast["covids"][random_modulo]
            covid.set_velocity(covid_direction.scale(constants.COVID_SPEED))
            covid_bullet_position = covid.get_position()
            covid_bullet_x = covid_bullet_position.get_x()
            covid_bullet_y = covid_bullet_position.get_y()
            covid_attack = Covid_Attack(covid_bullet_x,covid_bullet_y)
            cast["covid_attacks"].append(covid_attack)

    
            
                   
                        
 



            
