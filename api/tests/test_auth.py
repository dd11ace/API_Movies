import pytest
from api.api_manager import APIManager


class TestAuth:
    """Класс для позитивных auth тестов"""

    def test_register_user(self, api_manager: APIManager, test_user: dict) -> None:
        """Тестирование регистрации"""
        response_data = api_manager.auth_api.register_user(test_user).json()

        assert response_data["id"] is not None, "В ответе нет id"
        assert response_data["email"] == test_user["email"], "email не совпадает"
        assert response_data["fullName"] == test_user["fullName"], "имя не совпадает"
        assert "roles" in response_data, "Нет roles в ответе"
        assert "USER" in response_data["roles"], "Нет USER в roles"

    def test_register_and_login_user(
        self, api_manager: APIManager, test_user: dict, login_info: dict
    ) -> None:
        """Тестирование регистрации и логина"""
        api_manager.auth_api.register_user(test_user)
        response_data = api_manager.auth_api.login_user(login_info).json()

        assert response_data["user"]["email"] == login_info["email"], (
            "email не совпадает"
        )
