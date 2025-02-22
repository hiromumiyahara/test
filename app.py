import os
from flask import Flask

app = Flask(__name__)

# 環境変数からAPIキーを取得
API_KEY = os.getenv("API_KEY")

# ルートページでAPIキーを表示
@app.route("/")
def hello():
    return f"<h1>Hello, GitHub! 🚀</h1><p>API_KEY: {API_KEY}</p>"

# デバッグ用: ターミナルにAPIキーを表示
print(f"✅ API_KEY: {API_KEY}")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
