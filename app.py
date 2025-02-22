import os
from flask import Flask

app = Flask(__name__)

# 環境変数からAPIキーを取得
API_KEY = os.getenv("API_KEY")

# ルートページ
@app.route("/")
def hello():
    return "<h1>Hello, GitHub! 🚀</h1>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
