from datetime import datetime
from pydantic import BaseModel, ConfigDict
from src.enums.parameter_type import ParameterType
from src.enums.coefficient_type import CoefficientType

class Coefficient(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    parameter: ParameterType
    type: CoefficientType
    norm: float
    base: float
    weight: float
    is_positive: bool
