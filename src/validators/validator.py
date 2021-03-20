from typing import Dict
from cerberus import Validator


class Message_Validator:
    def __init__(self):
        self.validator = Validator(
            {
                "name": {"type": "string", "required": True},
                "age": {"type": "integer", "min": 10, "required": True},
            }
        )

    def check_message(self, message: Dict):
        return self.validator.validate(message)
