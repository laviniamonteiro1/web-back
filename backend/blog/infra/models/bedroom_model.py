from sqlalchemy import Column, String, Text
from blog.infra.database import Base


class BedroomModel(Base):
    __tablename__ = "bedrooms"

    id = Column(String, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(String(50), nullable=False) 
    image = Column(String(500), nullable=False)