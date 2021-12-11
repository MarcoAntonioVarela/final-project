from game.victory import Victory
from game.attack import Attack
from game.action import Action
from game.physics_service import PhysicsService
from game.point import Point
from game.audio_service import AudioService
from game.game_over import  Game_Over
from game.victory import Victory

from game import constants


class HandleCollisionsAction(Action):

    def execute(self,cast):
        
        physics = PhysicsService()
        collission_attack= cast["attacks"]
        covid_collission_attack= cast["covid_attacks"]
        sanitizer_collission_attack= cast["covid_attacks"]
        #sanitizer_collission_attack= cast["covid_attacks"]
        #collission_sanitizer = cast["sanitizer"][0]
        covids = cast["covids"]
        masks = cast["masks"]
        masks2 = cast["masks"]
        # victory = cast["victory"]
        sanitizers = cast["sanitizer"]
        
        #masks2 = cast["masks"]

        sound = AudioService()
        covid_sound = AudioService()
        sanitizer_sound = AudioService()
        victory_sound = AudioService()
        victory_background_sound = AudioService()
      

##############################################################################
#Collision if the attack (coming from sanitizer) hits one covid 

        for covid in covids:

            for attack in collission_attack:

                
                collided = physics.is_collision(attack,covid)

                covid_list_lenght = len(cast["covids"])




                if collided == True and covid_list_lenght >=2:
                    sound.play_sound(constants.SOUND_DEATH)
                    attack_velocity = attack.get_velocity()
                    dy =attack_velocity.get_y()
                    dy *= -1 
                    new_velocity = Point(attack_velocity.get_x(),dy)
                    attack.set_velocity(new_velocity)
                    

                    cast["covids"].remove(covid)
                    cast["attacks"].remove(attack)


                if collided == True and covid_list_lenght == 1:
                    victory_sound.play_sound(constants.SOUND_VICTORY)
                    #victory_background_sound.play_sound(constants.SOUND_VICTORY_BACKGROUND)
                    cast["attacks"].remove(attack)               
                    #Creating game over
                    for y2 in range (1,2):
                        for x2 in range(1,2):
                            victory = Victory((x2*150) ,(y2*60))
                            cast["victory"].append(victory)
                            cast["covids"].remove(covid)
                    

                  
        
###################################################################
#Collision when covid attack hits the mask

        for mask in masks:

            for covid_attack in covid_collission_attack:

                
                covid_collided = physics.is_collision(covid_attack,mask)

                if covid_collided == True:
                    covid_sound.play_sound(constants.SOUND_BOUNCE)
              
                    

                
                    cast["covid_attacks"].remove(covid_attack)


###################################################################
#Collision when sanitizer attack hits the mask

        for mask in masks:

            for attack in collission_attack:

                
                collided = physics.is_collision(attack,mask)

                if collided == True:
                    sanitizer_sound.play_sound(constants.SOUND_BOUNCE)
              
                    cast["attacks"].remove(attack)


###################################################################
#Collision when covid attack hits the sanitizer

        for sanitizer in sanitizers:

            for covid_attack in covid_collission_attack:

                
                covid_collided = physics.is_collision(covid_attack,sanitizer)

                if covid_collided == True:
                    sanitizer_sound.play_sound(constants.SOUND_OVER)
                    cast["covid_attacks"].remove(covid_attack)                 
                    #Creating game over
                    for y in range (1,2):
                        for x in range(1,2):
                            game_over = Game_Over((x*200) ,(y*240))
                            cast["game_over"].append(game_over)
                                    






