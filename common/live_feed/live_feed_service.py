from common.live_feed.live_feed_factory import LiveFeedFactory

class LiveFeedService:

    def __init__(self):
        self.live_feed_client = LiveFeedFactory.get_instance()

    def get_feed_of_instrument(self, correlation_id=str, mode=int, token_list=dict):
        try:
            """
                Method to get the live feed of an instrument.
            """
            return self.live_feed_client.get_feed_of_instrument(correlation_id, mode, token_list)
        except Exception as e:
            raise RuntimeError(f"Failed to get session: {e}")
    
