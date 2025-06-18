from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum
from database import Base, str_uniq, int_pk, str_null_true
from datetime import date
from enum import Enum

class PositionType(str, Enum):
    HEAD = "Руководитель"
    SUPER_OPERATOR = "Покупка"
    SENIOR_OPERATOR = "Старший оператор"
    OPERATOR = "Оператор"

class Employee(Base):
    id: Mapped[int_pk]
    name: Mapped[str]
    surname: Mapped[str]
    patronymic: Mapped[str]
    position: Mapped[PositionType] = mapped_column(SQLEnum(AdType), default=AdType.SALE)
    is_active: Mapped[bool]