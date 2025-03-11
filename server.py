from flask import Flask, request, jsonify
from flask_cors import CORS
from pypresence import Presence
import time
import win32gui, win32con

the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

app = Flask(__name__)
CORS(app, origins=["chrome-extension://*"]) 

CLIENT_ID = "1346156506818543727"

try:
    rpc = Presence(CLIENT_ID)
    rpc.connect()
    print("[INFO] Connected to Discord RPC successfully.")
except Exception as e:
    print(f"[ERROR] Failed to connect to Discord RPC: {e}")
    rpc = None

@app.route("/update_presence", methods=["POST"])
def update_presence():
    if rpc is None:
        return jsonify({"status": "error", "message": "Discord RPC not connected"}), 500

    data = request.json
    title = data.get("title")
    artist = data.get("artist")
    times = data.get("times")

    first_time_str = str(times).split(" / ")[0].split(" - ")[0]
    minutes, seconds = map(int, first_time_str.split(":"))
    total_seconds = minutes * 60 + seconds
    current_time = time.time()
    ttime = current_time - total_seconds
    try:
        rpc.update(
            state=f"{artist}",
            details=title,
            large_image="ytmusic_logo",
            large_text="YouTube Music",
            start=ttime
        )
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
