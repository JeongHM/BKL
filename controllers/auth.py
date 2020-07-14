from flask import Blueprint, request, jsonify

from services.auth import AuthService

auth_blueprint = Blueprint(name='auth', import_name=__name__)


@auth_blueprint.route(rule='/validate', methods=['POST'], endpoint='validate_token')
def validate_token():
    email = request.headers.get('x-user-email')
    access_token = request.headers.get('x-access-token')
    auth_service = AuthService(access_token=access_token, email=email)

    item, code = auth_service.validate_access_token()
    if not item:
        return 'FAIL', 404

    return f'{item}', 200


@auth_blueprint.route(rule='/refresh', methods=['POST'], endpoint='refresh_token')
def refresh_token():
    email = request.headers.get('x-user-email')
    access_token = request.headers.get('access_token')
    auth_service = AuthService(access_token=access_token, email=email)

    item, code = auth_service.refresh_access_token()
    if not item:
        return code, 404

    return f'{item}', 200
