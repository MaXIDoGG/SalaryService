from typing import List

from src.repositories.coefficients import CoefficientRepository
from src.schemas.coefficient import Coefficient, CoefficientRead


class CoefficientService:

    def __init__(self, repository: CoefficientRepository) -> None:
        self.repository = repository

    async def get_coefficients(self) -> List[CoefficientRead]:
        results = await self.repository.get_coefficients()
        return [CoefficientRead.model_validate(c) for c in results]
    
    async def get_coefficient_by_id(self, id) -> CoefficientRead:
        result = await self.repository.get_coefficient_by_id(id)
        return CoefficientRead.model_validate(result)

    async def create_coefficient(self, coef: Coefficient) -> CoefficientRead:
        result = await self.repository.create_coefficient(coef)
        return CoefficientRead.model_validate(result)
