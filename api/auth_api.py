from custom_requester.custom_requester import CustomRequester
from requests import Session, Response

from constants import BASE_URL, LOGIN_ENDPOINT


class AuthAPI(CustomRequester):
    def __init__(self, session: Session) -> None:
        super().__init__(session=session, base_url=BASE_URL)
        self.session = session

    def login_user(
        self, login_data: dict[str:str], expected_status: int = 201
    ) -> Response:
        """
        Авторизация пользователя
        :param login_data: Данные для логина.
        :param expected_status: Ожидаемый статус-код.
        """
        return self.send_request(
            method="POST",
            endpoint=LOGIN_ENDPOINT,
            data=login_data,
            expected_status=expected_status,
        )
