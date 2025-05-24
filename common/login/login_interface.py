from abc import ABC, abstractmethod


class LoginInterface(ABC):
    @abstractmethod
    def get_session(self):
        """
        Method to get the session details after login.
        returns {
            "auth_token": str,
            "feed_token": str,
            "refresh_token" : str
            }
        """
        pass