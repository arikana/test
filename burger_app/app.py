from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__)

# 메뉴 데이터를 로드합니다
def load_menu():
    with open('menu.json', 'r', encoding='utf-8') as file:
        return json.load(file)

menu = load_menu()

# 사용자가 입력한 금액 내에서 메뉴를 추천합니다
def recommend_menu(budget):
    options = [item for item in menu if item['price'] <= budget]
    if not options:
        return "추천할 메뉴가 없습니다."
    return random.choice(options)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        budget = int(request.form["budget"])
        recommendation = recommend_menu(budget)
        return render_template("index.html", recommendation=recommendation)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
