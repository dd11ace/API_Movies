import pytest
from api.api_manager import APIManager


class TestMoviesNegative:
    """Класс с негативными тестами"""

    def test_get_movie_not_found(
        self, api_manager: APIManager, nonexistent_movie_id: int
    ) -> None:
        """Тест получение несуществующего фильма"""
        response_data = api_manager.movies_api.get_movie_info(
            movie_id=nonexistent_movie_id, expected_status=404
        ).json()

        assert response_data["message"] is not None, (
            "Отсутствует сообщение об ошибке в логе ответа"
        )
        assert response_data["statusCode"] is not None, (
            "Отсутсвует код ошибки в логе ответа"
        )

    def test_methods_unauthorized(
        self,
        api_manager: APIManager,
        test_movie: dict,
        movie_id: int,
    ) -> None:
        """Тестирование запросов без авторизации"""
        methods = ["create_movie", "delete_movie", "patch_movie"]
        for method in methods:
            if method == "create_movie":
                response = api_manager.movies_api.create_movie(
                    test_movie, expected_status=401
                )

            elif method == "delete_movie":
                response = api_manager.movies_api.delete_movie(
                    movie_id, expected_status=401
                )

            elif method == "patch_movie":
                response = api_manager.movies_api.patch_movie(
                    movie_id, test_movie, expected_status=401
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
        test_movie: dict,
    ) -> None:
        """Тест создания фильма с уже существующим в базе именем"""
        test_movie["name"] = existing_movie_name

        response_data = authenticated_admin.movies_api.create_movie(
            movie_data=test_movie, expected_status=409
        ).json()

        assert response_data["message"] is not None, (
            "Отсутствует сообщение об ошибке в логе ответа"
        )
        assert response_data["statusCode"] is not None, (
            "Отсутсвует код ошибки в логе ответа"
        )

    @pytest.mark.parametrize(
        "field_name",
        [
            "name",
            "description",
            "price",
            "location",
            "published",
            "genreId",
        ],
    )
    def test_create_movie_without_field(
        self,
        authenticated_admin: APIManager,
        field_name: str,
        test_movie: dict[str : str | int | bool],
    ) -> None:
        """Тестирование создания фильма с путым полем"""
        test_movie[field_name] = None

        response_data = authenticated_admin.movies_api.create_movie(
            test_movie, expected_status=400
        ).json()

        assert response_data["message"] is not None, (
            "Отсутствует сообщение об ошибке в логе ответа"
        )
        assert response_data["statusCode"] is not None, (
            "Отсутсвует код ошибки в логе ответа"
        )

    @pytest.mark.parametrize(
        ("field_name", "invalid_value"),
        [
            ("name", 123),
            ("description", 123),
            ("price", "123"),
            ("location", 123),
            ("location", "string"),
            ("published", "True"),
            ("genreId", "1"),
        ],
    )
    def test_create_movie_with_invalid_data_types(
        self,
        test_movie: dict[str : str | int | bool],
        field_name: str,
        invalid_value: str | int,
        authenticated_admin: APIManager,
    ) -> None:
        """Тестирование создания фильма с неверными типами данных в полях"""
        test_movie[field_name] = invalid_value

        response_data = authenticated_admin.movies_api.create_movie(
            test_movie, expected_status=400
        ).json()

        assert response_data["message"] is not None, (
            "Отсутствует сообщение об ошибке в логе ответа"
        )
        assert response_data["statusCode"] is not None, (
            "Отсутсвует код ошибки в логе ответа"
        )
