import unittest
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from robot import Robot
from mars_grid import MarsGrid
from command_processor import CommandProcessor


class TestRobot(unittest.TestCase):
    """Test cases for Robot class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.grid = MarsGrid(5, 3)
    
    def test_robot_initialization(self):
        """Test robot initialization"""
        robot = Robot(1, 1, 'E', self.grid)
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 1)
        self.assertEqual(robot.orientation, 'E')
        self.assertFalse(robot.is_lost)
        self.assertEqual(robot.grid, self.grid)
    
    def test_turn_left(self):
        """Test left turn functionality"""
        robot = Robot(1, 1, 'N', self.grid)
        
        robot.turn_left()
        self.assertEqual(robot.orientation, 'W')
        
        robot.turn_left()
        self.assertEqual(robot.orientation, 'S')
        
        robot.turn_left()
        self.assertEqual(robot.orientation, 'E')
        
        robot.turn_left()
        self.assertEqual(robot.orientation, 'N')
    
    def test_turn_right(self):
        """Test right turn functionality"""
        robot = Robot(1, 1, 'N', self.grid)
        
        robot.turn_right()
        self.assertEqual(robot.orientation, 'E')
        
        robot.turn_right()
        self.assertEqual(robot.orientation, 'S')
        
        robot.turn_right()
        self.assertEqual(robot.orientation, 'W')
        
        robot.turn_right()
        self.assertEqual(robot.orientation, 'N')
    
    def test_move_forward_valid(self):
        """Test valid forward movement"""
        # Test moving north
        robot = Robot(1, 1, 'N', self.grid)
        robot.move_forward()
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 2)
        self.assertFalse(robot.is_lost)
        
        # Test moving east
        robot = Robot(1, 1, 'E', self.grid)
        robot.move_forward()
        self.assertEqual(robot.x, 2)
        self.assertEqual(robot.y, 1)
        self.assertFalse(robot.is_lost)
    
    def test_move_forward_lost(self):
        """Test robot getting lost when moving off grid"""
        robot = Robot(5, 3, 'N', self.grid)
        robot.move_forward()
        
        # Robot should be lost and scent should be added
        self.assertTrue(robot.is_lost)
        self.assertTrue(self.grid.has_scent(5, 3))
        
        # Position should remain at last valid position
        self.assertEqual(robot.x, 5)
        self.assertEqual(robot.y, 3)
    
    def test_scent_prevents_loss(self):
        """Test that scent prevents robot from getting lost"""
        # First robot gets lost
        robot1 = Robot(5, 3, 'N', self.grid)
        robot1.move_forward()
        self.assertTrue(robot1.is_lost)
        
        # Second robot at same position doesn't get lost due to scent
        robot2 = Robot(5, 3, 'N', self.grid)
        robot2.move_forward()
        self.assertFalse(robot2.is_lost)
        self.assertEqual(robot2.x, 5)
        self.assertEqual(robot2.y, 3)
    
    def test_lost_robot_ignores_commands(self):
        """Test that lost robot ignores further commands"""
        robot = Robot(5, 3, 'N', self.grid)
        robot.move_forward()  # Robot gets lost
        
        original_orientation = robot.orientation
        robot.turn_left()
        robot.turn_right()
        robot.move_forward()
        
        # Robot should ignore all commands after being lost
        self.assertEqual(robot.orientation, original_orientation)
        self.assertTrue(robot.is_lost)
    
    def test_string_representation(self):
        """Test string representation of robot"""
        # Normal robot
        robot = Robot(1, 2, 'N', self.grid)
        self.assertEqual(str(robot), "1 2 N")
        
        # Lost robot
        robot = Robot(5, 3, 'N', self.grid)
        robot.move_forward()  # Gets lost
        self.assertEqual(str(robot), "5 3 N LOST")
    
    def test_get_position(self):
        """Test position retrieval"""
        robot = Robot(3, 2, 'W', self.grid)
        position = robot.get_position()
        self.assertEqual(position, (3, 2, 'W'))
    
    def test_sample_input_output(self):
        """Test complete sample input produces expected output
        
        Sample Input:
        5 3
        1 1 E
        RFRFRFRF
        3 2 N
        FRRFLLFFRRFLL
        0 3 W
        LLFFFLFLFL
        
        Expected Output:
        1 1 E
        3 3 N LOST
        2 3 S
        """
        # Create grid matching sample input (5 3)
        grid = MarsGrid(5, 3)
        command_processor = CommandProcessor()
        results = []
        
        # Robot 1: Position (1, 1, E), Instructions: RFRFRFRF
        robot1 = Robot(1, 1, 'E', grid)
        command_processor.execute_commands(robot1, "RFRFRFRF")
        results.append(str(robot1))
        
        # Robot 2: Position (3, 2, N), Instructions: FRRFLLFFRRFLL
        robot2 = Robot(3, 2, 'N', grid)
        command_processor.execute_commands(robot2, "FRRFLLFFRRFLL")
        results.append(str(robot2))
        
        # Robot 3: Position (0, 3, W), Instructions: LLFFFLFLFL
        robot3 = Robot(0, 3, 'W', grid)
        command_processor.execute_commands(robot3, "LLFFFLFLFL")
        results.append(str(robot3))
        
        # Verify expected output
        expected_output = ["1 1 E", "3 3 N LOST", "2 3 S"]
        self.assertEqual(results, expected_output)
        
        # Additional verification of individual robot states
        self.assertEqual(robot1.x, 1)
        self.assertEqual(robot1.y, 1)
        self.assertEqual(robot1.orientation, 'E')
        self.assertFalse(robot1.is_lost)
        
        self.assertEqual(robot2.x, 3)
        self.assertEqual(robot2.y, 3)
        self.assertEqual(robot2.orientation, 'N')
        self.assertTrue(robot2.is_lost)
        
        self.assertEqual(robot3.x, 2)
        self.assertEqual(robot3.y, 3)
        self.assertEqual(robot3.orientation, 'S')
        self.assertFalse(robot3.is_lost)


if __name__ == '__main__':
    unittest.main()