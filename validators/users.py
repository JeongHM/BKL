from marshmallow import Schema, fields
from marshmallow.validate import Length


class UserListSchema(Schema):
    page = fields.Int(allow_none=True, required=False)
    size = fields.Int(allow_none=True, required=False)


class UserSignUpSchema(Schema):
    name = fields.Str(required=True, validate=Length(min=1, max=24))
    birth = fields.Date(allow_none=True, required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=Length(min=8, max=255))


class UserSignInSchema(Schema):
    email = fields.Email(allow_none=False, required=True)
    password = fields.Str(allow_none=False, required=True)

