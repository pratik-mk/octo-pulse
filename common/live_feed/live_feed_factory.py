import importlib
# from common.configs.conf_parser import ConfigParser
from common.configs.conf_parser import ConfParser
from common.live_feed.live_feed_interface import LiveFeedInterface

class LiveFeedFactory:
    @staticmethod
    def get_instance() -> LiveFeedInterface: 
        live_feed_class_name = None
        live_feed_module_path = None
        try: 
            live_feed_class_name = ConfParser.get_config_value("LIVE_FEED_CLASS")
            live_feed_module_path = ConfParser.get_config_value("LIVE_FEED_MODULE")
            live_feed_module = importlib.import_module(live_feed_module_path)
            live_feed_class = getattr(live_feed_module, live_feed_class_name)
            return live_feed_class()
        except Exception as e:
            raise ImportError(f"Failed to load login class '{live_feed_class_name}' from module '{live_feed_module_path}': {e}")