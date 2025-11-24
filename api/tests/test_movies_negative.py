import pytest
from api.api_manager import APIManager


class TestMoviesNegative:
    def test_get_movie_not_found(
        self, api_manager: APIManager, nonexistent_movie_id: int
    ) -> None:
        """Тест получение несуществующего фильма"""
        response = api_manager.movies_api.get_movie_info(
            movie_id=nonexistent_movie_id, expected_status=404
        )

        assert response.status_code == 404

        response_data = response.json()

        assert response_data["message"] is not None, (
            "Отсутствует сообщение об ошибке в логе ответа"
        )

        assert response_data["statusCode"] is not None, (
            "Отсутсвует код ошибки в логе ответа"
        )

    def test_post_without_auth(
        self, api_manager: APIManager, test_movie: dict[str : str | int | bool]
    ) -> None:
        """Тест создания фильма без аутентификации"""
        response = api_manager.movies_api.create_movie(test_movie, expected_status=401)

        assert response.status_code == 401, (
            f"Ожидалась ошибка 401 Unauthorized, но был получен {response.status_code}"
        )

        response_data = response.json()

        assert response_data["message"] is not None, (
            "Отсутствует сообщение об ошибке в логе ответа"
        )

        assert response_data["statusCode"] is not None, (
            "Отсутсвует код ошибки в логе ответа"
        )

    def test_delete_without_auth(
        self,
        api_manager: APIManager,
        movie_id,
    ) -> None:
        """Тест удаления без аутентификации"""
        response = api_manager.movies_api.delete_movie(movie_id, expected_status=401)

        assert response.status_code == 401, (
            f"Ожидалась ошибка 401 Unauthorized, но был получен {response.status_code}"
        )

        response_data = response.json()

        assert response_data["message"] is not None, (
            "Отсутствует сообщение об ошибке в логе ответа"
        )

        assert response_data["statusCode"] is not None, (
            "Отсутсвует код ошибки в логе ответа"
        )

    def test_patch_without_auth(
        self,
        api_manager: APIManager,
        movie_id: int,
        test_movie: dict[str : str | int | bool],
    ) -> None:
        """Тест редактирование без аутентификации"""
        response = api_manager.movies_api.patch_movie(
            movie_id, test_movie, expected_status=401
        )

        assert response.status_code == 401, (
            f"Ожидалась ошибка 401 Unauthorized, но был получен {response.status_code}"
        )

        response_data = response.json()

        assert response_data["message"] is not None, (
            "Отсутствует сообщение об ошибке в логе ответа"
        )

        assert response_data["statusCode"] is not None, (
            "Отсутсвует код ошибки в логе ответа"
        )

    def test_create_movie_with_existing_name(
        self,
        existing_movie_name: str,
        authenticated_admin: APIManager,
        test_movie: dict[str : str | int | bool],
    ) -> None:
        """Тест создания фильма с уже существующим в базе именем"""
        test_movie["name"] = existing_movie_name

        response = authenticated_admin.movies_api.create_movie(
            movie_data=test_movie, expected_status=409
        )

        assert response.status_code == 409, (
            f"Ожидалась ошибка со статус кодом 409, но был получен {response.status_code}"
        )

        response_data = response.json()

        assert response_data["message"] is not None, (
            "Отсутствует сообщение об ошибке в логе ответа"
        )

        assert response_data["statusCode"] is not None, (
            "Отсутсвует код ошибки в логе ответа"
        )

    def test_create_movie_without_name(
        self, authenticated_admin: APIManager, test_movie: dict[str : str | int | bool]
    ) -> None:
        """Тестирование создания фильма без названия"""
        test_movie["name"] = None

        response = authenticated_admin.movies_api.create_movie(
            test_movie, expected_status=400
        )

        assert response.status_code == 400, (
            f"Ожидалась ошибка 400 неверные параметры, но был получен {response.status_code}"
        )

        response_data = response.json()

        assert response_data["message"] is not None, (
            "Отсутствует сообщение об ошибке в логе ответа"
        )

        assert response_data["statusCode"] is not None, (
            "Отсутсвует код ошибки в логе ответа"
        )
