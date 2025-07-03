from pydantic import BaseModel, Field, HttpUrl
from typing import Optional


class CreateBedroomInput(BaseModel):
    id: str = Field(..., description="ID único do quarto")
    title: str = Field(..., min_length=3, max_length=255, description="Título ou nome do quarto (ex: 'Suíte Luxo')")
    description: str = Field(..., min_length=10, description="Descrição detalhada do quarto")
    price: str = Field(..., description="Preço do quarto (formato livre, ex: 'R$ 150,00/noite', 'USD 75')")
    image: HttpUrl = Field(..., description="URL da imagem principal do quarto")


class UpdateBedroomInput(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=255, description="Novo título do quarto")
    description: Optional[str] = Field(None, min_length=10, description="Nova descrição do quarto")
    price: Optional[str] = Field(None, description="Novo preço do quarto")
    image: Optional[HttpUrl] = Field(None, description="Nova URL da imagem do quarto")


class BedroomOutput(BaseModel):
    id: str = Field(..., description="ID único do quarto")
    title: str = Field(..., description="Título do quarto")
    description: str = Field(..., description="Descrição do quarto")
    price: str = Field(..., description="Preço do quarto")
    image: HttpUrl = Field(..., description="URL da imagem principal do quarto")

    class Config:
        from_attributes = True

    @classmethod
    def from_entity(cls, bedroom):
        return cls(
            id=bedroom.id,
            title=bedroom.title,
            description=bedroom.description,
            price=bedroom.price,
            image=bedroom.image,
        )