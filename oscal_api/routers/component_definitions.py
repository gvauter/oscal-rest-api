from fastapi import APIRouter, HTTPException

from oscal_api.backend import FileBackend

router = APIRouter()

db = FileBackend()

@router.get("/component-definitions")
async def list_component_definitions():
    """
    Returns a list of available component definitions.
    """
    try:
        component_definitions = db.find_all("component-definition")
        return {
            "component-definitions": component_definitions
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.get("/component-definitions/{uuid}")
async def get_component_definition(uuid):
    """
    Returns a single component definition.
    """
    try:
        component_definition = db.find_one("component-definition", uuid)
        return {
            "component-definition": component_definition
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

