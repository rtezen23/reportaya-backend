from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from database import get_database
from models import Incident
from schemas import IncidentCreate, IncidentResponse, IncidentStatus


router = APIRouter(prefix="/api/incidencias", tags=["Incidencias"])


@router.post("", response_model=IncidentResponse, status_code=status.HTTP_201_CREATED)
def create_incident(
    incident_data: IncidentCreate,
    database: Session = Depends(get_database),
):
    incident = Incident(
        code=f"TMP-{uuid4().hex[:11]}",
        registration_date=incident_data.registration_date,
        registration_time=incident_data.registration_time,
        incident_type=incident_data.incident_type,
        description=incident_data.description,
        location=incident_data.location,
        status=IncidentStatus.PENDING.value,
        registered_by=incident_data.registered_by,
    )

    try:
        database.add(incident)
        database.flush()
        incident.code = f"INC-{incident.id:04d}"
        database.commit()
        database.refresh(incident)
    except SQLAlchemyError as error:
        database.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se pudo registrar la incidencia.",
        ) from error

    return incident
