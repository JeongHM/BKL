import os
import json
from copy import deepcopy
from flask import request, Response

from services.auth import AuthService
from utills.response_code import RESPONSE_CODE


def response_formatted(func):
    def wrapper(*args, **kwargs):
        result, result_object, status = func(*args, **kwargs)
        if result_object:
            new_object = deepcopy(result)
            new_object['result'] = result_object
            result = new_object

        resp = json.dumps(obj=result, ensure_ascii=False, default=str).encode(encoding='utf-8')
        return Response(response=resp,
                        status=status,
                        content_type='application/json; charset=utf-8')
    return wrapper


def login_required(func):
    def wrapper(*args, **kwargs):
        resp = None
        email = request.headers.get('x-user-email')
        access_token = request.headers.get('x-access-token')

        if not access_token:
            resp = json.dumps(obj=RESPONSE_CODE['INVALID_HEADER'], ensure_ascii=False, default=str).encode('utf-8')

        auth_service = AuthService(access_token=access_token, email=email)
        validate, code = auth_service.validate_access_token()
        if not validate:
            resp = json.dumps(obj=RESPONSE_CODE['INVALID_TOKEN'], ensure_ascii=False, default=str).encode('utf-8')

        if resp:
            return Response(response=resp,
                            status=403,
                            content_type='application/json; charset=utf-8')
        return func(*args, **kwargs)
    return wrapper


def header_required(func):
    def wrapper(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        if not api_key or api_key != os.getenv('X_API_KEY'):
            resp = json.dumps(obj=RESPONSE_CODE['INVALID_HEADER'],
                              ensure_ascii=False,
                              default=str).encode('utf-8')
            return Response(response=resp,
                            status=403,
                            content_type='application/json; charset=utf-8')
        return func(*args, **kwargs)
    return wrapper
