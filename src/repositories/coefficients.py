from typing import List

from src.database import async_session_maker
from sqlalchemy import select, update
from src.models.coefficient import Coefficient as CoefficientDb
from src.schemas.coefficient import Coefficient, CoefficientRead
from src.enums import CoefficientType, ParameterType


class CoefficientRepository:

    async def get_coefficients(self) -> List[CoefficientDb]:
        async with async_session_maker() as session:
            results = await session.execute(select(CoefficientDb))
            coefficients = results.scalars().all()
            return list(coefficients)
    
    async def get_coefficient_by_id(self, id) -> CoefficientDb | None:
        async with async_session_maker() as session:
            result = await session.execute(select(CoefficientDb).where(CoefficientDb.id == id))
            coefficient = result.scalars().one_or_none()
            return coefficient
    
    async def get_complaint_coefficient(self) -> CoefficientDb | None:
        async with async_session_maker() as session:
            result = await session.execute(select(CoefficientDb).where(CoefficientDb.parameter == ParameterType.CLIENT_COMPLAINT and CoefficientDb.type == CoefficientType.NEGATIVE))
            coefficient = result.scalar_one_or_none()
            return coefficient

    async def create_coefficient(self, coef: Coefficient) -> CoefficientDb:
        async with async_session_maker() as session:
            db_coefficient = CoefficientDb(
                    parameter=coef.parameter,
                    type=coef.type,
                    norm=coef.norm,
                    base=coef.base,
                    weight=coef.weight,
                    is_positive=coef.is_positive
                )
            session.add(db_coefficient)
            await session.commit()
            await session.refresh(db_coefficient)
            return db_coefficient