from enum import Enum

class PositionType(str, Enum):
    HEAD = "Руководитель"
    SUPER_OPERATOR = "Супероператор"
    SENIOR_OPERATOR = "Старший оператор"
    OPERATOR = "Оператор"