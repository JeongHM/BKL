from flask import Blueprint, request, jsonify

from services.auth import AuthService
from services.users import UserService
from utills.response_code import RESPONSE_CODE
from utills.decorators import login_required, header_required, response_formatted


users_blueprint = Blueprint(name='users', import_name=__name__)


@users_blueprint.route(rule='', methods=['GET'], endpoint='get_users_list')
@header_required
@login_required
@response_formatted
def get_users_list():
    param = dict(request.args)
    user_service = UserService(param=param)

    validate, code = user_service.validate_user_list_param()
    if not validate:
        return RESPONSE_CODE[code], None, 400

    items, code = user_service.get_users_list()
    if items is False:
        return RESPONSE_CODE[code], None, 400
    if items is None:
        return RESPONSE_CODE[code], None, 204

    return RESPONSE_CODE[code], items, 200


@users_blueprint.route(rule='/detail', methods=['GET'], endpoint='get_user_detail')
@header_required
@login_required
@response_formatted
def get_user_detail():
    param = dict(request.args)
    user_service = UserService(param=param)
    items, code = user_service.get_user_object_by_email()
    if not items:
        return RESPONSE_CODE[code], None, 400

    return RESPONSE_CODE[code], items, 200


@users_blueprint.route(rule='/signup', methods=['POST'], endpoint='user_signup')
@header_required
@response_formatted
def user_signup():
    body = request.get_json()
    user_service = UserService(body=body)
    validate, code = user_service.validate_signup_body()

    if not validate:
        return RESPONSE_CODE[code], None, 400

    items, code = user_service.user_signup()
    if not items:
        return RESPONSE_CODE[code], None, 400

    return RESPONSE_CODE[code], None, 201


@users_blueprint.route(rule='/signin', methods=['POST'], endpoint='user_signin')
@header_required
@response_formatted
def user_signin():
    body = request.get_json()
    email = body.get('email')
    user_service = UserService(body=body)

    validate, code = user_service.validate_signin_body()
    if not validate:
        return RESPONSE_CODE[code], None, 400

    item, code = user_service.user_signin()
    if not item:
        return RESPONSE_CODE[code], None, 400

    access_token, code = AuthService.generate_access_token(email=email)
    if not access_token:
        return RESPONSE_CODE[code], None, 400

    return RESPONSE_CODE[code], access_token, 200


@users_blueprint.route(rule='/signout', methods=['POST'], endpoint='user_signout')
@header_required
@login_required
@response_formatted
def user_signout():
    email = request.headers.get('x-user-email')
    item, code = UserService.user_signout(email=email)
    if not item:
        return RESPONSE_CODE[code], None, 400
    return RESPONSE_CODE[code], None, 200

