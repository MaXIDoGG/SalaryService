from typing import List

from fastapi import APIRouter, Depends

from src.depends import get_employee_service
from src.schemas.employee import Employee, EmployeeRead, Shift, ShiftRead, Timeout, TimeoutRead, Stat, StatRead
from src.services.employees import EmployeeService

router = APIRouter(prefix="/employees", tags=["employees"])


@router.get(
   "",
   responses={400: {"description": "Bad request"}},
   response_model=List[EmployeeRead],
   description="Получение всех сотрудников",
)
async def get_all_employees(
       employee_service: EmployeeService = Depends(get_employee_service),
) -> List[EmployeeRead]:
   employees = await employee_service.get_employees()
   return employees


@router.post(
   "",
   responses={400: {"description": "Bad request"}},
   response_model=EmployeeRead,
   description="Создание сотрудника",
)
async def create_employee(
    new_employee: Employee,
    employee_service: EmployeeService = Depends(get_employee_service),
) -> EmployeeRead:
   employee = await employee_service.create_employee(new_employee)
   return employee

@router.post(
   "/shift",
   responses={400: {"description": "Bad request"}},
   response_model=ShiftRead,
   description="Создание смены",
)
async def create_shift(
    employee_id: int,
    new_shift: Shift,
    employee_service: EmployeeService = Depends(get_employee_service),
) -> ShiftRead:
   shift = await employee_service.create_employee_shift(employee_id, new_shift)
   return shift

@router.post(
   "/timeout",
   responses={400: {"description": "Bad request"}},
   response_model=ShiftRead,
   description="Создание перерыва",
)
async def create_timeout(
    employee_id: int,
    new_timeout: Timeout,
    employee_service: EmployeeService = Depends(get_employee_service),
) -> TimeoutRead:
   timeout = await employee_service.create_employee_timeout(employee_id, new_timeout)
   return timeout

@router.post(
   "/stat",
   responses={400: {"description": "Bad request"}},
   response_model=StatRead,
   description="Добавление статистики",
)
async def create_stat(
   shift_id: int,
   new_stat: Stat,
   employee_service: EmployeeService = Depends(get_employee_service),
) -> StatRead:
   stat = await employee_service.create_shift_stat(shift_id, new_stat)
   return stat