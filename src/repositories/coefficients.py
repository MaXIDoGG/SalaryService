from typing import List

from src.database import async_session_maker
from sqlalchemy import select, update
from src.models.coefficient import Coefficient as CoefficientModel
from src.schemas.coefficient import Coefficient


class CoefficientRepository:

   async def get_coefficients(self) -> List[Coefficient]:
       session = async_session_maker()
       results = await session.execute(select(CoefficientModel))
       coefficients = results.scalars().all()
       coefficients = [Coefficient.model_validate(c) for c in coefficients]
       await session.close()
       return coefficients

   async def create_coefficient(self, coef: Coefficient) -> None:
       session = async_session_maker()
       db_coefficient = CoefficientModel(
            parameter=coef.parameter,
            type=coef.type,
            norm=coef.norm,
            base=coef.base,
            weight=coef.weight,
            is_positive=coef.is_positive
        )
       session.add(db_coefficient)
       await session.commit()
       await session.close()
       return None
