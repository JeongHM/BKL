import os
import jwt

from datetime import datetime, timedelta
from flask import current_app

from models import mongo


class AuthService(object):
    def __init__(self, access_token: str, email: str):
        self._access_token = access_token
        self._email = email

    @staticmethod
    def generate_access_token(email: str) -> tuple:
        """
        generate JWT Token
        :return:
        """
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(hours=2),
                'iat': datetime.utcnow(),
                'sub': email
            }
            access_token = jwt.encode(payload=payload,
                                      key=os.getenv('SECRET_KEY'),
                                      algorithm='HS256').decode(encoding='utf-8')

            users = mongo.db.users.find_one({'email': email})
            users.update({'access_token': access_token})
            mongo.db.users.update({'email': email}, users)

        except Exception as e:
            current_app.logger.error(e)
            return False, None

        else:
            return access_token, True

    def validate_access_token(self) -> tuple:
        try:
            payload = jwt.decode(jwt=self._access_token,
                                 key=os.getenv('SECRET_KEY'))
            user_email = payload.get('sub')
            if not user_email or user_email != self._email:
                raise ValueError('Invalid Token')

            exp = payload.get('exp')
            if exp < int(datetime.utcnow().timestamp()):
                raise ValueError('Expired Token')

        except Exception as e:
            current_app.logger.error(e)
            return False, None

        else:
            return True, None

    def refresh_access_token(self) -> tuple:
        try:
            refresh_token = AuthService.generate_access_token(email=self._email)
            if not refresh_token:
                raise ValueError('Refresh Token Error')

        except Exception as e:
            current_app.logger.error(e)
            return False, None

        else:
            return refresh_token, True

