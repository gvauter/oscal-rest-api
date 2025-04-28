from fastapi import APIRouter

router = APIRouter()

@router.get("/catalogs")
async def list_catalogs() :
    return {
        "catalogs": [
            {
                "uuid": "catalog-1",
            },
            {
                "uuid": "catalog-2",
            },
            {
                "uuid": "catalog-3",
            }
        ]
    }

@router.get("/catalogs/{uuid}")
async def get_catalog(uuid):
    return {
        "catalog": {
            "uuid": uuid,
            "metadata": {
                "title": "Example catalog"
            }
        }
    }


