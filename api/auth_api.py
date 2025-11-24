from custom_requester.custom_requester import CustomRequester
import requests

from constants import AUTH_URL, LOGIN_ENDPOINT


class AuthAPI(CustomRequester):
    def __init__(self, session: requests.Session) -> None:
        super().__init__(session=session, base_url=AUTH_URL)
        self.session = session

    def login_user(
        self, login_data: dict[str:str], expected_status: int = 201
    ) -> requests.Response:
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

    def authenticate(
        self, user_credentials: dict[str:str], session: requests.Session
    ) -> None:
        """
        Аутентификация пользователя
        :param user_credentials: Данные для логина.
        :param session: requests.Session.
        """
        response = self.login_user(user_credentials)

        response_data = response.json()

        if "accessToken" not in response_data:
            raise KeyError("token is missing")

        token = response_data["accessToken"]
        self._update_session_headers(
            session=session, **{"authorization": "Bearer " + token}
        )
