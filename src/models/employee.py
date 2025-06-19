from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum
from src.database import Base, str_uniq, int_pk, str_null_true
from datetime import date
from enum import Enum

class PositionType(str, Enum):
    HEAD = "Руководитель"
    SUPER_OPERATOR = "Супероператор"
    SENIOR_OPERATOR = "Старший оператор"
    OPERATOR = "Оператор"

class Employee(Base):
    id: Mapped[int_pk]
    name: Mapped[str]
    name_2: Mapped[str]
    surname: Mapped[str]
    patronymic: Mapped[str]
    position: Mapped[PositionType] = mapped_column(SQLEnum(PositionType))
    is_active: Mapped[bool]
    
    shifts: Mapped["Shift"] = relationship("Shift", back_populates="employee")
    stats: Mapped["Stat"] = relationship("Stat", back_populates="employee")