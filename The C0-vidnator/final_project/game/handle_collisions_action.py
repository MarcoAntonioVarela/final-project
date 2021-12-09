from game.attack import Attack
from game.action import Action
from game.physics_service import PhysicsService
from game.point import Point
from game.audio_service import AudioService
from game import constants
class HandleCollisionsAction(Action):

    def execute(self,cast):
        
        physics = PhysicsService()
        collission_attack= cast["attacks"]
        collission_sanitizer = cast["sanitizer"][0]
        covids = cast["covids"]
        sound = AudioService()
      

        for covid in covids:

            for attack in collission_attack:

                
                collided = physics.is_collision(attack,covid)

                if collided == True:
                    sound.play_sound(constants.SOUND_BOUNCE)
                    attack_velocity = attack.get_velocity()
                    dy =attack_velocity.get_y()
                    dy *= -1 
                    new_velocity = Point(attack_velocity.get_x(),dy)
                    attack.set_velocity(new_velocity)
                    

                    cast["covids"].remove(covid)
                    cast["attacks"].remove(attack)


