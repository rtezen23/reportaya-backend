from datetime import date, datetime, time
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, field_validator


class IncidentType(str, Enum):
    WATER_LEAK = "Fuga de agua"
    ELEVATOR = "Ascensor"
    NOISE = "Ruido"
    SECURITY = "Seguridad"
    CLEANING = "Limpieza"
    OTHER = "Otro"


class IncidentStatus(str, Enum):
    PENDING = "Pendiente"
    IN_PROGRESS = "En proceso"
    ATTENDED = "Atendido"
    REJECTED = "Rechazado"


class IncidentBase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        str_strip_whitespace=True,
        extra="forbid",
    )

    registration_date: date = Field(alias="fechaRegistro")
    registration_time: time = Field(alias="horaRegistro")
    incident_type: IncidentType = Field(alias="tipoIncidencia")
    description: str = Field(alias="descripcion", min_length=10, max_length=250)
    location: str = Field(alias="ubicacion", min_length=1, max_length=60)
    registered_by: str = Field(alias="usuarioRegistro", min_length=1, max_length=50)

    @field_validator("registration_date")
    @classmethod
    def validate_registration_date(cls, value: date):
        if value > date.today():
            raise ValueError("la fecha de registro no puede ser futura")
        return value


class IncidentCreate(IncidentBase):
    pass


class IncidentUpdate(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        str_strip_whitespace=True,
        extra="forbid",
    )

    incident_type: IncidentType | None = Field(default=None, alias="tipoIncidencia")
    description: str | None = Field(
        default=None,
        alias="descripcion",
        min_length=10,
        max_length=250,
    )
    location: str | None = Field(
        default=None,
        alias="ubicacion",
        min_length=1,
        max_length=60,
    )
    status: IncidentStatus | None = Field(default=None, alias="estado")
    attention_note: str | None = Field(
        default=None,
        alias="observacionAtencion",
        min_length=1,
        max_length=250,
    )


class IncidentResponse(IncidentBase):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id: int = Field(alias="idIncidencia")
    code: str = Field(alias="codigo")
    status: IncidentStatus = Field(alias="estado")
    attended_at: datetime | None = Field(default=None, alias="fechaAtencion")
    attention_note: str | None = Field(default=None, alias="observacionAtencion")
    is_deleted: bool = Field(alias="eliminado")
    updated_at: datetime = Field(alias="fechaActualizacion")
