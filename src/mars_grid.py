#
# This class represents the Mars surface grid with boundaries and supports scent tracking
# to prevent multiple robots from getting lost from the same position.
#
class MarsGrid:
    # Initialize Mars grid with given dimensions
    #
    # Args:
    #     max_x: Maximum x coordinate (upper-right corner)
    #     max_y: Maximum y coordinate (upper-right corner)
    #
    def __init__(self, max_x: int, max_y: int):

        self.max_x = max_x
        self.max_y = max_y
        self.scent_positions = set()  # Record positions where robots were lost

    # Check if position is within grid bounds
    #
    # Args:
    #     x: X coordinate
    #     y: Y coordinate
    #
    # Returns:
    #     True if position is within bounds, False otherwise
    def is_valid_position(self, x: int, y: int) -> bool:

        return 0 <= x <= self.max_x and 0 <= y <= self.max_y

    # Check if position has robot scent (previous robot was lost here)
    #
    # Args:
    #     x: X coordinate
    #     y: Y coordinate
    #
    # Returns:
    #     True if position has scent, False otherwise
    def has_scent(self, x: int, y: int) -> bool:
        return (x, y) in self.scent_positions

    # Add robot scent at given position
    #
    # Args:
    #     x: X coordinate
    #     y: Y coordinate
    #
    def add_scent(self, x: int, y: int):
        self.scent_positions.add((x, y))

    # Get grid dimensions
    #    
    #    Returns:
    #        Tuple of (max_x, max_y)
    def get_dimensions(self) -> tuple:
        return (self.max_x, self.max_y)