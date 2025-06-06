from fastapi import APIRouter, HTTPException

from oscal_api.backend import FileBackend

router = APIRouter()

db = FileBackend()


@router.get("/profiles")
async def list_catalogs():
    """
    Returns a list of available profiles.
    """
    try:
        profiles = db.find_all("profile")
        return {"profiles": profiles}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.get("/profiles/{uuid}")
async def get_profile(uuid: str):
    """
    Returns a single profile.
    """
    try:
        profile = db.find_one("profile", uuid=uuid)
        return {"profile": profile}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
