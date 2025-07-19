#
# Robot class for Mars Robot Challenge
# This class represents a robot that can move on a grid, turn, and handle being moving off the grid
# in which case it will be marked as lost. A scent is left at the position where it got lost, to prevent
# another robot from trying to move off the grid again from that position.
#
class Robot:
    
    # Define orientations in clockwise order to establish convention for orientation changes
    ORIENTATIONS = ['N', 'E', 'S', 'W']
    
    # Movement vectors for each orientation
    DIRECTION_VECTORS = {
        'N': (0, 1),   # North: y increases
        'E': (1, 0),   # East: x increases
        'S': (0, -1),  # South: y decreases
        'W': (-1, 0)   # West: x decreases
    }

    # Initialize robot with position, orientation, and grid
    # Args:
    #     x: Initial x coordinate
    #     y: Initial y coordinate
    #     orientation: Initial orientation (N, S, E, W)
    #     grid: MarsGrid instance for boundary checking
    def __init__(self, x: int, y: int, orientation: str, grid):

        self.x = x
        self.y = y
        self.orientation = orientation
        self.grid = grid
        self.is_lost = False
    
    # Turn robot 90 degrees left (counterclockwise)
    def turn_left(self):
        if self.is_lost:
            return
            
        current_index = self.ORIENTATIONS.index(self.orientation)
        self.orientation = self.ORIENTATIONS[(current_index - 1) % 4]
    
    # Turn robot 90 degrees right (clockwise)
    def turn_right(self):
        if self.is_lost:
            return
            
        current_index = self.ORIENTATIONS.index(self.orientation)
        self.orientation = self.ORIENTATIONS[(current_index + 1) % 4]
    
    # Move robot forward one step in current direction
    def move_forward(self):
        if self.is_lost:
            return
        
        # Calculate new position
        dx, dy = self.DIRECTION_VECTORS[self.orientation]
        new_x = self.x + dx
        new_y = self.y + dy
        
        # Check if new position is off the grid
        if not self.grid.is_valid_position(new_x, new_y):
            # Check if current position has scent (ignore move if it does)
            if not self.grid.has_scent(self.x, self.y):
                # Robot is lost, add scent at current position
                self.grid.add_scent(self.x, self.y)
                self.is_lost = True
            # If there's scent, ignore the move instruction
        else:
            # Valid move - update position
            self.x = new_x
            self.y = new_y
    
    # Get current position as tuple
    # Returns:
    #     Tuple of (x, y, orientation)
    def get_position(self) -> tuple:
        return (self.x, self.y, self.orientation)
    
    # String representation of robot's final position
    # Returns:
    #     String in format "x y orientation" or "x y orientation LOST"
    def __str__(self) -> str:
        result = f"{self.x} {self.y} {self.orientation}"
        if self.is_lost:
            result += " LOST"
        return result
    
    # Developer-friendly representation
    def __repr__(self) -> str:
        status = " (LOST)" if self.is_lost else ""
        return f"Robot(x={self.x}, y={self.y}, orientation='{self.orientation}'{status})"