from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum
from src.database import Base, str_uniq, int_pk, str_null_true
from datetime import date
from enum import Enum

class Shift(Base):
    id: Mapped[int_pk]
    start_date: Mapped[date]
    end_date: Mapped[date]
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)

    employee: Mapped["Employee"] = relationship("Employee", back_populates="shifts")

    

    