from fastapi import FastAPI

from oscal_api.routers import assessment_results
from oscal_api.routers import component_definitions 
from oscal_api.routers import catalogs
from oscal_api.routers import profiles 

app = FastAPI()

app.include_router(assessment_results.router)
app.include_router(catalogs.router)
app.include_router(component_definitions.router)
app.include_router(profiles.router)

@app.get("/health")
async def health():
    return {"status": "ok"}
