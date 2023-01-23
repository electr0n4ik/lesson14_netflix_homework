# 1
def search_movie(title_movie):
    """
    Принимает название фильма
    Выполняет SQL-запрос
    Возвращает информацию о фильме в словаре
    (Необходимо добавить обработку названий фильмов с пробелом)
    """
    import sqlite3

    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = f"""SELECT title, country, release_year, description
                    FROM netflix
                    WHERE lower(title)
                    LIKE {title_movie}
                    AND `type` = 'Movie'
                    AND `release_year` != ''
                    AND `country` != ''
                    AND `description` != ''
                    """
    cur.execute(sqlite_query)
    search_result = cur.fetchall()

    for movie in search_result:
        if title_movie == movie[0]:
            result = {
                "title": movie[0],
                "country": movie[1],
                "release_year": movie[2],
                "genre": "listed_in",
                "description": movie[3]
                }
        else:
            result = f"Фильм {title_movie} не найден"

    con.close()

    return result

# 2
def search_movie_years(years):
    """
    Принимает количество годов(лет) для вывода
    Выполняет SQL-запрос
    Возвращает информацию о фильмах в JSON
    Один фильм на один год
    """
    import sqlite3

    list_movies = []

    con = sqlite3.connect("netflix.db")
    cur = con.cursor()

    sqlite_query = f"""SELECT title, release_year AS years_films
                        FROM netflix
                        WHERE `type` = 'Movie'
                        GROUP BY release_year
                        ORDER BY years_films DESC
                        LIMIT 100
                        """
    cur.execute(sqlite_query)
    search_result = cur.fetchall()

    for i in range(int(years)):
        list_movies.append({
            "title": search_result[i][0],
            "release_year": search_result[i][1],
        })

    return list_movies

# 3
def rank_movies(rank):
    """
    Принимает количество годов(лет) для вывода
    Выполняет SQL-запрос
    Возвращает информацию о фильмах в JSON
    Один фильм на один год
    """
    import sqlite3

    children = "G"
    family = ["G", "PG", "PG-13"]
    adult = ["R", "NC-17"]
    list_movies = []

    con = sqlite3.connect("netflix.db")
    cur = con.cursor()

    sqlite_query = f"""SELECT title, rating, description
                        FROM netflix
                        WHERE `type` = 'Movie'
                        """
    cur.execute(sqlite_query)
    search_result = cur.fetchall()

    for element in search_result:
        if rank == "children" and element[1] == children:

            list_movies.append({
                "title": element[0],
                "rating": element[1],
                "description": element[2]
            })

        elif rank == "family" and element[1] in family:
            list_movies.append({
                "title": element[0],
                "rating": element[1],
                "description": element[2]
            })

        elif rank == "adult" and element[1] in adult:
            list_movies.append({
                "title": element[0],
                "rating": element[1],
                "description": element[2]
            })

    return list_movies

# 4
def fresh_movies(genre):
    """
    TODO В базе данных нет жанров
    Принимает жанр для вывода
    Выполняет SQL-запрос
    Возвращает информацию о 10 свежих фильмах в JSON определенного жанра
    """
    import sqlite3

    list_movies = []

    sqlite_query = f"""SELECT title, description
    FROM netflix
    WHERE `type` = 'Movie'
    ORDER BY release_year DESC 
    LIMIT 10
    """
    cur.execute(sqlite_query)
    search_result = cur.fetchall()

    for element in search_result:
        if genre == element[1]:
            list_movies.append({
                "title": element[0],
                "description": element[1]
            })

    return list_movies

# 5
def twince_