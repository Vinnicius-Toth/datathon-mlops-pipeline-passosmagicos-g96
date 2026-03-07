from fastapi import FastAPI
from app.routes.health import router as health_router

app = FastAPI(
    title="Infra API",
    description="API deployed with Terraform + AWS",
    version="1.0.0"
)

app.include_router(health_router)


@app.get("/")
def root():
    return {"message": "API is running 🚀"}
