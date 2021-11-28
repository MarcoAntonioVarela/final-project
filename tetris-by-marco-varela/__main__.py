def main():

    # create the cast {key: tag, value: list}
    cast = {} 

    cast["shapes"] = []

    shape = Shape(355,500)
    cast["shapes"].append(ball)

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    move_actors_action = MoveActorsAction()
    
    control_actors_action = ControlActorsAction(input_service)
    draw_actors_action = DrawActorsAction(output_service)
    handle_off_screen_action = Handle_Off_Screen_Action()
    handle_collisions_action = HandleCollisionsAction()

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action,handle_off_screen_action,handle_collisions_action]
    
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.
    audio_service.
    audio_service.
    
    director = Director(cast, script)
    director.start_game()

    audio_service.

if __name__ == "__main__":
    main()