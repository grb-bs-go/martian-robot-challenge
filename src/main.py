#
# Mars Robot Challenge
# Main Program is launch pad to Mars from src/main.py !
#
import sys
from mars_grid import MarsGrid
from robot import Robot
from command_processor import CommandProcessor

#
# Parse input from stdin and return grid and robot data
#
def parse_input():
    try:
        # Read grid dimensions
        grid_line = input().strip()
        try:
            max_x, max_y = map(int, grid_line.split())
        except ValueError:
            print("Invalid grid dimensions. Please enter two integers separated by a space.")
            return None, []
        
        if max_x > 50 or max_y > 50:
            raise ValueError("Grid dimensions must not exceed 50 for either axis.")        
        
        robots_data = []
        grid = MarsGrid(max_x, max_y)
        
        # Read robot data in pairs
        while True:
            try:
                # Read robot position and orientation
                position_line = input().strip()
                if not position_line:
                    continue
                    
                parts = position_line.split()
                x, y, orientation = int(parts[0]), int(parts[1]), parts[2]
                
                # Read robot instructions
                instructions = input().strip()
                
                # Check instruction string length
                if len(instructions) > 100:
                    raise ValueError(f"Robot instruction string length ({len(instructions)}) exceeds maximum of 100 characters.")
                
                robots_data.append((x, y, orientation, instructions))
                
            except EOFError:
                break
                
        return grid, robots_data
        
    except EOFError:
        return None, []

#
# Main function to run the Martian Robot Challenge
#
def main():
    """Run the Martian Robot Challenge"""
    print("Martian Robot Challenge")
    print("Enter grid dimensions e.g. 5 3")
    print("Then enter robot data as two lines")
    print("Enter each robot position and orientation e.g. 1 1 E")
    print("Followed by the specific instructions e.g. RFRFRFRF")
    print("And repeat for each new robot.")
    print("Press Ctrl+D (Linux/Mac) or Ctrl+Z (Windows) when done")
    print("Enter your input below:")
    
    try:
        grid, robots_data = parse_input()
        
        if grid is None:
            print("No input provided.")
            return
        
        command_processor = CommandProcessor()
        results = []
        
        # Process each robot sequentially
        for x, y, orientation, instructions in robots_data:
            robot = Robot(x, y, orientation, grid)
            command_processor.execute_commands(robot, instructions)
            results.append(str(robot))
        
        # Output results
        print("\nOutput:")
        for result in results:
            print(result)
            
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()