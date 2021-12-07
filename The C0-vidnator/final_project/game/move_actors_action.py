from typing import cast
from game.action import Action
from game.actor import Actor
from game.point import Point


class MoveActorsAction(Action):

    def execute(self,cast):


        for cast_actors in cast:

            for individual_actor in cast[cast_actors]:
                velocity = individual_actor.get_velocity()
                position = individual_actor.get_position()

                #Merging/separating both x and y values so we can use them in our Point parameters
                new_x_position = velocity.get_x() + position.get_x() 
                new_y_position = velocity.get_y() + position.get_y() 


                new_position = Point(new_x_position,new_y_position)

                individual_actor.set_position(new_position)



