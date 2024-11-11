# Breakout Game

## Overview
Welcome to the **Breakout Game** project! This project is a simple, fun game implemented using Python and `pygame`, with a focus on Object-Oriented Programming (OOP) principles.

## Requirements

1. **Python**: Ensure you have Python 3.10 or later installed. You can check your Python version with:
```
python --version
```
If your Python version is < 3.10, you should go to this [link](https://www.python.org/downloads/) and click the download button. Once the download is complete, run the `.exe` file and follow the prompts to install the latest version. 


2. **Git**: Ensure you have Git installed. You can check if you do by running:
```
git --version
```
If you need to install Git download the installer from [Git for Windows](https://git-scm.com/download/win) and run the `.exe` file, following the prompts to complete the installation.


## Installation and Setup
To make the installation process easier, a script (`setup.sh`) has been provided to build and install the package. Run the following terminal commands in a `Git Bash` terminal to setup the project. 


- **Choosing the Right Directory**: Before cloning the repository, navigate to a directory where you want the project folder to be created. This directory will serve as the location for your project files. For example, if you want to keep all your projects in a folder called `Projects`, first navigate to that folder in Git Bash or your terminal, then proceed to clone the repository.

- **Using Git Bash Tips**: If you're using Git Bash on Windows, keep in mind:
  - Standard keyboard shortcuts like `Ctrl + C` and `Ctrl + V` don't work as expected.
  - To copy text, simply highlight the text in the terminal; it will automatically be copied.
  - To paste copied text, use the middle mouse button (scroll wheel) or right-click and select “Paste”.
  - You can also use the up and down arrow keys to cycle through previously used commands, which can save time when re-entering commands.

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

3. **Set the Python path**:
```
export PYTHONPATH=$(pwd)
```

4. **Run the script**:
```
./setup.sh
```

### What the `setup.sh` Script Does
- Builds the package using `python setup.py sdist bdist_wheel`.
- Installs the package locally with `pip install .`.
- Sets PYTHONPATH to the project root directory
- Cleans up build directories (`build/`, `dist/`, `*.egg-info`) after the build process is complete.

## Running the Game
Once the installation is complete, you can run the game with:
```
python src/breakout/breakout_game.py
```
