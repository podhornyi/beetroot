import json

from marshmallow import Schema, fields, pre_load


class PersonSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)

    @pre_load
    def fill_age(self, data, **kwargs):
        if 'age' not in data:
            data['age'] = 999
        return data


class DataEventSchema(Schema):
    persons = fields.Nested(PersonSchema, many=True)


#################################################################################
# FRONTEND
#################################################################################
def get_frontend_request() -> str:
    return """
            {
                "persons": [
                    {
                        "name": "Ivan",
                        "age": 12
                    },
                    {
                        "name": "Kola",
                        "age": 122
                    },
                    {
                        "name": "Petro"
                    }
                ]
            }
        """


#################################################################################
# BACKEND 1
#################################################################################
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return str(self.name)


payload = json.loads(get_frontend_request())
data = DataEventSchema()
payload = data.loads(get_frontend_request())

print(payload)


