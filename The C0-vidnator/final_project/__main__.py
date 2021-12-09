#Marco Varela
#Final Project

from os import X_OK
import random
from game.title import Title
from game.cse210 import CSE210
from game import constants
from game.director import Director
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.covid import Covid
from game.move_actors_action import MoveActorsAction
from game.sanitizer import Sanitizer
from game.mask import Mask
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen import Handle_Off_Screen_Action


def main():
            
   
    #My cast (dictionary) contains several lists, each list represents a group of actors

    cast = {} 

    #Each list contains one or many individual actors
    
    cast["covids"] = []
    cast["attacks"] = []
    cast["covid_attacks"] = []
    cast["masks"]= []
    cast["titles"]= []
    cast["CSE210S"]= []
    cast["sanitizer"] = []
    sanitizer = Sanitizer(5,800)
    cast["sanitizer"].append(sanitizer)



#I have created a for loop in order to create and append several covids (4 lines x 11 columns)
    for y in range(4):     
        for x in range(11):
            covid = Covid((x*90) ,(y*74))  
            cast["covids"].append(covid)

#I have created a for loop in order to create and append 3 covids (1 line x 3 columns)
    for y in range (1,2):
        for x in range(0,3):
            mask = Mask((x*370) ,(y*660))
            cast["masks"].append(mask)

#I have created a for loop in order to create and append 1 title holding my information 
    for y in range (1,2):          
        for x in range(1,2):
            title = Title((x*820) ,(y*850))
            cast["titles"].append(title)

    
#I have created a for loop in order to create and append 1 title holding the course information
    for y in range (1,2):
        for x in range(1,2):
            cse210 = CSE210((x*10) ,(y*850))
            cast["CSE210S"].append(cse210)




    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    move_actors_action = MoveActorsAction()
    
    control_actors_action = ControlActorsAction(input_service)
    draw_actors_action = DrawActorsAction(output_service)
    handle_collisions_action = HandleCollisionsAction()
    handle_off_screen_action = Handle_Off_Screen_Action()

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    #script["update"] = [move_actors_action,handle_collisions_action]
    script["update"] = [move_actors_action,handle_off_screen_action,handle_collisions_action]
    
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("The C0-vidnator by Marco Varela")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio(constants.SOUND_OVER)

if __name__ == "__main__":
    main()
