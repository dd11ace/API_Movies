import random
import pytest
import requests


from utils.data_generator import DataGenerator
from custom_requester.custom_requester import CustomRequester

from api.api_manager import APIManager

from constants import BASE_URL
from utils.credentials import ADMIN_USER_CREDENTIALS


@pytest.fixture(name="test_movie")
def test_movie_data() -> dict[str : str | int | bool]:
    """Fixture с данными для создания фильма"""
    movie_data = DataGenerator.generate_random_movie_data()

    return movie_data


@pytest.fixture()
def movie_id() -> int:
    """Возвращает случайный id"""
    return DataGenerator.generate_random_id()


@pytest.fixture(scope="session")
def requester() -> CustomRequester:
    """Fixture для создания экземпляра CustomRequester"""
    session = requests.Session()

    return CustomRequester(session=session, base_url=BASE_URL)


@pytest.fixture(scope="session")
def session() -> requests.Session:
    """Fixture для создания HTTP-сессии"""
    http_session = requests.Session()
    yield http_session
    http_session.close()


@pytest.fixture(scope="session")
def api_manager(session: requests.Session) -> requests.Session:
    return APIManager(session)


@pytest.fixture(scope="session")
def authenticated_admin(
    api_manager: APIManager, session: requests.Session
) -> APIManager:
    api_manager.auth_api.authenticate(ADMIN_USER_CREDENTIALS, session)

    yield api_manager


@pytest.fixture()
def nonexistent_movie_id() -> int:
    """Несуществующий id для негативных тестов"""
    return DataGenerator.generate_random_non_existing_id()


@pytest.fixture()
def existing_movie_name() -> str:
    """Существующие название фильма"""
    return DataGenerator.generate_random_existing_movie_name()
