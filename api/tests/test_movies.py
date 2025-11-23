import pytest
from api.api_manager import APIManager
from custom_requester.custom_requester import CustomRequester


class TestMovies:
    def test_get_movie(self, api_manager: APIManager, movie_id: int) -> None:
        response = api_manager.movies_api.get_movie_info(movie_id)

        assert response.status_code == 200, "Ошибка получения данных фильма"

        response_data = response.json()

        assert response_data["id"] == movie_id, "ID фильмов не совпадают"
