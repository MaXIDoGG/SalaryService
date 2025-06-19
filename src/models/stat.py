from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ENUM
from src.database import Base, str_uniq, int_pk, str_null_true
from datetime import date
from .enums.parameter_type import ParameterType

class Stat(Base):
    id: Mapped[int_pk]
    date: Mapped[date]
    parameter: Mapped[ParameterType] = mapped_column(ENUM(ParameterType, create_type=False))
    value: Mapped[float]
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)
    shift_id: Mapped[int] = mapped_column(ForeignKey("shifts.id"), nullable=False)

    employee: Mapped["Employee"] = relationship("Employee", back_populates="stats")
    shift: Mapped["Shift"] = relationship("Shift", back_populates="stats")