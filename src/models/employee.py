from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import ENUM
from datetime import date
from typing import List
from src.database import Base, int_pk
from src.enums.position_type import PositionType
from src.enums.parameter_type import ParameterType
from src.enums.position_type import PositionType
from src.enums.status_type import StatusType

class Employee(Base):
    id: Mapped[int_pk]
    name: Mapped[str]
    surname: Mapped[str]
    patronymic: Mapped[str]
    position: Mapped[PositionType] = mapped_column(SQLEnum(PositionType))
    dismissed: Mapped[bool] = mapped_column(Boolean, default=False)
    status: Mapped[StatusType] = mapped_column(SQLEnum(StatusType), default=StatusType.NOT_WORKING)
    
    shifts: Mapped[List["Shift"]] = relationship("Shift", back_populates="employee")
    stats: Mapped[List["Stat"]] = relationship("Stat", back_populates="employee")
    timeouts: Mapped[List["Timeout"]] = relationship("Timeout", back_populates="employee")
    calc_salary: Mapped["CalcSalary"] = relationship("CalcSalary", back_populates="employee")
    
class Shift(Base):
    id: Mapped[int_pk]
    start_date: Mapped[date]
    end_date: Mapped[date]
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)

    employee: Mapped["Employee"] = relationship("Employee", back_populates="shifts", lazy=False)
    stats: Mapped[List["Stat"]] = relationship("Stat", back_populates="shift")
    
class Timeout(Base):
    id: Mapped[int_pk]
    start_date: Mapped[date]
    end_date: Mapped[date]
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)

    employee: Mapped["Employee"] = relationship("Employee", back_populates="timeouts")
    
class Stat(Base):
    id: Mapped[int_pk]
    date: Mapped[date]
    parameter: Mapped[ParameterType] = mapped_column(ENUM(ParameterType, create_type=False))
    value: Mapped[float]
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)
    shift_id: Mapped[int] = mapped_column(ForeignKey("shifts.id"), nullable=False)

    employee: Mapped["Employee"] = relationship("Employee", back_populates="stats")
    shift: Mapped["Shift"] = relationship("Shift", back_populates="stats")
    
class CalcSalary(Base):
    id: Mapped[int_pk]
    parameter: Mapped[ParameterType] = mapped_column(ENUM(ParameterType, create_type=False))
    total: Mapped[float]
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)

    employee: Mapped["Employee"] = relationship("Employee", back_populates="calc_salary")