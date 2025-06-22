from typing import List

from src.database import async_session_maker
from sqlalchemy import select, update
from src.models.employee import Employee as EmployeeModel
from src.schemas.employee import Employee


class EmployeeRepository:

   async def get_employees(self) -> List[Employee]:
       session = async_session_maker()
       results = await session.execute(select(EmployeeModel))
       employees = results.scalars().all()
       employees = [Employee.model_validate(c) for c in employees]
       await session.close()
       return employees

   async def create_employee(self, new_employee: Employee) -> None:
       session = async_session_maker()
       db_employee = EmployeeModel(
            name=new_employee.name,
            surname=new_employee.surname,
            patronymic=new_employee.patronymic,
            position=new_employee.position,
            is_active=new_employee.is_active
        )
       session.add(db_employee)
       await session.commit()
       await session.close()
       return None
