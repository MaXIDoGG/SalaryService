from enum import Enum

class ParameterType(str, Enum):
    FIRST_RESPONSE_TIME = "Время ответа на первое сообщение"
    NEXT_RESPONSE_TIME = "Время ответа на последующие сообщения"
    POLITENESS_RATING = "Оценка вежливости"
    COMPETENCE_RATING = "Оценка компетентности" 