# Keep-Active-Scripts

This repository contains two scripts that help prevent your computer from going idle by simulating mouse and keyboard activity.

## Scripts

1. `always_active_mouse.py`: This script uses the `pyautogui` library to move the mouse every 10 seconds.

2. `always_active_kb.py`: This script uses the `pyautogui` library to simulate keyboard activity every 10 seconds.

## How to use

1. Make sure you have `pyautogui` installed. If not, you can install it by running `pip install pyautogui` or `pip3 install pyautogui`

2. Run the script by typing `python always_active_mouse.py` or `python3 always_active_mouse.py` in the terminal.

3. Run the script by typing `python always_active_kb.py` or `python3 always_active_kb.py` in the terminal.

## Note

The scripts are set to move the mouse or simulate keyboard activity every 10 seconds by default, but you can adjust the time interval by changing the `time.sleep()` function in the script.

The scripts will keep running until you stop them manually by pressing `CTRL + C`.

The `pyautogui` library is used to simulate mouse and keyboard activity, refer to the pyautogui documentation for more information on how to use it.

