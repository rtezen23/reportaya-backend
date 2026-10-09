from datetime import date, datetime, time

from sqlalchemy import Boolean, Date, DateTime, Integer, String, Time, false, func
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Incident(Base):
    __tablename__ = "INCIDENCIA"

    id: Mapped[int] = mapped_column(
        "idIncidencia", Integer, primary_key=True, autoincrement=True
    )
    code: Mapped[str] = mapped_column("codigo", String(15), unique=True, nullable=False)
    registration_date: Mapped[date] = mapped_column(
        "fechaRegistro", Date, nullable=False
    )
    registration_time: Mapped[time] = mapped_column(
        "horaRegistro", Time, nullable=False
    )
    incident_type: Mapped[str] = mapped_column(
        "tipoIncidencia", String(30), nullable=False
    )
    description: Mapped[str] = mapped_column(
        "descripcion", String(250), nullable=False
    )
    location: Mapped[str] = mapped_column("ubicacion", String(60), nullable=False)
    status: Mapped[str] = mapped_column("estado", String(15), nullable=False)
    registered_by: Mapped[str] = mapped_column(
        "usuarioRegistro", String(50), nullable=False
    )
    attended_at: Mapped[datetime | None] = mapped_column(
        "fechaAtencion", DateTime, nullable=True
    )
    attention_note: Mapped[str | None] = mapped_column(
        "observacionAtencion", String(250), nullable=True
    )
    is_deleted: Mapped[bool] = mapped_column(
        "eliminado", Boolean, nullable=False, default=False, server_default=false()
    )
    updated_at: Mapped[datetime] = mapped_column(
        "fechaActualizacion",
        DateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
