from flask import Blueprint, request, jsonify

from services.users import UserService

users_blueprint = Blueprint(name='users', import_name=__name__)


@users_blueprint.route(rule='', methods=['GET'], endpoint='get_users_list')
def get_users_list():
    param = dict(request.args)
    user_service = UserService(param=param)

    validate = user_service.validate_user_list_param()
    if not validate:
        return 'FAIL', 404

    items, code = user_service.get_users_list()
    if not items:
        return code, 404

    return jsonify(items), 200


@users_blueprint.route(rule='/detail', methods=['GET'], endpoint='get_user_detail')
def get_user_detail():
    param = dict(request.args)
    user_service = UserService(param=param)
    items, code = user_service.get_user_object_by_email()
    if not items:
        return 'FAIL', 404

    return items, 200


@users_blueprint.route(rule='/signup', methods=['POST'], endpoint='user_signup')
def user_signup():
    body = request.get_json()
    user_service = UserService(body=body)
    validate = user_service.validate_signup_body()

    if not validate:
        return 'FAIL', 404

    items, code = user_service.user_signup()
    if not items:
        return code, 404

    return 'SUCCESS', 200


@users_blueprint.route(rule='/signin', methods=['POST'], endpoint='user_signin')
def user_signin():
    body = request.get_json()
    user_service = UserService(body=body)

    return 'SUCCESS', 200


@users_blueprint.route(rule='/signout', methods=['POST'], endpoint='user_signout')
def user_signout():
    body = request.get_json()
    user_service = UserService(body=body)

    return 'SUCCESS', 200

