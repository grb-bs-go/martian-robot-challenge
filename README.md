## Martian Robot Challenge
This Project was completed by Gavin Bayfield on 20 July 2025, within the specified time constraints of 3 hours. This development effort was completed using GitHub Codespaces, supported by GitHub Copilot, and provides a test suite to demonstrate that the project complies with the specific requirements outlined in the project description.

## Overview
The Martian Robot Challenge is a simulation of robots navigating the surface of Mars, represented as a rectangular grid. Each robot can move according to a set of instructions, and the program determines the final position of each robot after executing its commands. If a robot moves off the edge of the grid, it is considered "lost," and the program keeps track of these positions to prevent future robots from falling off at the same spot.

## Project Structure
```
martian-robot-challenge
├── src
│   ├── main.py                   # Entry point of the application
│   ├── robot.py                  # Defines the Robot class and its behaviors
│   ├── mars_grid.py              # Represents the Mars grid and manages boundaries
│   └── command_processor.py      # Processes robot commands
├── tests
│   ├── __init__.py               # Marks the tests directory as a package
│   ├── test_robot.py             # Unit tests for the Robot class
│   ├── test_mars_grid.py         # Unit tests for the MarsGrid class
│   └── test_command_processor.py # Unit tests for the CommandProcessor class
├── requirements.txt              # Lists project dependencies
└── README.md                     # Project documentation
```

## Robot Commands
- **L**: Turn left 90 degrees (remains on current grid point)
- **R**: Turn right 90 degrees (remains on current grid point)
- **F**: Move forward one grid point in current orientation

## Grid Rules
- Grid coordinates start at (0,0) in the lower-left corner
- Maximum coordinate values are specified in the first input line
- Robots that move off the edge are "lost" forever
- Lost robots leave a "scent" that prevents future robots from falling off at the same position
- Commands that would cause a robot to fall off from a scented position are ignored

## Constraints (if exceeded resulting in input validation error)
- Grid dimensions must not exceed 50 for either axis.
- Robot instruction string length must not exceed 100 characters.

## How to Run the Program
1. Clone the repository:
   ```
   git clone <repository-url>
   cd martian-robot-challenge
   ```

2. Install the required dependencies:
   ```
   pip3 install -r requirements.txt
   ```

3. Run the application:
   ```
   python3 src/main.py
   ```

## Input Format
Input Commands consists of multiple lines of input, pressing Enter once to send each command:
1. First, input the dimensions of the rectangular grid (represending the martian surface).
2. Then input two lines for robot, the first line providing its starting position, and the second line its movement instructions.
   Repeat this two line sequence to provide the input in the same format for each robot.
3. Signal end of input

When you run python3 src/main.py, the program will prompt you to enter input. You would enter:

Grid dimensions (first line), example: 5 3
Robot data (pairs of lines):
Robot position and orientation, example: 1 1 E
Robot instructions, example: RFRFRFRF
Next robot position, example: 3 2 N
Next robot instructions, example: FRRFLLFFRRFLL
And so on...
Ending Input Sequence
To end the command input sequence, use CTL+D (Linux/Mac) or CTL+Z (Win)

### Example Input
```
5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLFFFLFLFL
```

## Output Format
The output indicates the final position and orientation of each robot. If a robot is lost, the output will include the word "LOST."

### Example Output
```
1 1 E
3 3 N LOST
2 3 S
```

## Running Tests
To run all unit tests at once:
```bash
python3 -m unittest discover tests/ -v
```

To run individual test files:
```bash
python3 tests/test_robot.py
python3 tests/test_mars_grid.py
python3 tests/test_command_processor.py
```

To run tests with coverage (if coverage.py is installed):
```bash
python3 -m coverage run -m unittest discover tests/
python3 -m coverage report
```

## Future Enhancements
The project is designed to be extensible, allowing for the addition of new command types and features as needed.