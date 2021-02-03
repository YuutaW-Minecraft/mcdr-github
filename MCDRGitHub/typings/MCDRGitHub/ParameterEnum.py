from enum import Enum

class ParameterEnum(Enum):
    def __str__(self):
        return str(self.value)
