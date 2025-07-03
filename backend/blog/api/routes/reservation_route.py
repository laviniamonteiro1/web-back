from fastapi import APIRouter, HTTPException, Depends
from blog.api.deps import reservation_repo
from blog.usecases.reservation.create_reservation import CreateReservationUseCase
from blog.usecases.reservation.list_reservation import ListUserReservationsUseCase
from blog.usecases.reservation.update_reservation import UpdateReservationUseCase
from blog.usecases.reservation.delete_reservation import DeleteReservationUseCase
from blog.usecases.reservation.cancel_reservation import CancelReservationUseCase
from blog.usecases.reservation.get_user_reservation_by_id import GetUserReservationByIdUseCase


from blog.domain.entities.reservation import Reservation
import uuid
from datetime import datetime

from blog.api.schemas.reservation_schema import (
    CreateReservationInput,
    UpdateReservationInput,
    ReservationOutput,
)

router = APIRouter()


@router.post(
    "/users/{user_id}/reservations",
    response_model=ReservationOutput,
    summary="Criar nova reserva para um usuário",
    description="Cria uma nova reserva para um usuário específico.",
)
def create_reservation(user_id: str, data: CreateReservationInput):
    try:
        reservation_data_dict = data.model_dump()
        reservation_data_dict["id"] = str(uuid.uuid4())
        
        usecase = CreateReservationUseCase(reservation_repo)
        result = usecase.execute(user_id=user_id, reservation_data=reservation_data_dict)
        return ReservationOutput.from_entity(result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {str(e)}")


@router.get(
    "/users/{user_id}/reservations",
    response_model=list[ReservationOutput],
    summary="Listar todas as reservas de um usuário",
    description="Retorna uma lista de todas as reservas de um usuário específico.",
)
def list_user_reservations(user_id: str):
    try:
        usecase = ListUserReservationsUseCase(reservation_repo)
        results = usecase.execute(user_id)
        return [ReservationOutput.from_entity(res) for res in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {str(e)}")


@router.get(
    "/users/{user_id}/reservations/{reservation_id}",
    response_model=ReservationOutput,
    summary="Obter reserva específica de um usuário",
    description="Retorna os detalhes de uma reserva específica de um usuário pelo seu ID.",
)
def get_user_reservation_by_id(user_id: str, reservation_id: str):
    try:
        usecase = GetUserReservationByIdUseCase(reservation_repo)
        result = usecase.execute(user_id=user_id, reservation_id=reservation_id)
        if result is None:
            raise HTTPException(status_code=404, detail="Reserva não encontrada para este usuário.")
        return ReservationOutput.from_entity(result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {str(e)}")


@router.put(
    "/users/{user_id}/reservations/{reservation_id}",
    response_model=ReservationOutput,
    summary="Atualizar reserva de um usuário",
    description="Atualiza uma reserva específica de um usuário pelo seu ID com os dados fornecidos.",
)
def update_reservation(user_id: str, reservation_id: str, data: UpdateReservationInput):
    try:
        reservation_data_dict = data.model_dump(exclude_unset=True)
        reservation_data_dict["id"] = reservation_id
        
        usecase = UpdateReservationUseCase(reservation_repo)
        result = usecase.execute(user_id=user_id, reservation_data=reservation_data_dict)
        
        return ReservationOutput.from_entity(result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {str(e)}")


@router.delete(
    "/users/{user_id}/reservations/{reservation_id}",
    summary="Deletar reserva de um usuário",
    description="Deleta uma reserva específica de um usuário pelo seu ID.",
    status_code=204,
)
def delete_reservation(user_id: str, reservation_id: str):
    try:
        usecase = DeleteReservationUseCase(reservation_repo)
        usecase.execute(user_id=user_id, reservation_id=reservation_id)
        return {"message": "Reserva deletada com sucesso."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {str(e)}")


@router.post(
    "/users/{user_id}/reservations/{reservation_id}/cancel",
    response_model=ReservationOutput,
    summary="Cancelar reserva de um usuário",
    description="Cancela uma reserva específica de um usuário pelo seu ID.",
)
def cancel_reservation(user_id: str, reservation_id: str):
    try:
        usecase = CancelReservationUseCase(reservation_repo)
        result = usecase.execute(user_id=user_id, reservation_id=reservation_id)
        return ReservationOutput.from_entity(result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {str(e)}")