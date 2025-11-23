import random
from faker import Faker

faker = Faker()


class DataGenerator:
    """Генерация тестовых данных"""

    @staticmethod
    def generate_random_movie_data() -> dict[str, str | int | bool]:
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
