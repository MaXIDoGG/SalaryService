from src.repositories.coefficients import CoefficientRepository
from src.services.coefficients import CoefficientService

from src.repositories.employees import EmployeeRepository
from src.services.employees import EmployeeService

coefficient_repository = CoefficientRepository()
coefficient_service = CoefficientService(coefficient_repository)

employee_repository = EmployeeRepository()
employee_service = EmployeeService(employee_repository)


def get_coefficient_service() -> CoefficientService:
   return coefficient_service

def get_employee_service() -> EmployeeService:
   return employee_service
