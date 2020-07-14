from marshmallow import Schema, fields


class TokenSchema(Schema):
    access_token = fields.Str(allow_none=False, required=True)
