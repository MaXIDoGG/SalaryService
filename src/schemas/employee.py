from datetime import datetime
from pydantic import BaseModel, ConfigDict
from src.enums.position_type import PositionType

class Employee(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    surname: str
    patronymic: str
    position: PositionType
    is_active: bool