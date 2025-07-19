import unittest
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from command_processor import CommandProcessor
from robot import Robot
from mars_grid import MarsGrid


class TestCommandProcessor(unittest.TestCase):
    """Test cases for CommandProcessor class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.grid = MarsGrid(5, 3)
        self.processor = CommandProcessor()
    
    def test_initialization(self):
        """Test command processor initialization"""
        commands = self.processor.get_available_commands()
        self.assertIn('L', commands)
        self.assertIn('R', commands)
        self.assertIn('F', commands)
        self.assertEqual(len(commands), 3)
    
    def test_execute_basic_commands(self):
        """Test execution of basic commands"""
        robot = Robot(1, 1, 'E', self.grid)
        
        # Test the sample input sequence
        self.processor.execute_commands(robot, "RFRFRFRF")
        
        # Should end up at (1, 1, E)
        self.assertEqual(str(robot), "1 1 E")
    
    def test_execute_commands_with_loss(self):
        """Test command execution when robot gets lost"""
        robot = Robot(3, 2, 'N', self.grid)
        
        # This should make the robot lost
        self.processor.execute_commands(robot, "FRRFLLFFRRFLL")
        
        # Should end up lost
        self.assertTrue(robot.is_lost)
        self.assertEqual(str(robot), "3 3 N LOST")
    
    def test_sample_input_complete(self):
        """Test complete sample input scenario"""
        results = []
        
        # Robot 1
        robot1 = Robot(1, 1, 'E', self.grid)
        self.processor.execute_commands(robot1, "RFRFRFRF")
        results.append(str(robot1))
        
        # Robot 2
        robot2 = Robot(3, 2, 'N', self.grid)
        self.processor.execute_commands(robot2, "FRRFLLFFRRFLL")
        results.append(str(robot2))
        
        # Robot 3
        robot3 = Robot(0, 3, 'W', self.grid)
        self.processor.execute_commands(robot3, "LLFFFLFLFL")
        results.append(str(robot3))
        
        # Check expected results
        expected = ["1 1 E", "3 3 N LOST", "2 3 S"]
        self.assertEqual(results, expected)
    
    def test_register_new_command(self):
        """Test registering a new command for extensibility"""
        def backward_command(robot):
            # Turn around and move forward
            robot.turn_right()
            robot.turn_right()
            robot.move_forward()
            robot.turn_right()
            robot.turn_right()
        
        # Register new command
        self.processor.register_command('B', backward_command)
        
        # Test new command
        robot = Robot(2, 2, 'N', self.grid)
        self.processor.execute_commands(robot, "B")
        
        # Should have moved south (backward from north)
        self.assertEqual(robot.x, 2)
        self.assertEqual(robot.y, 1)
        self.assertEqual(robot.orientation, 'N')
    
    def test_unknown_command_handling(self):
        """Test handling of unknown commands"""
        robot = Robot(1, 1, 'N', self.grid)
        
        # This should not crash and should ignore unknown command
        self.processor.execute_commands(robot, "LXRF")
        
        # Should have executed L, ignored X, executed R and F
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 2)
        self.assertEqual(robot.orientation, 'N')


if __name__ == '__main__':
    unittest.main()
