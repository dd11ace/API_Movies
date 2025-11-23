import pytest
from api.api_manager import APIManager

from utils.credentials import ADMIN_USER_CREDENTIALS


class TestMovies:
    def test_get_movie(self, api_manager: APIManager, movie_id: int) -> None:
        response = api_manager.movies_api.get_movie_info(movie_id)

        assert response.status_code == 200, "Ошибка получения данных фильма"

        response_data = response.json()

        assert response_data["id"] == movie_id, "ID фильмов не совпадают"

    def test_create_movie(
        self,
        api_manager: APIManager,
        test_movie: dict[str : str | int | bool,],
        session,
    ) -> None:
        api_manager.auth_api.authenticate(ADMIN_USER_CREDENTIALS, session)

        response = api_manager.movies_api.create_movie(test_movie)

        assert response.status_code == 201, "Ошибка при создании фильма"

        response_data = response.json()

        assert response_data["name"] == test_movie["name"], (
            "Названия фильмов не совпадают"
        )

        assert response_data["price"] == test_movie["price"], "Цены не совпадают"

        assert response_data["description"] == test_movie["description"], (
            "Описание не совпадает"
        )

        assert response_data["location"] == test_movie["location"], (
            "Локация не совпадает"
        )

        assert response_data["published"] == test_movie["published"], (
            "Статус published не совпадает"
        )

        assert response_data["genreId"] == test_movie["genreId"], (
            "ID жанра не совпадает"
        )
