from common.login.login_interface import LoginInterface
from SmartApi import SmartConnect
import os
import pyotp
from dotenv import load_dotenv
load_dotenv()



class LoginService(LoginInterface):
    def __init__(self):
        self.obj=SmartConnect(api_key=os.getenv("API_KEY"))
    
    def get_session(self):
        """
        Method to get the session details after login.
        """
        try:
            TOPT_TOKEN = os.getenv("TOPT_TOKEN")
            userid = os.getenv("USER_ID")
            pin = os.getenv("PIN")
            session = self.obj.generateSession(userid,pin,pyotp.TOTP(TOPT_TOKEN).now())
            return {
                "auth_token": session['data']['jwtToken'],
                "refresh_token": session['data']['refreshToken'],
                "feed_token": self.obj.getfeedToken()
            }
        except Exception as e:
            raise RuntimeError(f"Failed to get session: {e}")
