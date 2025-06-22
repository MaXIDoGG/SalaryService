from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum
from src.database import Base, int_pk
from src.enums.position_type import PositionType

class Employee(Base):
    id: Mapped[int_pk]
    name: Mapped[str]
    surname: Mapped[str]
    patronymic: Mapped[str]
    position: Mapped[PositionType] = mapped_column(SQLEnum(PositionType))
    is_active: Mapped[bool]
    
    shifts: Mapped["Shift"] = relationship("Shift", back_populates="employee")
    stats: Mapped["Stat"] = relationship("Stat", back_populates="employee")
    timeouts: Mapped["Timeout"] = relationship("Timeout", back_populates="employee")
    calc_salary: Mapped["CalcSalary"] = relationship("CalcSalary", back_populates="employee")