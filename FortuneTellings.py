import random
from flask import Flask, render_template  # 💡 render_template を追加

App_FortuneTellings = Flask(__name__)


# 🏠 1. トップページ（index.htmlを表示する）
@App_FortuneTellings.route("/")
def index():
    # templates/index.html を読み込んで画面に表示します
    return render_template("index.html")


# 🔮 2. おみくじページ（URLは /fortune に変更）
@App_FortuneTellings.route("/fortune")
def fortune_telling_page():
    results = [
        "大吉 🌟 最高の一日になります！",
        "吉 👍 良いことあるかも。",
        "中吉 😊 穏やかに過ごせそう。",
        "凶 ☕ 暖かいコーヒーでも飲んでリラックス。",
    ]
    fortune = random.choice(results)

    html = f"""
    <!DOCTYPE html>
    <html>
    <head><title>おみくじ</title></head>
    <body style="text-align: center; margin-top: 100px; font-family: sans-serif;">
        <h1>今日のおみくじ</h1>
        <h2 style="color: #ff4757; background: #f1f2f6; display: inline-block; padding: 10px 20px; border-radius: 10px;">
            {fortune}
        </h2>
        <p><button onclick="location.reload()">もう一度引く</button></p>
        <p><a href="/">トップページに戻る</a></p>
    </body>
    </html>
    """
    return html


if __name__ == "__main__":
    App_FortuneTellings.run(host="0.0.0.0", port=8080)
