import unittest
import sys
import os
import io
from unittest.mock import patch

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import parse_input


class TestInputValidation(unittest.TestCase):
    """Test cases for input validation in main.py"""
    
    def test_grid_dimension_exceeds_50_x(self):
        """Test that ValueError is raised when x dimension exceeds 50"""
        with patch('builtins.input', side_effect=['51 30']):
            with self.assertRaises(ValueError) as context:
                parse_input()
            self.assertIn("Grid dimensions must not exceed 50", str(context.exception))
    
    def test_grid_dimension_exceeds_50_y(self):
        """Test that ValueError is raised when y dimension exceeds 50"""
        with patch('builtins.input', side_effect=['30 51']):
            with self.assertRaises(ValueError) as context:
                parse_input()
            self.assertIn("Grid dimensions must not exceed 50", str(context.exception))
    
    def test_grid_dimension_exceeds_50_both(self):
        """Test that ValueError is raised when both dimensions exceed 50"""
        with patch('builtins.input', side_effect=['51 51']):
            with self.assertRaises(ValueError) as context:
                parse_input()
            self.assertIn("Grid dimensions must not exceed 50", str(context.exception))
    
    def test_valid_grid_dimensions_at_boundary(self):
        """Test that valid dimensions at boundary (50, 50) work correctly"""
        with patch('builtins.input', side_effect=['50 50', EOFError()]):
            grid, robots_data = parse_input()
            self.assertIsNotNone(grid)
            self.assertEqual(grid.max_x, 50)
            self.assertEqual(grid.max_y, 50)
            self.assertEqual(len(robots_data), 0)
    
    def test_instruction_string_exceeds_100_chars(self):
        """Test that ValueError is raised when instruction string exceeds 100 characters"""
        long_instructions = 'F' * 101  # 101 characters
        input_sequence = ['5 3', '1 1 E', long_instructions]
        
        with patch('builtins.input', side_effect=input_sequence):
            with self.assertRaises(ValueError) as context:
                parse_input()
            self.assertIn("instruction string length", str(context.exception))
            self.assertIn("exceeds maximum of 100", str(context.exception))
    
    def test_valid_instruction_string_at_boundary(self):
        """Test that instruction string of exactly 100 characters is valid"""
        instructions_100 = 'F' * 100  # Exactly 100 characters
        input_sequence = ['5 3', '1 1 E', instructions_100, EOFError()]
        
        with patch('builtins.input', side_effect=input_sequence):
            grid, robots_data = parse_input()
            self.assertIsNotNone(grid)
            self.assertEqual(len(robots_data), 1)
            self.assertEqual(robots_data[0][3], instructions_100)
    
    def test_invalid_grid_format(self):
        """Test handling of invalid grid dimension format"""
        with patch('builtins.input', side_effect=['invalid input']):
            grid, robots_data = parse_input()
            self.assertIsNone(grid)
            self.assertEqual(len(robots_data), 0)
    
    def test_valid_input_processing(self):
        """Test that valid input is processed correctly"""
        input_sequence = [
            '5 3',           # Grid dimensions
            '1 1 E',         # Robot 1 position
            'RFRFRFRF',      # Robot 1 instructions
            '3 2 N',         # Robot 2 position
            'FRRFLLFFRRFLL', # Robot 2 instructions
            EOFError()       # End of input
        ]
        
        with patch('builtins.input', side_effect=input_sequence):
            grid, robots_data = parse_input()
            
            self.assertIsNotNone(grid)
            self.assertEqual(grid.max_x, 5)
            self.assertEqual(grid.max_y, 3)
            self.assertEqual(len(robots_data), 2)
            
            # Verify first robot data
            self.assertEqual(robots_data[0], (1, 1, 'E', 'RFRFRFRF'))
            
            # Verify second robot data
            self.assertEqual(robots_data[1], (3, 2, 'N', 'FRRFLLFFRRFLL'))


if __name__ == '__main__':
    unittest.main()