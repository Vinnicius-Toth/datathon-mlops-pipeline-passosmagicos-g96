from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/health",
    summary="Health Check",
    tags=["Infra"]
)
def health():
    return {"status": "ok"} 