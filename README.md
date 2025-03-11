# Youtube-Music-RPC

A Discord Rich Presence integration for YouTube Music, displaying the currently playing song on your Discord profile using a Flask server and a custom browser extension/plugin.

## Features
- Displays the current song playing on YouTube Music in Discord Rich Presence
- Shows track title, artist, and album information
- Uses a local Flask server to send updates
- Lightweight and easy to set up

## Requirements
- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/)
- Google Chrome or a Chromium-based browser (for the custom plugin)

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/xizzr/Youtube-Music-RPC.git
cd Youtube-Music-RPC
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Install the Browser Extension
1. Open Chrome and go to `chrome://extensions/`
2. Enable **Developer mode** (toggle in the top right corner)
3. Click **Load unpacked**
4. Select the `extension` folder from this repository

### 4. Run server.py
```sh
python server.py
```

## Usage
1. Make sure YouTube Music is open in your browser.
2. Start the Flask application as described above.
3. Your Discord Rich Presence should now display the currently playing song.

## Troubleshooting
- Ensure Discord is running in the background.
- Check that the browser extension is installed and active.
- If the RPC isn't updating, restart the script and refresh YouTube Music.
- The flask server may not be able to set your rich presence using pypresence if you're on a modded discord client.

## Contributing
Issues and feature requests are welcome, but modifications and redistribution of modified versions are not permitted under the chosen license.

## License
This project is licensed under the [GNU General Public License v3.0](LICENSE).