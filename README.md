# Telegram Add or Invite Contact Bot

This project consists of Python scripts to interact with the Telegram API for adding or inviting contacts to a channel and sending messages to specified recipients.

## Prerequisites

Before running the scripts, ensure you have the following:

- Python 3.x installed on your system.
- Required Python packages installed:
  - `telethon`
  - `vobject`

## Setup

1. Clone this repository to your local machine.

2. Install the required Python packages using pip:

```bash
pip install telethon vobject
```

## Usage

### TelegramContactAdderBot_main.py

This script is used to add or invite contacts to a Telegram channel.

#### Parameters

- `filename`: Path to the vCard file containing contact information.
- `api_id`: Your Telegram API ID.
- `api_hash`: Your Telegram API hash.
- `phone_number`: Your phone number in international format (e.g., `'+98'`).
- `session_name`: Name for the Telegram session.
- `channel_username`: Username of the channel to which contacts will be added.

#### Running the Script

1. Ensure you have a vCard file containing the contact information.

2. Set the parameters in the script.

3. Run the script:

```bash
python TelegramContactAdderBot_main.py
```

### TelBotSendMessage.py

This script sends a message to specified recipients using the Telegram API.

#### Parameters

- `filename`: Path to the vCard file containing contact information.
- `api_id`: Your Telegram API ID.
- `api_hash`: Your Telegram API hash.
- `phone_number`: Your phone number in international format (e.g., `'+98'`).
- `session_name`: Name for the Telegram session.
- `recipient_number`: Phone number of the recipient to whom the message will be sent.

#### Running the Script

1. Ensure you have a vCard file containing the contact information.

2. Set the parameters in the script.

3. Run the script:

```bash
python TelBotSendMessage.py
```

## License

This project is licensed under the [MIT License](LICENSE).
