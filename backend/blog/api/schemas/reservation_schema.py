from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional, Literal


class CreateReservationInput(BaseModel):
    user_id: str = Field(..., description="ID do usuário que está fazendo a reserva")
    title: str = Field(..., min_length=3, max_length=255, description="Título da reserva (ex: 'Hotel Conforto', 'Consulta Dentária')")
    address: str = Field(..., min_length=10, max_length=500, description="Endereço completo do local da reserva")
    check_in: str = Field(..., description="Data e hora de check-in (formato: DD/MM/YYYY às HHhMM)")
    check_out: str = Field(..., description="Data e hora de check-out (formato: DD/MM/YYYY às HHhMM)")

    @validator('check_in', 'check_out', pre=True)
    def parse_datetime_fields(cls, v):
        try:
            return datetime.strptime(v, "%d/%m/%Y às %Hh%M")
        except ValueError:
            raise ValueError("Formato de data e hora inválido. Use 'DD/MM/YYYY às HHhMM'.")

    @validator('check_out')
    def check_out_after_check_in(cls, v, values):
        if 'check_in' in values and v <= values['check_in']:
            raise ValueError("Data de check-out deve ser posterior à data de check-in.")
        return v


class UpdateReservationInput(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=255, description="Novo título da reserva")
    address: Optional[str] = Field(None, min_length=10, max_length=500, description="Novo endereço do local da reserva")
    check_in: Optional[str] = Field(None, description="Nova data e hora de check-in (formato: DD/MM/YYYY às HHhMM)")
    check_out: Optional[str] = Field(None, description="Nova data e hora de check-out (formato: DD/MM/YYYY às HHhMM)")
    status: Optional[Literal["Confirmada", "Cancelada", "Concluída"]] = Field(
        None, description="Novo status da reserva"
    )

    @validator('check_in', 'check_out', pre=True)
    def parse_datetime_fields_optional(cls, v):
        if v is None:
            return v
        try:
            return datetime.strptime(v, "%d/%m/%Y às %Hh%M")
        except ValueError:
            raise ValueError("Formato de data e hora inválido. Use 'DD/MM/YYYY às HHhMM'.")

    @validator('check_out')
    def check_out_after_check_in_optional(cls, v, values):
        if 'check_in' in values and values['check_in'] is not None and v is not None and v <= values['check_in']:
            raise ValueError("Data de check-out deve ser posterior à data de check-in.")
        return v


class ReservationOutput(BaseModel):
    id: str = Field(..., description="ID único da reserva")
    user_id: str = Field(..., description="ID do usuário que fez a reserva")
    title: str = Field(..., description="Título da reserva")
    address: str = Field(..., description="Endereço do local da reserva")
    check_in: datetime = Field(..., description="Data e hora de check-in")
    check_out: datetime = Field(..., description="Data e hora de check-out")
    status: Literal["Confirmada", "Cancelada", "Concluída"] = Field(..., description="Status atual da reserva")

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda dt: dt.strftime("%d/%m/%Y às %Hh%M")
        }

    @classmethod
    def from_entity(cls, reservation):
        return cls(
            id=reservation.id,
            user_id=reservation.user_id,
            title=reservation.title,
            address=reservation.address,
            check_in=reservation.check_in,
            check_out=reservation.check_out,
            status=reservation.status,
        )