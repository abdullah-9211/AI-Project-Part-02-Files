# Street-Fighter-AI-Project

Street fighter run on bizhawk emulator and automated using ML Models.

## Requirements

- Numpy
- Pandas
- Scikit-learn
- joblib

## Method to Install

pip install numpy pandas scikit-learn joblib

## How to use

- Run EmuHawk in single-player folder
- Open ROM and select "Street Fighter II Turbo (U).smc"
- Open Toolbox from Tools in menu above
- Open command prompt and navigate to the PythonAPI folder
- run "python controller.py 1"
- Select character to play and as soon as round begins, select second option in toolbox which is Gyroscope Bot
- This will connect the game with file and bot will start playing
- After round ends, bot disconnects
- Stop the gyro bot, run controller.py from command prompt again and press start
- Keep repeating this process to play more
- Make sure the .pkl files, controller.py and bot.py are all in the same folder.
- Model is loaded from .pkl file into bot.py
