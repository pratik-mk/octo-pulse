import importlib
# from common.configs.conf_parser import ConfigParser
from common.configs.conf_parser import ConfParser
from common.login.login_interface import LoginInterface

class LoginFactory:
    @staticmethod
    def get_instance() -> LoginInterface: 
        login_class_name = None
        login_module_path = None
        try: 
            login_class_name = ConfParser.get_config_value("LOGIN_CLASS")
            login_module_path = ConfParser.get_config_value("LOGIN_MODULE")
            login_module = importlib.import_module(login_module_path)
            login_class = getattr(login_module, login_class_name)
            return login_class()
        except Exception as e:
            raise ImportError(f"Failed to load login class '{login_class_name}' from module '{login_module_path}': {e}")