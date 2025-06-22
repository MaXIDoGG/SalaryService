from typing import List

from fastapi import APIRouter, Depends

from src.depends import get_coefficient_service
from src.schemas.coefficient import Coefficient
from src.services.coefficients import CoefficientService

router = APIRouter(prefix="/coefficients", tags=["coefficients"])


@router.get(
   "",
   responses={400: {"description": "Bad request"}},
   response_model=List[Coefficient],
   description="Получение всех коэффициентов",
)
async def get_all_coefficients(
       coefficient_service: CoefficientService = Depends(get_coefficient_service),
) -> List[Coefficient]:
   coefficients = await coefficient_service.get_coefficients()
   return coefficients


@router.post(
   "",
   responses={400: {"description": "Bad request"}},
   response_model=None,
   description="Создание коэффициента",
)
async def create_coefficient(
    new_coef: Coefficient,
    coefficient_service: CoefficientService = Depends(get_coefficient_service),
) -> None:
   await coefficient_service.create_coefficient(new_coef)
   return None
