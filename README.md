# Asteroids Game

A simple arcade-style Asteroids game built with Python and Pygame.

## Features

- Control a spaceship and shoot asteroids.
- Asteroids move and bounce around the screen.
- Score points by destroying asteroids.
- Game ends if your ship collides with an asteroid.
- Real-time graphics and keyboard controls.

## Requirements

- Python 3.x
- [Pygame](https://www.pygame.org/) library

## Installation

1. Clone this repository or download the source files.
2. Install Pygame:
    ```
    pip install pygame
    ```

## How to Run

From the project directory, run:

```
uv run main.py
```

## Controls

- **Arrow keys**: Move and rotate the spaceship.
- **Spacebar**: Shoot.

## Files

- `main.py`: Main game loop and logic.
- `player.py`: Player spaceship class.
- `asteroid.py`: Asteroid class.
- `asteroidfield.py`: Asteroid field manager.
- `shot.py`: Projectile class.
- `constants.py`: Game constants (screen size, colors, etc.).

## Scoring

- Destroying an asteroid gives you 100 points.
- Your current score is displayed at the top-left of the screen.

## License

This project is open source and free to use for educational purposes.