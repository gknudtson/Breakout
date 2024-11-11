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

- **Git Bash Tips**:
  - Standard keyboard shortcuts like `Ctrl + C` and `Ctrl + V` don't work as expected.
  - To copy text, simply highlight the text in the terminal; it will automatically be copied.
  - To paste copied text, use the middle mouse button (scroll wheel) or right-click and select “Paste”.
  - You can also use the up and down arrow keys to cycle through previously used commands, which can save time when re-entering commands.

## How to Run `setup.sh`
Follow these steps to build and install the `Breakout` game package:

1. **Set up a project folder**:
```
mkdir python_projects
cd python_projects
```

2. **Clone the repository (if not already done)**:
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
- Installs the setup tools package using pip.
- Builds the package using `python setup.py sdist bdist_wheel`.
- Installs the package locally with `pip install .`.
- Cleans up build directories (`build/`, `dist/`, `*.egg-info`) after the build process is complete.

## Running the Game

Each time you want to run the game ensure all files are saved (`Ctrl + S`). To start the game, use the following command in the terminal:

```bash
python src/breakout/breakout_game.py
```

### Running in VSCode

If you'd like to set up a launch configuration in VSCode for easier access, follow these steps:

1. Create a `launch.json` file in a `.vscode` directory at the root of your project:
   ```bash
   mkdir .vscode
   touch .vscode/launch.json
   ```

2. Open `launch.json` and paste in the following configuration:
```
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Breakout Game",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/src/breakout/breakout_game.py",
      "console": "integratedTerminal",
      "cwd": "${workspaceFolder}",
      "env": {
        "PYTHONPATH": "${workspaceFolder}"
      }
    }
  ]
}
```
3. To run the game press `f5`.
