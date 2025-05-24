from common.login.login_service import LoginService
from common.live_feed.live_feed_service import LiveFeedService
from logzero import logger

class AngelBroker:
    """
    AngelBroker class to handle login and live feed services.
    This class initializes the login and live feed services and provides methods to interact with them.
    """

    def __init__(self):
        # self.login_service = LoginService()
        self.live_feed_service = LiveFeedService()

    # def get_session(self):
    #     return self.login_service.get_session()

    def get_live_feed(self, correlation_id, mode, token_list):
        return self.live_feed_service.get_feed_of_instrument(correlation_id, mode, token_list)

def main():
    broker = AngelBroker()
    try:
        # Example usage of get_live_feed
        correlation_id = "abc123"
        mode = 1
        token_list = [
            {
                "exchangeType": 1,
                "tokens": ["26009"]
            }
        ]
        feed = broker.get_live_feed(correlation_id, mode, token_list)
        logger.info(f"Live Feed: {feed}")
    except Exception as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    main()