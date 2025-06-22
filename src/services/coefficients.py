from typing import List

from src.repositories.coefficients import CoefficientRepository
from src.schemas.coefficient import Coefficient


class CoefficientService:

   def __init__(self, repository: CoefficientRepository) -> None:
       self.repository = repository

   async def get_coefficients(self) -> List[Coefficient]:
       result = await self.repository.get_coefficients()
       return result
  
   async def create_coefficient(self, coef: Coefficient) -> None:
       await self.repository.create_coefficient(coef)
       return None
