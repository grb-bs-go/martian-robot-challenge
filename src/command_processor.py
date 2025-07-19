from typing import Dict, Callable

#
# CommandProcessor class to handle robot commands input by the user.
# This class allows for extensibility by registering new commands dynamically.
#
class CommandProcessor:

    # Initialize command processor with default commands
    def __init__(self):

        self.commands: Dict[str, Callable] = {
            'L': self._turn_left,
            'R': self._turn_right,
            'F': self._move_forward
        }

    #  Register a new command for future extensibility
    #
    # Args:
    #   command_char: Single character command identifier
    #    command_func: Function to execute for this command
    def register_command(self, command_char: str, command_func: Callable):
        self.commands[command_char] = command_func
    
    # Execute a string of commands on the given robot
    #
    # Args:
    #     robot: Robot instance to command
    #     instructions: String of command characters
    def execute_commands(self, robot, instructions: str):

        for instruction in instructions:
            if robot.is_lost:
                break  # Stop processing if robot is lost
            
            if instruction in self.commands:
                self.commands[instruction](robot)
            else:
                print(f"Warning: Unknown command '{instruction}' ignored")
    
    # Execute left turn command
    def _turn_left(self, robot):
        robot.turn_left()
    
    # Execute right turn command
    def _turn_right(self, robot):
        robot.turn_right()
    
    # Execute forward movement command
    def _move_forward(self, robot):
        robot.move_forward()

    # Get list of available command characters
    #
    # Returns:
    #     List of command characters
    def get_available_commands(self) -> list:
        return list(self.commands.keys())