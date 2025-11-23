from custom_requester.custom_requester import CustomRequester
from requests import Session, Response

from constants import BASE_URL, MOVIES_ENDPOINT


class MoviesAPI(CustomRequester):
    """
    Класс для работы с Movies API
    """

    def __init__(self, session: Session) -> None:
        super().__init__(base_url=BASE_URL, session=session)
        self.session = session

    def create_movie(
        self, movie_data: dict[str : str | int | bool], expected_status: int = 201
    ) -> Response:
        """
        Создание фильма
        :param movie_data: данные для фильма в формате JSON
        :param expected_status: Ожидаемый статус-код.
        """
        return self.send_request(
            method="POST",
            data=movie_data,
            endpoint=MOVIES_ENDPOINT,
            expected_status=expected_status,
        )

    def get_movie_info(self, movie_id: int, expected_status: int = 200) -> Response:
        """
        Получение информации о фильме.
        :param movie_id: ID фильма.
        :param expected_status: Ожидаемый статус-код.
        """
        return self.send_request(
            method="GET",
            endpoint=f"{MOVIES_ENDPOINT}/{movie_id}",
            expected_status=expected_status,
        )

    def delete_movie(self, movie_id: int, expected_status: int = 200) -> Response:
        """
        Удаление фильма.
        :param movie_id: ID фильма.
        :param expected_status: Ожидаемый статус-код.
        """
        return self.send_request(
            method="DELETE",
            endpoint=f"{MOVIES_ENDPOINT}/{movie_id}",
            expected_status=expected_status,
        )
