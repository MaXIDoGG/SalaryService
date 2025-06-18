from fastapi import FastAPI


app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")