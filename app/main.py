from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="RepairTrack API",
    description="API para gestión de reparaciones de celulares",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "RepairTrack API funcionando"}
