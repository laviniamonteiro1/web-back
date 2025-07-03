import pytest
from blog.domain.entities.user import User
from blog.domain.entities.reservation import Reservation
from blog.domain.entities.bedroom import Bedroom
from blog.domain.value_objects.email_vo import Email
from blog.domain.value_objects.password import Password
from datetime import datetime

def test_create_user():
    email = Email("user@example.com")
    pwd = Password("Secret123")
    user = User("1", "User", email, pwd, "user")
    assert user.name == "User"
    assert user.email.value() == "user@example.com"

def test_invalid_role():
    with pytest.raises(ValueError):
        User("1", "User", Email("user@example.com"), Password("Secret123"), "invalid")

def test_create_reservation():
    reservation = Reservation(
        id="1",
        user_id="1",
        title="Suíte Luxo",
        address="Rua Exemplo, 123",
        check_in="10/09/2025 às 14h00",
        check_out="15/09/2025 às 12h00",
        status="Confirmada"
    )
    assert reservation.title == "Suíte Luxo"
    assert reservation.status == "Confirmada"

def test_cancel_reservation():
    reservation = Reservation(
        id="1",
        user_id="1",
        title="Suíte Luxo",
        address="Rua Exemplo, 123",
        check_in="10/09/2025 às 14h00",
        check_out="15/09/2025 às 12h00",
        status="Confirmada"
    )
    reservation.cancel_reservation()
    assert reservation.status == "Cancelada"

def test_update_reservation_status():
    reservation = Reservation(
        id="1",
        user_id="1",
        title="Suíte Luxo",
        address="Rua Exemplo, 123",
        check_in="10/09/2025 às 14h00",
        check_out="15/09/2025 às 12h00",
        status="Confirmada"
    )
    reservation.update_reservation(new_status="Finalizada")
    assert reservation.status == "Finalizada"

def test_create_bedroom():
    bedroom = Bedroom("1", "Suíte Luxo", "Quarto com cama king size e vista para o mar.", "R$ 500,00", "quarto1.png")
    assert bedroom.title == "Suíte Luxo"
    assert bedroom.price == "R$ 500,00"
    assert bedroom.image == "quarto1.png"
