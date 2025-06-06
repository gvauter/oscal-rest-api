from fastapi import APIRouter, HTTPException

from oscal_api.backend import FileBackend

router = APIRouter()

db = FileBackend()

@router.get("/catalogs")
async def list_catalogs():
    """
    Returns a list of available catalogs.
    """
    try:
        catalogs = db.find_all("catalog")
        return {"catalogs": catalogs}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.get("/catalogs/{uuid}")
async def get_catalog(uuid: str):
    """
    Returns a single catalog.
    """
    try:
        catalog = db.find_one("catalog", uuid=uuid)
        return {"catalog": catalog}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
