# 🖱️ Random Square Clicks Python Script v2.0 💻

## Description

This Python script utilizes the `pyautogui` library to simulate random, human-like mouse clicks within a configurable square area centered on the screen.

It runs for a specified duration, performing bursts of clicks with randomized coordinates, number of clicks, and mouse movement speed. It introduces variable-length pauses between bursts and includes robust error handling and safe stop mechanisms. Provides real-time progress feedback.

## ✨ Key Features

* **Enhanced Simulation:** Emulates mouse clicks with variable-duration cursor movements for a more natural feel. 🎯
* **Configurable Area:** Clicks are confined to a square area centered on the screen, the size of which can be easily adjusted. 🔳
* **Customizable Duration:** Allows defining the total script execution time. ⏱️
* **Multiple Randomization Levels:**
    * Random click location within the area. 🎲
    * Random number of clicks per burst. 🔢
    * Random duration of pauses between bursts. ⏳
    * Random mouse movement speed. 💨
* **Real-time Feedback:** Displays a constantly updating status line showing:
    * Elapsed and total time. 📊
    * Total number of clicks performed. 🖱️
    * Duration of the next pause. ⏸️
* **Robustness and Safety:**
    * Clean handling of interruptions (`Ctrl+C`). 🛑
    * Activation of PyAutoGUI's Failsafe (move mouse to top-left corner). 🛡️
    * Catches unexpected errors during execution. ⚠️
    * Initial validation of area size against screen dimensions.
* **Easy Configuration:** All main parameters (duration, area size, pause/click/speed ranges) are adjusted via clear constants at the beginning of the script. 🔧

## Requirements

* **Python:** Version 3.6 or higher (recommended due to f-strings and type hints usage). 🐍
* **Libraries:** `pyautogui`.

## 🛠️ Installation

1.  **Ensure you have Python installed.** You can download it from [python.org](https://www.python.org/).
2.  **Install the `pyautogui` library:** Open your terminal or command prompt and run:
    ```bash
    pip install pyautogui
    ```
    * **Note:** `pyautogui` might have additional dependencies depending on your operating system (e.g., `python3-tk`, `python3-dev`, `libxtst-dev`, `scrot` on Debian/Ubuntu Linux; may require special permissions on macOS). Refer to the [PyAutoGUI documentation](https://pyautogui.readthedocs.io/en/latest/install.html) if you encounter issues.

## ⚙️ Configuration

Before running, you can adjust the script's parameters by editing the **Configuration Constants** near the beginning of the `.py` file:

* `TOTAL_RUN_TIME_SECONDS`: Total duration in seconds the script will be active.
* `MIN_WAIT_SECONDS` / `MAX_WAIT_SECONDS`: Range (minimum and maximum) for pause durations in seconds.
* `SQUARE_AREA_SIZE`: Size (in pixels) of the side of the square where clicks will occur.
* `MIN_CLICKS_PER_BURST` / `MAX_CLICKS_PER_BURST`: Range for the number of clicks in each burst.
* `MIN_MOUSE_MOVE_DURATION` / `MAX_MOUSE_MOVE_DURATION`: Range for the duration (in seconds) of the mouse movement for each click.

## ▶️ Usage

1.  **Save the code** into a file, for example, `random_clicker.py`.
2.  **Open your terminal** or command prompt.
3.  **Navigate to the directory** where you saved the file.
4.  **Run the script** using the command:
    ```bash
    python random_clicker.py
    ```
5.  The script will start, display the welcome message, and then show the updating status line.

## 🛑 How to Stop the Script

You can safely stop the script at any time using one of these methods:

1.  **Press `Ctrl + C`** in the terminal where the script is running.
2.  **Activate the PyAutoGUI Failsafe:** Quickly move your mouse cursor to the top-left corner of your primary screen.

---

Feel free to modify and adapt the script to your needs! 🚀