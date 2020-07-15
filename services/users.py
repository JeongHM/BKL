import hashlib

from flask import current_app
from datetime import datetime

from models import mongo
from validators.users import (UserListSchema,
                              UserSignInSchema,
                              UserSignUpSchema)


class UserService(object):
    def __init__(self, param: dict = None, body: dict = None):
        """
        :param param: parameters [GET, DELETE]
        :param body: body [POST, PUT]
        """
        self._param = param
        self._body = body

    def get_user_object_by_email(self) -> tuple:
        """
        get user object by email
        :return:
        """
        try:
            email = self._param.get('email')
            user = mongo.db.users.find_one({'email': email})
            items = UserService.make_user_object(user_list=[user])

        except Exception as e:
            current_app.logger.error(e)
            return False, 'FAIL_USER_LIST_UP'

        else:
            return items, 'SUCCESS'

    @staticmethod
    def make_user_object(user_list: list) -> bool or list:
        """
        make users return format
        :param user_list: Users Model Object
        :return:
        """
        try:
            items = {
                'users': [
                    {
                        'name': user.get('name'),
                        'email': user.get('email'),
                        'birth': user.get('birth')
                    } for user in user_list
                ],
                'total_count': len(user_list)
            }

            if not items:
                return None

        except Exception as e:
            current_app.logger.error(e)
            return False

        else:
            return items

    def validate_user_list_param(self) -> tuple:
        """
        validate parameters when list up users info
        :return: Boolean
        """
        try:
            error = UserListSchema().validate(data=self._param)
            if error:
                raise ValueError(error)

        except Exception as e:
            current_app.logger.error(e)
            return False, 'INVALID_LIST_UP_SCHEMA'

        else:
            return True, 'SUCCESS'

    def validate_signup_body(self) -> tuple:
        """
        validate body parameters when user sign up
        :return: bool
        """
        try:
            error = UserSignUpSchema().validate(data=self._body)
            if error:
                raise ValueError(error)

        except Exception as e:
            current_app.logger.error(e)
            return False, 'INVALID_SIGN_UP_SCHEMA'

        else:
            return True, 'SUCCESS'

    def validate_signin_body(self) -> tuple:
        """
        validate body parameters when user sign in
        :return: bool
        """
        try:
            error = UserSignInSchema().validate(data=self._body)
            if error:
                raise ValueError(error)

        except Exception as e:
            current_app.logger.error(e)
            return False, 'INVALID_SIGN_IN_SCHEMA'

        else:
            return True, 'SUCCESS'

    def get_users_list(self) -> tuple:
        """
        Get users list business logic
        :return: Boolean, (String or List)
        """
        try:
            page, size = int(self._param.get('page')), int(self._param.get('size'))
            users = list(mongo.db.users.find())[(page - 1) * size: (page * size) + 1]
            items = UserService.make_user_object(user_list=users)
            if items is None:
                return False, 'EMPTY_OBJECT'

        except Exception as e:
            current_app.logger.error(e)
            return False, 'FAIL_USER_LIST_UP'

        else:
            return items, 'SUCCESS'

    def user_signup(self) -> tuple:
        """
        user sign up business logic
        :return: Boolean, (String or List)
        """
        try:
            email_check = self.check_email_can_use()
            if not email_check:
                return False, 'ALREADY_EXIST_EMAIL'

            if not self.set_salt_hash_password():
                raise ValueError('Fail to set hash password')

            mongo.db.users.insert(self._body)

        except Exception as e:
            current_app.logger.error(e)
            return False, 'FAIL_USER_SIGN_UP'

        else:
            return True, 'SUCCESS'

    def user_signin(self) -> tuple:
        """
        user sign up business logic
        :return: Boolean, (String or List)
        """
        try:
            if not self.check_password():
                raise ValueError('incorrect password')

        except Exception as e:
            current_app.logger.error(e)
            return False, 'FAIL_USER_SIGN_IN'

        else:
            return True, 'SUCCESS'

    def user_signout(self) -> tuple:
        """
        user sign up business logic
        :return: Boolean, (String or List)
        """
        try:
            pass

        except Exception as e:
            current_app.logger.error(e)
            return False, None

        else:
            return False, None

    def set_salt_hash_password(self) -> bool:
        try:
            salt = str(datetime.utcnow().timestamp()).split('.')[0]
            password = self._body.get('password')
            hash_password = hashlib.sha512(str(salt + password).encode(encoding='utf-8')).hexdigest()

            self._body['password'] = hash_password
            self._body['salt'] = salt

        except Exception as e:
            current_app.logger.error(e)
            return False

        else:
            return True

    def check_password(self) -> bool:
        try:
            email, password = self._body.get('email'), self._body.get('password')

            user = mongo.db.users.find_one({"email": email})
            user_password = user.get('password')
            user_salt = user.get('salt')

            hash_password = hashlib.sha512(str(user_salt + password).encode(encoding='utf-8')).hexdigest()
            if not user_password == hash_password:
                raise ValueError('Incorrect Password')

        except Exception as e:
            current_app.logger.error(e)
            return False

        else:
            return True

    def check_email_can_use(self):
        try:
            user = mongo.db.users.find_one({"email": self._body.get('email')})
            if user:
                raise ValueError('Already Regist Email')

        except Exception as e:
            current_app.logger.error(e)
            return False

        else:
            return True

