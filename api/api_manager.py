from requests import Session

from .movies_api import MoviesAPI
from .auth_api import AuthAPI


class APIManager:
    """
    Класс для управления API-классами с единой HTTP-сессией.
    """

    def __init__(self, session: Session) -> None:
        """
        Инициализация APIManager.
        :param session: HTTP-сессия, используемая всеми API-классами
        """
        self.session = session

        self.movies_api = MoviesAPI(session)
        self.auth_api = AuthAPI(session)
