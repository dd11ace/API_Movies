import random
import requests
import string
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
            "name": faker.sentence(nb_words=3),
            "imageUrl": faker.image_url(),
            "price": random.randint(100, 1000),
            "description": faker.text(max_nb_chars=200),
            "location": random.choice(["SPB", "MSK"]),
            "published": random.choice([True, False]),
            "genreId": random.randint(1, 10),
        }

        return movie_data

    @staticmethod
    def generate_random_email() -> str:
        """Генерация случайного email"""
        random_string = "".join(
            random.choices(string.ascii_letters + string.digits, k=8)
        )

        return f"kek{random_string}@gmail.com"

    @staticmethod
    def generate_random_password() -> str:
        """
        Генерация пароля, соответствующего требованиям:
        - Минимум 1 буква.
        - Минимум 1 цифра.
        - Допустимые символы.
        - Длина от 8 до 20 символов
        """
        # Гарантия хотя бы одной буквы и цифры
        letters = random.choice(string.ascii_letters)
        digits = random.choice(string.digits)

        # Дополнение пароля случайными символами из допустимых
        special_chars = "?@#$%^&*|:"

        all_chars = string.ascii_letters + string.digits + special_chars

        remaining_length = random.randint(6, 18)
        remaining_chars = "".join(random.choices(all_chars, k=remaining_length))

        # Перемешиваем пароль для рандомизации
        password = list(letters + digits + remaining_chars)
        random.shuffle(password)

        return "".join(password)

    @staticmethod
    def generate_random_full_name() -> str:
        """Генерация случайного имени"""
        return f"{faker.first_name()} {faker.last_name()}"
