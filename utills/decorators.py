import os
from flask import request, Response

from services.auth import AuthService


def login_required(func):
    def wrapper(*args, **kwargs):
        email = request.headers.get('x-user-email')
        access_token = request.headers.get('x-access-token')
        if not access_token:
            return Response()

        auth_service = AuthService(access_token=access_token, email=email)
        validate, code = auth_service.validate_access_token()
        if not validate:
            return Response()

        return func(*args, **kwargs)
    return wrapper


def header_required(func):
    def wrapper(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        if not api_key or api_key != os.getenv('X_API_KEY'):
            return Response()

        return func(*args, **kwargs)
    return wrapper
