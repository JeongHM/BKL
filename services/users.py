from flask import current_app

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

    def validate_user_list_param(self) -> bool:
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
            return False

        else:
            return True

    def validate_signup_body(self) -> bool:
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
            return False

        else:
            return True

    def validate_signin_body(self) -> bool:
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
            return False

        else:
            return True

    def get_users_list(self) -> tuple:
        """
        Get users list business logic
        :return: Boolean, (String or List)
        """
        try:
            pass

        except Exception as e:
            current_app.logger.error(e)
            return False, None

        else:
            return False, None

    def user_signup(self) -> tuple:
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

    def user_signin(self) -> tuple:
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



