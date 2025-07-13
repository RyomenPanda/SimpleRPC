# SimpleRPC

A desktop Rock, Paper, Scissors game implemented in Python with an intelligent AI opponent and modern GUI interface.

## Overview

SimpleRPC is a standalone desktop application that implements the classic Rock, Paper, Scissors game with four AI difficulty levels ranging from random play to perfect strategic play. The system features a graphical user interface with visual feedback and comprehensive asset management capabilities.

## Features

- **Four AI Difficulty Levels:**
  - Easy: Random AI opponent
  - Normal: Probability-based AI with strategic elements
  - Hard: Advanced probability-based AI
  - Impossible: Perfect strategic AI that always wins

- **Modern GUI Interface:**
  - Dual-window system (difficulty selection and game interface)
  - Visual asset integration with PNG graphics
  - Interactive button system with hover states

- **Asset Management:**
  - Bundled visual assets for all game elements
  - Automatic path resolution for development and compiled environments
  - Support for standalone executable distribution

## System Architecture

The application follows a layered architecture with clear separation between presentation, logic, and resource management:

- **Presentation Layer:** `rps_gui.py` - GUI components and window management
- **Logic Layer:** `rps_logic.py` - Game logic and AI implementations
- **Resource Management:** Asset handling and path resolution

## Installation

### Prerequisites

- Python 3.x
- tkinter (usually included with Python)
- ttkbootstrap
- PIL/Pillow
- random (standard library)

### Setup

1. Clone the repository
2. Install required dependencies:
   ```bash
   pip install ttkbootstrap pillow
   ```
3. Run the application:
   ```bash
   python rps_gui.py
   ```

## Usage

1. **Launch Application:** Run the main GUI file to start the game
2. **Select Difficulty:** Choose from Easy, Normal, Hard, or Impossible AI opponents
3. **Play Game:** Click Rock, Paper, or Scissors buttons to make your choice
4. **View Results:** See the outcome and play again or change difficulty

## File Structure

```
SimpleRPC/
├── rps_gui.py          # Main GUI implementation
├── rps_logic.py        # Game logic and AI algorithms
├── assets/             # Visual assets directory
│   ├── easy.png        # Easy difficulty icon
│   ├── normal.png      # Normal difficulty icon
│   ├── hard.png        # Hard difficulty icon
│   ├── impossible.png  # Impossible difficulty icon
│   ├── rock.png        # Rock choice icon
│   ├── paper.png       # Paper choice icon
│   ├── scissors.png    # Scissors choice icon
│   ├── btn_normal.png  # Normal button state
│   ├── btn_hover.png   # Button hover state
│   └── splashimage.png # Application splash screen
├── LICENSE             # GPL v3 license
└── README.md           # This file
```

## Core Components

### GUI System (`rps_gui.py`)
- `windowstart()`: Difficulty selection interface
- `windowgame()`: Main game interface  
- `setup_game_buttons()`: Game button initialization
- `resource_path()`: Asset path resolution for bundled executables

### Game Logic (`rps_logic.py`)
- `rps_play()`: Main game execution controller
- `diff_easy()`: Easy AI implementation (random)
- `diff_normal()`: Normal AI with probability events
- `diff_hard()`: Hard AI with advanced probability
- `diff_impossible()`: Perfect AI that always wins
- `move_check()`: Game result calculation

## AI Difficulty Details

- **Easy:** Completely random opponent choices
- **Normal:** Uses probability events with some strategic elements
- **Hard:** Advanced probability-based decision making
- **Impossible:** Strategic AI that analyzes player patterns for guaranteed wins

## Building Standalone Executable

The application is designed for compilation into standalone executables using tools like PyInstaller:

```bash
pyinstaller --onefile --windowed --add-data "assets;assets" rps_gui.py
```

The `resource_path()` function automatically handles asset resolution in both development and compiled environments.

## License

This project is licensed under the GNU General Public License v3.0. [1](#1-0) 

## Contributing

This is free software distributed under GPL v3. [2](#1-1)  You are free to redistribute and modify the software under the terms of the license.

## Technical Requirements

- Compatible with Windows, macOS, and Linux
- Requires Python 3.x runtime (or standalone executable)
- Minimal system requirements for GUI applications
