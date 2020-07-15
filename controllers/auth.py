from flask import Blueprint, request

from services.auth import AuthService
from utills.response_code import RESPONSE_CODE
from utills.decorators import login_required, header_required, response_formatted

auth_blueprint = Blueprint(name='auth', import_name=__name__)


@auth_blueprint.route(rule='/validate', methods=['POST'], endpoint='validate_token')
@header_required
@login_required
@response_formatted
def validate_token():
    email = request.headers.get('x-user-email')
    access_token = request.headers.get('x-access-token')
    auth_service = AuthService(access_token=access_token, email=email)

    item, code = auth_service.validate_access_token()
    if not item:
        return RESPONSE_CODE[code], None, 400

    return RESPONSE_CODE[code], item, 200


@auth_blueprint.route(rule='/refresh', methods=['POST'], endpoint='refresh_token')
@header_required
@login_required
@response_formatted
def refresh_token():
    email = request.headers.get('x-user-email')
    access_token = request.headers.get('access_token')
    auth_service = AuthService(access_token=access_token, email=email)

    item, code = auth_service.refresh_access_token()
    if not item:
        return RESPONSE_CODE[code], None, 400

    return RESPONSE_CODE[code], item, 200
