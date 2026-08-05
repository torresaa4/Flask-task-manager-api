from marshmallow import fields, Schema

class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    email = fields.String()


class TaskSchema(Schema):
    id = fields.Integer()
    to_do = fields.String()
    priority = fields.String()