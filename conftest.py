import pytest
import requests

from utils.data_generator import DataGenerator

from api.api_manager import APIManager
from utils.credentials import ADMIN_USER_CREDENTIALS


@pytest.fixture(name="test_movie")
def test_movie_data() -> dict[str : str | int | bool]:
    """Fixture с данными для создания фильма"""
    movie_data = DataGenerator.generate_random_movie_data()

    return movie_data


@pytest.fixture(name="test_user")
def test_user_info() -> dict:
    email = DataGenerator.generate_random_email()
    full_name = DataGenerator.generate_random_full_name()
    password = DataGenerator.generate_random_password()

    user_data = {
        "email": email,
        "fullName": full_name,
        "password": password,
        "passwordRepeat": password,
        "roles": ["USER"],
    }

    return user_data


@pytest.fixture()
def login_info(test_user: dict) -> dict:
    user_data = {
        "email": test_user["email"],
        "password": test_user["password"],
    }

    return user_data


@pytest.fixture()
def movie_id() -> int:
    """Возвращает случайный id"""
    return DataGenerator.generate_random_id()


@pytest.fixture(scope="session")
def session() -> requests.Session:
    """Fixture для создания HTTP-сессии"""
    http_session = requests.Session()
    yield http_session
    http_session.close()


@pytest.fixture(scope="session")
def api_manager(session: requests.Session) -> APIManager:
    """Возвращает экземпляр APIManager"""
    return APIManager(session)


@pytest.fixture()
def authenticated_admin(
    api_manager: APIManager, session: requests.Session
) -> APIManager:
    """Возвращает экземпляр APIManager с аутентификацией админа"""
    api_manager.auth_api.authenticate(ADMIN_USER_CREDENTIALS, session)

    yield api_manager
    api_manager.session.headers.clear()


@pytest.fixture()
def nonexistent_movie_id() -> int:
    """Возвращает несуществующий id для негативных тестов"""
    return DataGenerator.generate_random_non_existing_id()


@pytest.fixture()
def existing_movie_name() -> str:
    """Возвращает существующие название фильма"""
    return DataGenerator.generate_random_existing_movie_name()
