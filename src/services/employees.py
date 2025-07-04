from typing import List

from src.repositories.employees import EmployeeRepository
from src.repositories.coefficients import CoefficientRepository
from src.schemas.employee import Employee, EmployeeRead, Shift, ShiftRead, Timeout, TimeoutRead, Stat, StatRead
from src.enums import StatusType


class EmployeeService:

    def __init__(self, repository: EmployeeRepository) -> None:
        self.repository = repository
        

    async def get_employees(self) -> List[EmployeeRead]:
        employees = await self.repository.get_employees()
        result = [EmployeeRead.model_validate(c) for c in employees]
        return result

    async def get_employee_by_id(self, id) -> EmployeeRead | None:
        employee = await self.repository.get_employee_by_id(id)
        return EmployeeRead.model_validate(employee)

    async def create_employee(self, new_employee: Employee) -> EmployeeRead:
        employee = await self.repository.create_employee(new_employee)
        return EmployeeRead.model_validate(employee)
    
    async def create_employee_shift(self, employee_id: int, shift: Shift) -> ShiftRead:
        employee = await self.repository.get_employee_by_id(employee_id)
        if employee:
            new_shift = await self.repository.create_employee_shift(employee, shift)
            await self.repository.change_employee_status(employee, StatusType.WORKING)
            return ShiftRead.model_validate(new_shift)
        else:
            raise Exception("Не удалось найти такого сотрудника")
    
    async def create_employee_timeout(self, employee_id: int, timeout: Timeout) -> TimeoutRead:
        employee = await self.repository.get_employee_by_id(employee_id)
        if employee:
            new_timeout = await self.repository.create_employee_timeout(employee, timeout)
            await self.repository.change_employee_status(employee, StatusType.BREAK)
            return TimeoutRead.model_validate(new_timeout)
        else:
            raise Exception("Не удалось найти такого сотрудника")
    
    async def create_shift_stat(self, shift_id: int, stat: Stat) -> StatRead:
        shift = await self.repository.get_shift_by_id(shift_id)
        if shift:
            new_stat = await self.repository.create_shift_stat(shift, stat)
            return StatRead.model_validate(new_stat)
        else:
            raise Exception("Не удалось найти такой смены")
        
    async def calculate_salary(self, employee_id: int):
        total_complaints = await self.repository.get_stats_complaint(employee_id)
        
        # Получаем коэффициент для жалоб
        coeff_repository = CoefficientRepository()
        complaint_coeff = await coeff_repository.get_complaint_coefficient()
        
        if complaint_coeff:
            if total_complaints > complaint_coeff.base:
                salary_penalty = (total_complaints - complaint_coeff.base) * complaint_coeff.weight
            else:
                salary_penalty = 0.0
        else:
            raise Exception("Нет коэффициента для жалобы")
        
        # Обновляем CalcSalary
        salary_record = CalcSalary(
            parameter=ParameterType.CLIENT_COMPLAINT,
            total=-salary_penalty,  # Отрицательное значение
            employee_id=employee_id
        )
        
        
            
            
        
   
