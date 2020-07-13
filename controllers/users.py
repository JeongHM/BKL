from flask import Blueprint, request

from services.users import UserService

users_blueprint = Blueprint(name='users', import_name=__name__)


@users_blueprint.route(rule='', methods=['GET'], endpoint='get_users_list')
def get_users_list():
    param = dict(request.args)
    user_service = UserService(param=param)

    return 'SUCCESS', 200


@users_blueprint.route(rule='/{int:user_id}', methods=['GET'], endpoint='get_user_detail')
def get_user_detail(user_id):
    user_service = UserService()

    return 'SUCCESS', 200


@users_blueprint.route(rule='/signup', methods=['POST'], endpoint='user_signup')
def user_signup():
    body = request.get_json()
    user_service = UserService(body=body)

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

