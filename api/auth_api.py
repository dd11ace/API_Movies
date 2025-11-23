from custom_requester.custom_requester import CustomRequester
from requests import Session, Response

from constants import AUTH_URL, LOGIN_ENDPOINT, BASE_URL

from utils.credentials import ADMIN_USER_CREDENTIALS


class AuthAPI(CustomRequester):
    def __init__(self, session: Session) -> None:
        super().__init__(session=session, base_url=AUTH_URL)
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

    def authenticate(self, user_credentials, session):
        response = self.login_user(user_credentials, expected_status=201)

        response_data = response.json()

        if "accessToken" not in response_data:
            raise KeyError("token is missing")

        token = response_data["accessToken"]
        self._update_session_headers(
            session=session, **{"authorization": "Bearer " + token}
        )
