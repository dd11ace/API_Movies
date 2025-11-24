import random
import requests
from faker import Faker

from constants import BASE_URL, MOVIES_ENDPOINT

faker = Faker()


class DataGenerator:
    """Генерация тестовых данных"""

    @staticmethod
    def generate_random_movie_data() -> dict[str : str | int | bool]:
        """
        Генерация данных для создания фильма

        returns:
            dict: Данные фильма
        """

        movie_data = {
            "name": faker.sentence(nb_words=2),
            "imageUrl": faker.image_url(),
            "price": random.randint(100, 1000),
            "description": faker.text(max_nb_chars=200),
            "location": random.choice(["SPB", "MSK"]),
            "published": random.choice([True, False]),
            "genreId": random.randint(1, 10),
        }

        return movie_data

    @staticmethod
    def generate_random_existing_movie_name(id_range: tuple = (1, 4000)) -> str:
        """Генерация случайного имени из существуещего фильма"""
        while True:
            random_id = random.randint(id_range[0], id_range[1])

            try:
                response = requests.get(
                    f"{BASE_URL}{MOVIES_ENDPOINT}/{random_id}", timeout=3
                )

                if response.status_code == 200:
                    return response.json()["name"]

            except requests.exceptions.RequestException:
                # Продолжение при ошибке
                pass

    @staticmethod
    def generate_random_id(id_range: tuple = (1, 4000)) -> int:
        """Генерация случайного существуего id"""
        while True:
            random_id = random.randint(id_range[0], id_range[1])

            try:
                response = requests.get(
                    f"{BASE_URL}{MOVIES_ENDPOINT}/{random_id}", timeout=3
                )

                if response.status_code == 200:
                    return random_id
                # Для ошибки 404 цикл продолжается

            except requests.exceptions.RequestException:
                # Продолжение при ошибке
                pass

    @staticmethod
    def generate_random_non_existing_id(id_range: tuple = (1, 10000)):
        """Генерация случайного несуществуего id для негативных тестов"""
        while True:
            random_id = random.randint(id_range[0], id_range[1])

            try:
                response = requests.get(
                    f"{BASE_URL}{MOVIES_ENDPOINT}/{random_id}", timeout=3
                )

                if response.status_code == 404:
                    return random_id
                # Для 200 цикл продолжается

            except requests.exceptions.RequestException:
                # Продолжение при ошибке
                pass
