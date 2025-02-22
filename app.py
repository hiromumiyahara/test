import os
from flask import Flask

app = Flask(__name__)

# 環境変数からAPIキーを取得
API_KEY = os.getenv("API_KEY")

# ルートパス（"/"）にアクセスしたときの挙動
@app.route("/")
def hello():
    return "<h1>Hello World!!</h1>"

# エラーハンドリング（404 Not Found用）
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 - ページが見つかりません</h1>", 404

# デバッグ用ログ出力
print(f"✅ API_KEY: {API_KEY}")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)