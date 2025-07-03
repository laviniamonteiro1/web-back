from sqlalchemy import Column, String, DateTime
from blog.infra.database import Base
from datetime import datetime


class ReservationModel(Base):
    __tablename__ = "reservations"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    title = Column(String(255), nullable=False)
    address = Column(String(500), nullable=False)
    check_in = Column(DateTime, nullable=False)
    check_out = Column(DateTime, nullable=False)
    status = Column(String(50), nullable=False, default="Confirmada")