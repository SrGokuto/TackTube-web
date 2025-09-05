from flask import Flask, request, jsonify
from yt_dlp import YoutubeDL

app = Flask(__name__)

@app.route("/api/yt-dlp", methods=["POST"])
def yt_dlp():
    data = request.json
    link = data.get("link")

    ydl_opts = {
        'format': 'best',
        "playlist_items": "1",
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(link, download=False)

    return jsonify(result), 200