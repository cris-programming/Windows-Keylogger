# Keystroke and Screen Activity Monitoring Script

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/open-source.svg)

This Python script monitors keystrokes, captures active window titles, and takes screenshots of specific browsers. It is designed for various purposes, such as computer usage tracking or debugging.

## Features

- Keystroke monitoring and logging.
- Detection of specific browser windows and capturing screenshots.
- Thread-safe file operations for log file.
- Configurable parameters for monitoring.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages (install using `pip`):
  - pynput
  - pyautogui
  - pygetwindow

### Usage

1. Clone this repository or download the script.

2. Install the required Python packages:

   ```bash
   pip install pynput pyautogui pygetwindow
   ```

3. Run the script:

   ```bash
   python Klogger.pyw
   ```

   The script will start monitoring keystrokes and active windows, logging the activity to a text file and capturing screenshots of specified browsers.

## Configuration

You can customize the script by modifying the following parameters in the script file:

- `seconds`: The interval (in seconds) at which active windows are monitored.
- `browser_names`: A list of browser names to detect and capture screenshots of.

## Logging

The script logs keystrokes and active window titles to a text file named with the current date. Screenshots are saved with random names in the script's directory.

## Legal and Ethical Considerations

Please use this script responsibly and ensure that you comply with all applicable laws and regulations. Monitoring computer activity should be done with the consent of the user and for legitimate purposes.

## Acknowledgments

- [pynput](https://github.com/moses-palmer/pynput) - Python library for controlling and monitoring input devices.
- [pyautogui](https://github.com/asweigart/pyautogui) - Python library for GUI automation tasks.
- [pygetwindow](https://github.com/asweigart/pygetwindow) - Python library for controlling and querying window properties.
