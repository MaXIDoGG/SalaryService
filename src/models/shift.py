from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.database import Base, int_pk
from datetime import date

class Shift(Base):
    id: Mapped[int_pk]
    start_date: Mapped[date]
    end_date: Mapped[date]
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)

    employee: Mapped["Employee"] = relationship("Employee", back_populates="shifts")
    stats: Mapped["Stat"] = relationship("Stat", back_populates="shift")