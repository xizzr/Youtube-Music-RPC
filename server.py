from flask import Flask, request
from pypresence import Presence
import time

app = Flask(__name__)
client_id = "YOUR_DISCORD_APP_CLIENT_ID"
rpc = Presence(client_id)
rpc.connect()

@app.route("/update_presence", methods=["POST"])
def update_presence():
    data = request.json
    title = data.get("title", "Unknown Song")
    artist = data.get("artist", "Unknown Artist")

    rpc.update(
        state=f"{artist}",
        details=title,
        large_image="ytmusic_logo",
        large_text="YouTube Music",
        start=time.time()
    )
    
    return {"status": "success"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
