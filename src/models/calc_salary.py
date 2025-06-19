from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ENUM
from src.database import Base, int_pk
from .enums.parameter_type import ParameterType

class CalcSalary(Base):
    id: Mapped[int_pk]
    parameter: Mapped[ParameterType] = mapped_column(ENUM(ParameterType, create_type=False))
    total: Mapped[float]
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)

    employee: Mapped["Employee"] = relationship("Employee", back_populates="calc_salary")