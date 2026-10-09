from fastapi import FastAPI


app = FastAPI(
    title="ReportaYa API",
    description="Servicio para registrar y gestionar incidencias.",
    version="0.1.0",
)


@app.get("/")
def get_home():
    return {"message": "API de ReportaYa funcionando"}
