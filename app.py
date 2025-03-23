import gtts.lang as lang

from gtts import gTTS
from flask import Flask, request, send_file
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)

app.config["version"] = "v1"
app.config["api"] = f"/api/" + app.config.get("version") + "/"

limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri="memory://",
)


api = app.config.get("api")


@app.route(api + "gtt", methods=["POST"])
@limiter.limit("20 per minute")
def gtt():
    data = request.get_json()

    text = data["text"]
    lang = data["lang"]

    gtt_client = gTTS(text, lang=lang)
    gtt_client.save("output.mp3")

    return send_file("output.mp3")

@app.route(api + "langs")
@limiter.limit("2 per minute")
def langs():
    return lang.tts_langs()

if __name__ == "__main__":
    app.run()
