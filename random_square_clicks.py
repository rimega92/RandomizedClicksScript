import pyautogui
import time
import random

# Define the time in seconds for the script to run
TOTAL_TIME_SECONDS = 1 * 60 * 60  # (Hours * Minutes * Seconds)

# Define the range of random waiting time in seconds
WAIT_RANGE_MIN = 0
WAIT_RANGE_MAX = 30

# Get screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

# Define square dimensions
SQUARE_SIZE = 500
POSITION_X = int((SCREEN_WIDTH - SQUARE_SIZE) / 2)
POSITION_Y = int((SCREEN_HEIGHT - SQUARE_SIZE) / 2)

# Check that coordinates are within the square
def check_bounds(x, y):
    x = max(POSITION_X, min(POSITION_X + SQUARE_SIZE, x))
    y = max(POSITION_Y, min(POSITION_Y + SQUARE_SIZE, y))
    return x, y

# Get the elapsed time in hours:minutes:seconds format
def get_elapsed_time(time):
    time_hours = int(time // 3600)
    time_minutes = int((time % 3600) // 60)
    time_seconds = int(time % 60)
    return time_hours, time_minutes, time_seconds

def print_welcome_message():
    print("================================================")
    print("🖱️ Welcome to the Random Square Clicks Script 💻")
    print("================================================")

# Main function
def main():
    clicks_made = 0
    start_time = time.time()

    print_welcome_message()

    while (time.time() - start_time) < TOTAL_TIME_SECONDS:
        # Generate random click coordinates within the square
        x = random.randint(POSITION_X, POSITION_X + SQUARE_SIZE)
        y = random.randint(POSITION_Y, POSITION_Y + SQUARE_SIZE)

        # Verify and adjust coordinates if they're outside the square
        x, y = check_bounds(x, y)

        # Move the cursor to the coordinates and perform a click
        pyautogui.moveTo(x, y)
        pyautogui.click()
        clicks_made += 1

        # Calculate elapsed time and format it
        elapsed_time = time.time() - start_time
        hours, minutes, seconds = get_elapsed_time(elapsed_time)

        # Generate a random pause time and display information
        pause_time = random.uniform(WAIT_RANGE_MIN, WAIT_RANGE_MAX)
        message = (f"Clicks made: {clicks_made} | Elapsed time: "
                   f"{hours:02d}:{minutes:02d}:{seconds:02d} | "
                   f"Pause time: {pause_time:.2f} seconds.")
        print(message)
        time.sleep(pause_time)

    print("Script finished")

if __name__ == "__main__":
    main()
