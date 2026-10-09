from fastapi import FastAPI

from database import Base, engine
from models import Incident


Base.metadata.create_all(bind=engine, tables=[Incident.__table__])


app = FastAPI(
    title="ReportaYa API",
    description="Servicio para registrar y gestionar incidencias.",
    version="0.1.0",
)


@app.get("/")
def get_home():
    return {"message": "API de ReportaYa funcionando"}
