from flask import Flask, request, render_template, jsonify, redirect
from utils import *

app = Flask(__name__)
# Чтобы заработала кириллица
app.config['JSON_AS_ASCII'] = False

@app.route("/movie/<title>")
def search_page(title):
    """
    Вывод информации по названию фильма GET /movie/<title>
    """
    return search_movie(title)#jsonify(search_movie(title))



@app.errorhandler(404)
def error_404(error):
    """
    Представление для ошибки "Страница не найдена"
    """
    return "<h1>Страница не найдена</h1>", 404


@app.errorhandler(500)
def internal_server_error(error):
    """
    Представление для ошибки "Внутренняя ошибка сервера"
    """
    return "<h1>Сервер не отвечает</h1>", 500


if __name__ == "__main__":
    app.run(debug=True)
