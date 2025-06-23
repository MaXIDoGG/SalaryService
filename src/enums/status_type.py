from enum import Enum

class StatusType(str, Enum):
    WORKING = "Работает"
    BREAK = "На перерыве"
    NOT_WORKING = "Не работает"