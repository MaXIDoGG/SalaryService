from typing import List

from src.repositories.employees import EmployeeRepository
from src.schemas.employee import Employee


class EmployeeService:

   def __init__(self, repository: EmployeeRepository) -> None:
       self.repository = repository

   async def get_employees(self) -> List[Employee]:
       result = await self.repository.get_employees()
       return result
  
   async def create_employee(self, new_employee: Employee) -> None:
       await self.repository.create_employee(new_employee)
       return None
