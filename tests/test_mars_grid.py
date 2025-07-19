import unittest
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from mars_grid import MarsGrid


class TestMarsGrid(unittest.TestCase):
    """Test cases for MarsGrid class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.grid = MarsGrid(5, 3)
    
    def test_initialization(self):
        """Test grid initialization"""
        self.assertEqual(self.grid.max_x, 5)
        self.assertEqual(self.grid.max_y, 3)
        self.assertEqual(len(self.grid.scent_positions), 0)
    
    def test_valid_positions(self):
        """Test valid position checking"""
        # Corner positions
        self.assertTrue(self.grid.is_valid_position(0, 0))
        self.assertTrue(self.grid.is_valid_position(5, 3))
        self.assertTrue(self.grid.is_valid_position(0, 3))
        self.assertTrue(self.grid.is_valid_position(5, 0))
        
        # Middle positions
        self.assertTrue(self.grid.is_valid_position(2, 1))
        self.assertTrue(self.grid.is_valid_position(3, 2))
    
    def test_invalid_positions(self):
        """Test invalid position checking"""
        # Negative coordinates
        self.assertFalse(self.grid.is_valid_position(-1, 0))
        self.assertFalse(self.grid.is_valid_position(0, -1))
        self.assertFalse(self.grid.is_valid_position(-1, -1))
        
        # Beyond grid boundaries
        self.assertFalse(self.grid.is_valid_position(6, 3))
        self.assertFalse(self.grid.is_valid_position(5, 4))
        self.assertFalse(self.grid.is_valid_position(6, 4))
    
    def test_scent_functionality(self):
        """Test scent tracking functionality"""
        # Initially no scent
        self.assertFalse(self.grid.has_scent(2, 2))
        
        # Add scent
        self.grid.add_scent(2, 2)
        self.assertTrue(self.grid.has_scent(2, 2))
        
        # Check other positions still have no scent
        self.assertFalse(self.grid.has_scent(1, 1))
        self.assertFalse(self.grid.has_scent(3, 3))
    
    def test_get_dimensions(self):
        """Test dimension retrieval"""
        dimensions = self.grid.get_dimensions()
        self.assertEqual(dimensions, (5, 3))


if __name__ == '__main__':
    unittest.main()