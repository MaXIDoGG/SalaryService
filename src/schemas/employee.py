from datetime import datetime
from pydantic import BaseModel, ConfigDict
from datetime import date
from src.enums import PositionType, StatusType, ParameterType

class Employee(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    surname: str
    patronymic: str
    position: PositionType
    dismissed: bool
    status: StatusType
    
class EmployeeRead(Employee):
    id: int
    
class Shift(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    start_date: date
    end_date: date
    
class ShiftRead(Shift):
    id: int

class Timeout(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    start_date: date
    end_date: date
    
class TimeoutRead(Timeout):
    id: int
    
class Stat(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    date: date
    parameter: ParameterType
    value: float
    employee_id: int
    shift_id: int

class StatRead(Stat):
    id: int
    
