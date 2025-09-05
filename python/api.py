from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/yt-dlp", methods=["POST"])
def yt_dlp():
    data = request.json
    link = data.get("link")
    return "Testing API with link: " + link + "\n"