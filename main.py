from flask import Flask, request

app = Flask(__name__)

# Проверка что сервер работает
@app.route("/")
def home():
    return {"status": "VPN backend работает"}

# Получение ссылки
@app.route("/get-link")
def get_link():
    device = request.args.get("device")

    if device == "android":
        return {"link": "vless://ANDROID_LINK"}
    
    elif device == "ios":
        return {"link": "vless://IOS_LINK"}
    
    else:
        return {"error": "unknown device"}

# Запуск сервера (ОБЯЗАТЕЛЬНО В КОНЦЕ)
app.run(host="0.0.0.0", port=8080)