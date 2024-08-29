# Keylogger with Discord Integration

## Introduction

This project is an educational keylogger that captures keystrokes on a system and sends the logged data to a specified Discord channel once a day. The keylogger is written in Python using the `pynput` library to capture keystrokes and the `requests` library to send data to Discord. The log file is cleared after every successful send, ensuring efficient log management.

## Features

- **Keystroke Logging**: Captures and logs all keystrokes, including handling for special keys like space and Enter.
- **Discord Integration**: Sends the captured keystrokes to a specified Discord channel once a day.
- **Log Management**: The log file is deleted and recreated after being sent to Discord, preventing log file bloat.
- **Customizable**: Easily change the logging interval and the Discord channel details.
- **Multi-threaded**: Utilizes threading to handle keylogging, log saving, and sending the logs simultaneously without blocking the main program.

## Usage
If don't want to use discord intergration use the normal **./SimpleKeylogger.py**

### Prerequisites

Before you can run this keylogger, you need to have Python installed on your system. Additionally, you'll need to install the required Python libraries:

```bash
pip install pynput requests discord.py
```

### Setting Up the Discord Bot

1. Create a Discord Application:
- Go to the Discord Developer Portal.
- Click on New Application.
- Give your application a name and click Create.

2. Create a Bot:
- In your new application, navigate to the Bot tab.
- Click on Add Bot.
- Confirm by clicking Yes, do it!.

3. Get the Bot Token:
- Under the Token section, click Copy to copy your bot's token. Save this token securely as you will need it in your Python script.

4. Invite the Bot to Your Server:
- Go to the OAuth2 tab in your application.
- Under OAuth2 URL Generator, select bot under SCOPES.
- Under BOT PERMISSIONS, select Send Messages.
- Copy the generated URL and paste it into your browser.
- Select the server you want to add the bot to and click Authorize.

5. Get the Channel ID:
- Go to your Discord server and right-click on the channel where you want the bot to send messages.
- Click on Copy ID. If you don't see this option, you'll need to enable Developer Mode in Discord's settings:
- Go to User Settings > Advanced > Developer Mode > Enable.

6. Update the Script:
- Replace the placeholders in the script with your Discord bot token and channel ID:
```python
discord_bot_token = 'your_bot_token'
channel_id = 'your_channel_id'
```

## Running the Keylogger
Simply run the Python script:
```bash
python keylogger.py
```
The keylogger will start capturing keystrokes and saving them to key_log.txt. Every day, it will send the log file to the specified Discord channel and then clear the log file.

## Logging Format
Spaces: Captured as regular spaces in the log file.
Enter Key: Logs are separated into new lines whenever the Enter key is pressed.
Special Keys: Some special keys like Ctrl are ignored in the log.

### Example Log
```bash
Hello World
This is a test log.
```
## Error Handling
### Common Errors
1. Invalid Discord Token or Channel ID:
- Error: "Failed to send log file: 401"
- Solution: Ensure that the Discord bot token and channel ID are correctly set.

2. Failed to Send Log:
- Error: "Failed to send log file: 403" or other HTTP status codes.
- Solution: Check the bot's permissions in the Discord server, particularly the permission to send messages in the specified channel.

### Troubleshooting
- Log File Not Being Created: Ensure the script has write permissions in the directory where it's being run.
- Keystrokes Not Being Logged: Ensure no other application is interfering with keyboard inputs.

## Purpose
The purpose of this project is purely educational, to demonstrate how keystrokes can be captured and logged using Python. It's intended for students learning about keylogging, cybersecurity practices, and Python programming. It should not be used for unethical purposes.

## Disclaimer
Warning: This keylogger is for educational purposes only. Unauthorized use of keyloggers to monitor other individuals' activities without their consent is illegal and unethical. Always ensure you have permission from the user of the system you are monitoring.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.