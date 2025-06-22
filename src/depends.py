from src.repositories.coefficients import CoefficientRepository
from src.services.coefficients import CoefficientService

coefficient_repository = CoefficientRepository()

coefficient_service = CoefficientService(coefficient_repository)


def get_coefficient_service() -> CoefficientService:
   return coefficient_service
