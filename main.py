from fastapi import FastAPI

from database import Base, engine
from models import Incident
from routers.incidents import router as incidents_router


Base.metadata.create_all(bind=engine, tables=[Incident.__table__])


app = FastAPI(
    title="ReportaYa API",
    description="Servicio para registrar y gestionar incidencias.",
    version="0.1.0",
)

app.include_router(incidents_router)


@app.get("/")
def get_home():
    return {"message": "API de ReportaYa funcionando"}
