from common.login.login_factory import LoginFactory

class LoginService:

    def __init__(self):
        self.login_client = LoginFactory.get_instance()

    def get_session(self):
        try:
            """
            Method to get the session details after login.
             returns {
                "auth_token": str,
                "feed_token": str,
                "refresh_token" : str
            }
            """
            return self.login_client.get_session()
        except Exception as e:
            raise RuntimeError(f"Failed to get session: {e}")
    
