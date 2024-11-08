# Color Match Game

Color Match Game is an engaging Pygame-based game where players control a sphere and match its color to falling objects to earn points. As objects fall, the player must strategically change the sphere's color to match the objects and increase their score. This game features bouncing objects and a simple game-over mechanism, challenging players to improve their color-matching skills over time.

## Features
- **Interactive Gameplay**: Control a sphere that can move left and right and change colors to match falling objects.
- **Bouncing Objects**: Falling objects bounce off screen edges, adding an extra challenge.
- **Score Tracking**: Players earn points by successfully matching the sphere's color with falling objects.
- **Game Over and Restart**: A game-over screen shows the final score and provides an option to restart the game.
- **Difficulty levels**: Players can select their preferred difficulty level, which include: easy, medium and hard.

## Project Structure
Here is the structure of the project directory:
```
ColorMatchGame/
├── color_match.py         
├── GitHubLink.txt          
├── README.md               
├── requirements.txt       
```
## Gameplay
- **Move the Sphere**: Use the `left` and `right` arrow keys to move the sphere horizontally.
- **Change Sphere Color**: Press the `Space key` or left-click on the sphere to change its color.
- **Match Colors**: Match the sphere’s color with falling objects to earn points. Avoid mismatches, as they reduce lives. Losing all lives ends the game.
- **Difficulty Selection**: At the start of the game, choose a difficulty level (Easy, Medium, or Hard), which affects the speed and frequency of falling objects.
- **Pause/Resume**: Click the `Pause` button in the top-right corner to pause or resume the game.
- **Restart**: After a game over, click the `Restart` button to play again with a reset score and lives.

## Controls
- **Left Arrow Key**: Move sphere left
- **Right Arrow Key**: Move sphere right
- **Space Key**: Change sphere color
- **Pause Button**: pause the game.
- **Play Button**: resume the game.
- **Restart Button**: restarts the game.

## Installation and Setup
1. Install pycharm

2. Ensure you have Python and Pygame installed.
   ```bash
   pip install pygame
   ```
3. Download or clone the repository:
   ```bash
   git clone https://github.com/joyyy-99/ColorMatchGame.git
   ```
4. Install the Required libraries from requirements.txt:
    ```bash
   pip install -r requirements.txt
   ```
5. Navigate to the project directory and run the game:
   ```bash
   cd ColorMatchGame
   python color_match.py
   ```

## Requirements
- Python 3.x
- Pygame library



