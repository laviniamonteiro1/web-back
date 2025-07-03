from fastapi import APIRouter, HTTPException
from blog.api.deps import bedroom_repo
from blog.usecases.bedroom.list_bedroom import ListBedroomsUseCase
from blog.usecases.bedroom.get_bedroomById import GetBedroomByIdUseCase 

from blog.api.schemas.bedroom_schema import BedroomOutput
from typing import List

router = APIRouter()


@router.get(
    "/",
    response_model=List[BedroomOutput],
    summary="Listar todos os quartos",
    description="Retorna uma lista de todos os quartos disponíveis.",
)
def list_bedrooms():
    try:
        usecase = ListBedroomsUseCase(bedroom_repo)
        results = usecase.execute()
        return [BedroomOutput.from_entity(bedroom) for bedroom in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {str(e)}")


@router.get(
    "/{bedroom_id}",
    response_model=BedroomOutput,
    summary="Obter quarto por ID",
    description="Retorna os detalhes de um quarto específico pelo seu ID.",
)
def get_bedroom_by_id(bedroom_id: str):
    try:
        usecase = GetBedroomByIdUseCase(bedroom_repo)
        result = usecase.execute(bedroom_id)
        if result is None:
            raise HTTPException(status_code=404, detail="Quarto não encontrado.")
        return BedroomOutput.from_entity(result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {str(e)}")