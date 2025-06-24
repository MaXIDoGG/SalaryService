from typing import List

from src.database import async_session_maker
from sqlalchemy import select, update, func
from src.models.employee import Employee as EmployeeDb
from src.models.employee import Shift as ShiftDb
from src.models.employee import Timeout as TimeoutDb
from src.models.employee import Stat as StatDb
from src.models.employee import CalcSalary as CalcSalaryDb
from src.schemas.employee import Employee, Shift, Timeout, Stat
from src.enums import StatusType, ParameterType


class EmployeeRepository:

    async def get_employees(self) -> List[EmployeeDb]:
        async with async_session_maker() as session:
            results = await session.execute(select(EmployeeDb))
            employees = results.scalars().all()
            return list(employees)
    
    async def get_employee_by_id(self, id: int) -> EmployeeDb|None:
        async with async_session_maker() as session:
            results = await session.execute(select(EmployeeDb).where(EmployeeDb.id == id))
            employee = results.scalars().one_or_none()
            return employee

    async def create_employee(self, new_employee: Employee) -> EmployeeDb:
        async with async_session_maker() as session:
            db_employee = EmployeeDb(
                    name=new_employee.name,
                    surname=new_employee.surname,
                    patronymic=new_employee.patronymic,
                    position=new_employee.position,
                    dismissed=new_employee.dismissed,
                    status=new_employee.status
                )
            session.add(db_employee)
            await session.commit()
            await session.refresh(db_employee)
            return db_employee
        

    async def create_employee_shift(self, employee: EmployeeDb, shift: Shift) -> ShiftDb:
        async with async_session_maker() as session:
            db_shift = ShiftDb(
                start_date=shift.start_date,
                end_date=shift.end_date,
                employee = employee
            )
            session.add(db_shift)
            await session.commit()
            await session.refresh(db_shift)
            return db_shift
        
    async def get_shift_by_id(self, id: int) -> ShiftDb|None:
        async with async_session_maker() as session:
            result = await session.execute(select(ShiftDb).where(ShiftDb.id == id))
            shift = result.scalars().one_or_none()
            return shift
    
    async def create_employee_timeout(self, employee: EmployeeDb, timeout: Timeout) -> TimeoutDb:
        async with async_session_maker() as session:
            db_timeout = TimeoutDb(
                start_date=timeout.start_date,
                end_date=timeout.end_date,
                employee = employee
            )
            session.add(db_timeout)
            await session.commit()
            await session.refresh(db_timeout)
            return db_timeout
    
    async def change_employee_status(self, employee: EmployeeDb, status: StatusType) -> EmployeeDb:
        async with async_session_maker() as session:
            employee.status = status
            session.add(employee)
            await session.commit()
            return employee
        
    async def create_shift_stat(self, shift: ShiftDb, stat: Stat) -> StatDb:
        async with async_session_maker() as session:
            db_stat = StatDb(
                date = stat.date,
                parameter = stat.parameter,
                value = stat.value,
                employee = shift.employee,
                shift = shift
            )
            session.add(db_stat)
            await session.commit()
            await session.refresh(db_stat)
            return db_stat
        
    async def get_stats_complaint(self, employee_id):
        async with async_session_maker() as session:
            total_complaints = await session.execute(
                select(func.sum(StatDb.value))
                .where(
                    (StatDb.employee_id == employee_id) &
                    (StatDb.parameter == ParameterType.CLIENT_COMPLAINT))
            )
            return total_complaints.scalar() or 0.0
            
           
