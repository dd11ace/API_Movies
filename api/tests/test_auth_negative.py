import pytest

from faker import Faker
from api.api_manager import APIManager

faker = Faker()


class TestAuthNegative:
    """Класс для тестирование негативных кейсов для auth"""

    @pytest.mark.parametrize("field", ["email", "password"])
    def test_login_with_invalid_field_data(
        self, api_manager: APIManager, field: str, test_user: dict, login_info: dict
    ) -> None:
        """Тестирование логина с невалидным паролем"""
        api_manager.auth_api.register_user(test_user)

        if field == "email":
            login_info[field] = faker.email()
        elif field == "password":
            login_info[field] = faker.password()

        response_data = api_manager.auth_api.login_user(
            login_info, expected_status=401
        ).json()

        assert response_data["message"] == "Неверный логин или пароль"
        assert response_data["error"] == "Unauthorized"
        assert response_data["statusCode"] == 401

    @pytest.mark.parametrize(
        "field", ["email", "fullName", "password", "passwordRepeat"]
    )
    def test_register_with_missing_required_field(
        self, field: str, api_manager: APIManager, test_user: dict
    ) -> None:
        test_user[field] = None

        response_data = api_manager.auth_api.register_user(
            test_user, expected_status=400
        ).json()

        assert response_data["message"] is not None
        assert response_data["statusCode"] == 400
