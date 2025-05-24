from common.live_feed.live_feed_interface import LiveFeedInterface
from .smartWebSocketV2 import SmartWebSocketV2
import os
from dotenv import load_dotenv
load_dotenv()
from SmartApi import SmartConnect
from logzero import logger
import pyotp
from functools import partial


class LiveFeedService(LiveFeedInterface):
    def __init__(self):
        self.obj=SmartConnect(api_key=os.getenv("API_KEY"))
        try:
            self.API_KEY = os.getenv("API_KEY")
            TOPT_TOKEN = os.getenv("TOPT_TOKEN")
            self.userid = os.getenv("USER_ID")
            self.pin = os.getenv("PIN")
            self.session = self.obj.generateSession(self.userid,self.pin,pyotp.TOTP(TOPT_TOKEN).now())
    
        except Exception as e:
            raise RuntimeError(f"Failed to initialize session of Live Feed: {e}")
    
    def get_feed_of_instrument(self, correlation_id, mode, token_list):
        # correlation_id = "abc123"
        # action = 1
        # mode = 1

        # token_list = [
        #     {
        #         "exchangeType": 1,
        #         "tokens": ["26009"]
        #     }
        # ]
        # token_list1 = [
        #     {
        #         "action": 0,
        #         "exchangeType": 1,
        #         "tokens": ["26009"]
        #     }
        # ]
        """
        Method to get the session details after login.
        """
        self.sws = SmartWebSocketV2(self.session['data']['jwtToken'], self.API_KEY, self.userid, self.obj.getfeedToken())

        # Assign the callbacks.
        # Bind callbacks with required arguments using partial
        self.sws.on_open = partial(self.on_open, correlation_id, mode, token_list)
        self.sws.on_data = self.on_data
        self.sws.on_error = self.on_error
        self.sws.on_close = self.on_close

        self.sws.connect()

    def on_data(self, wsapp, message):
        logger.info("Ticks: {}".format(message))

    def on_open(self, correlation_id, mode, token_list, wsapp):
        logger.info("WebSocket opened")
        self.sws.subscribe(correlation_id, mode, token_list)

    def on_error(self, wsapp, error):
        logger.error(error)

    def on_close(self, wsapp):
        logger.info("Close")
        




