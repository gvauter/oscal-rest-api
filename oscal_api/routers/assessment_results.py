import os
import glob
import shutil

from fastapi import APIRouter, HTTPException, Request, UploadFile
from fastapi.responses import FileResponse

from oscal_api.backend import FileBackend

router = APIRouter()

db = FileBackend("./files")

@router.get("/assessment-results")
async def list_assessment_results():
    """
    Returns a list of available assessment results.
    """
    try:
        assessment_results = db.find_all("assessment-results")
        return {
            "assessment-results": assessment_results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.get("/assessment-results/{uuid}")
async def get_assessment_results(uuid: str):
    """
    Returns a single assessment results.
    """
    try:
        assessment_results = db.find_one("assessment-results", uuid)
        return {"assessment-results": assessment_results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.post("/assessment-results", status_code=201)
async def create_assessment_results(request: Request):
    """
    Create a new assessment results.
    """
    try:
        data: bytes = await request.json()
        db.create_one("assessment-results", data)
        return {
            "assessment-results": {
                "uuid": data["assessment-results"]["uuid"],
                "metadata": data["assessment-results"]["metadata"]
            }
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.post("/assessment-results/{uuid}/relevent-evidences/upload", status_code=201)
async def upload_relevent_evidences(uuid: str, file: UploadFile):
    """
    Upload relevent evidence for an assessment results.
    """
    try:
        dir_path = f"./files/assessment-results/{uuid}/evidence/"
        os.makedirs(dir_path, exist_ok=True)
        with open(f"{dir_path}/{file.filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            return {"filename": file.filename}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@router.get("/assessment-results/{uuid}/relevent-evidences")
async def list_relevent_evidences(uuid: str):
    """
    List relevent evidences for an assessment results.
    """
    try:
        dir_path = f"./files/assessment-results/{uuid}/evidence/*"
        files = glob.glob(dir_path)
        filenames = [f.split("/")[-1] for f in files]
        return {
            "relevent-evidences": filenames
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.get("/assessment-results/{uuid}/relevent-evidences/{filename}")
async def list_relevent_evidences(uuid: str, filename: str):
    """
    Download a relevent evidences item.
    """
    try:
        file_path = f"./files/assessment-results/{uuid}/evidence/{filename}"
        return FileResponse(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
