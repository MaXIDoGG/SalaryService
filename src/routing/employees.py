from typing import List

from fastapi import APIRouter, Depends

from src.depends import get_employee_service
from src.schemas.employee import Employee
from src.services.employees import EmployeeService

router = APIRouter(prefix="/employees", tags=["employees"])


@router.get(
   "",
   responses={400: {"description": "Bad request"}},
   response_model=List[Employee],
   description="Получение всех сотрудников",
)
async def get_all_employees(
       employee_service: EmployeeService = Depends(get_employee_service),
) -> List[Employee]:
   employees = await employee_service.get_employees()
   return employees


@router.post(
   "",
   responses={400: {"description": "Bad request"}},
   response_model=None,
   description="Создание сотрудника",
)
async def create_employee(
    new_employee: Employee,
    employee_service: EmployeeService = Depends(get_employee_service),
) -> None:
   await employee_service.create_employee(new_employee)
   return None
