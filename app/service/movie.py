"""Сервис фильмов"""
from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, id):
        return self.dao.get_one(id)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create()

    def update(self, data):
        id = data.get("id")
        movie = self.get_one(id)

        movie.id = data.get("id")
        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        self.dao.update(movie)

    def update_path(self, data):
        id = data.get("id")
        movie = self.get_one(id)
        if "id" in data:
            movie.id = data.get("id")
        if "title" in data:
            movie.title = data.get("title")
        if "description" in data:
            movie.description = data.get("description")
        if "trailer" in data:
            movie.trailer = data.get("trailer")
        if "year" in data:
            movie.year = data.get("year")
        if "rating" in data:
            movie.rating = data.get("rating")
        if "genre_id" in data:
            movie.genre_id = data.get("genre_id")
        if "director_id" in data:
            movie.director_id = data.get("director_id")

        self.dao.update(movie)

    def delete(self, id):
        self.dao.delete(id)
