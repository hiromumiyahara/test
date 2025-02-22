from flask import Flask

app = Flask(__name__)

# ルートパス（"/"）にアクセスしたときの挙動
@app.route("/")
def hello():
    return "<h1>Hello, GitHub! 🚀</h1>"

# エラーハンドリング（404 Not Found用）
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 - ページが見つかりません</h1>", 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)