from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "VPN backend работает"}

@app.route("/get-link")
def get_link():
    device = request.args.get("device")

    if device == "android":
        return {"link": "vless://ANDROID_LINK"}
    elif device == "ios":
        return {"link": "vless://IOS_LINK"}
    else:
        return {"error": "unknown device"}

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))