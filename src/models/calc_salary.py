from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum
from src.database import Base, str_uniq, int_pk, str_null_true
from datetime import date
from enum import Enum

class ParameterType(str, Enum):
    FIRST_RESPONSE_TIME = "Время ответа на первое сообщение"
    NEXT_RESPONSE_TIME = "Время ответа на последующие сообщения"
    POLITENESS_RATING = "Оценка вежливости"
    COMPETENCE_RATING = "Оценка компетентности"

class CalcSalary(Base):
    id: Mapped[int_pk]
    parameter: Mapped[ParameterType] = mapped_column(SQLEnum(ParameterType))
    total: Mapped[float]
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)

    employee: Mapped["Employee"] = relationship("Employee", back_populates="CalcSalary")