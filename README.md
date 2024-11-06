
# Breakout Game

## Overview
Welcome to the **Breakout Game** project! This project is a simple, fun game implemented using Python and `pygame` with a focus on Object-Oriented Programming (OOP) principles.

## Requirements
Ensure you have Python 3.10 or later installed. You can check your Python version with:
```
python --version
```

## Installation and Setup
To make the installation process easier, a script (`setup.sh`) has been provided to build and install the package.

## How to Run `setup.sh`
Follow these steps to build and install the `Breakout` game package:

1. **Clone the repository (if not already done)**:
```
git clone https://github.com/gknudtson/Breakout.git
cd Breakout
```

2. **Ensure the script has executable permissions**:
```
chmod +x setup.sh
```

3. **Run the script**:
```
./setup.sh
```

### What the `setup.sh` Script Does
- Builds the package using `python setup.py sdist bdist_wheel`.
- Installs the package locally with `pip install .`.
- Cleans up build directories (`build/`, `dist/`, `*.egg-info`) after the build process is complete.

## Running the Game
Once the installation is complete, you can run the game with:
```
python src/breakout/breakout_game.py
```
