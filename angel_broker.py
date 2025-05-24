from common.login.login_service import LoginService
from logzero import logger

    
if __name__ == "__main__":
    login_service = LoginService()
    try:
        session_details = login_service.get_session()
        logger.info("Session details retrieved successfully")
    except RuntimeError as e:
        logger.error(f"Error retrieving session details: {e}")