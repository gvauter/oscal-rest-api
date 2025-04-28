from fastapi import Depends, FastAPI

from oscal_api.routers import catalogs

app = FastAPI()

app.include_router(catalogs.router)

@app.get("/health")
async def health():
    return {"status": "ok"}
