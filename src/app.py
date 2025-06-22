from fastapi import FastAPI
from src.routing.coefficients import router as coef_router
from src.routing.employees import router as employee_router


app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")
app.include_router(coef_router)
app.include_router(employee_router)