from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ENUM
from src.database import Base, int_pk
from src.enums.parameter_type import ParameterType
from src.enums.coefficient_type import CoefficientType

class Coefficient(Base):
    id: Mapped[int_pk]
    parameter: Mapped[ParameterType] = mapped_column(ENUM(ParameterType, create_type=False))
    type: Mapped[CoefficientType] = mapped_column(ENUM(CoefficientType))
    norm: Mapped[float]
    base: Mapped[float]
    weight: Mapped[float]
    is_positive: Mapped[bool]
    
    
    
    