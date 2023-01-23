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
    return jsonify(search_movie(title))#search_movie(title)


@app.route("/movie/year/to/<year>")
def search_page_years(year):
    """
    Вывод информации по названию фильма GET /movie/year/to/<year>
    """

    return jsonify(search_movie_years(year))


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
