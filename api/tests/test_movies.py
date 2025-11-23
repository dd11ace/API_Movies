import pytest
from api.api_manager import APIManager


class TestMovies:
    def test_get_movie(self, api_manager: APIManager, movie_id: int) -> None:
        """Тестирование получение фильма по ID"""
        response = api_manager.movies_api.get_movie_info(movie_id)

        assert response.status_code == 200, "Ошибка получения данных фильма"

        response_data = response.json()

        assert response_data["id"] == movie_id, "ID фильмов не совпадают"

    def test_create_movie(
        self,
        test_movie: dict[str : str | int | bool,],
        authenticated_admin: APIManager,
    ) -> None:
        """Тестирование создания фильма"""

        response = authenticated_admin.movies_api.create_movie(test_movie)

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

    def test_delete_movie(
        self,
        authenticated_admin: APIManager,
        movie_id: int,
    ) -> None:
        """Тест на удаление фильма по ID"""
        response = authenticated_admin.movies_api.delete_movie(movie_id)

        assert response.status_code == 200, "Ошибка при удалении"

        response_data = response.json()

        assert response_data["id"] == movie_id, "ID фильмов не совпадают"

    def test_patch_movie(
        self,
        authenticated_admin: APIManager,
        movie_id: int,
        test_movie: dict[str : str | int | bool],
    ) -> None:
        """Тест редактирования фильма"""
        response = authenticated_admin.movies_api.patch_movie(
            movie_id=movie_id, movie_data=test_movie
        )

        assert response.status_code == 200, "Ошибка при редактировании фильма"

        response_data = response.json()

        assert response_data["id"] == movie_id

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
