"""Конфигурация pytest-фикстур для проекта."""

import pytest
from faker import Faker

from helpers import (
    register_new_courier,
    create_courier,
    login_courier,
    create_order,
    get_order_id_by_track,
    delete_courier,
)
from data import TestData, OrderData, ExpectedResponses


@pytest.fixture
def fake():
    """Вспомогательная фигура для генерации случайных данных."""
    return Faker()


@pytest.fixture
def courier_credentials():
    """Генерирует уникальные учётные данные нового курьера (без регистрации)."""
    return register_new_courier()


@pytest.fixture
def courier_registered_and_logged():
    """
    Регистрирует курьера через API, входит в систему и возвращает
    {login, password, id}. После теста курьер удаляется.
    """
    creds = register_new_courier()
    create_courier(creds)
    courier_id = login_courier(creds["login"], creds["password"])
    result = {**creds, "id": courier_id}
    yield result

    # Очистка
    try:
        delete_courier(courier_id)
    except Exception:
        pass


@pytest.fixture
def registered_courier_id():
    """
    Регистрирует нового курьера, входит в систему и возвращает id.
    После теста курьер удаляется через API.
    """
    creds = register_new_courier()
    # Регистрация через API
    create_courier(creds)
    # Вход и получение id
    courier_id = login_courier(creds["login"], creds["password"])

    yield courier_id

    # Очистка: удаляем созданного курьера
    try:
        delete_courier(courier_id)
    except Exception:
        pass  # Курьер мог быть уже удалён другим тестом


@pytest.fixture
def created_order_track():
    """
    Создаёт заказ через API и возвращает track-номер.
    После теста заказ не удаляется (заказы — неизменяемые сущности).
    """
    track = create_order()
    yield track
    # Заказы не удаляются — это корректное поведение


@pytest.fixture
def order_with_id(created_order_track):
    """
    Возвращает кортеж (order_id, track) для созданного заказа.
    """
    order_id = get_order_id_by_track(created_order_track)
    return order_id, created_order_track


@pytest.fixture
def courier_and_order():
    """
    Регистрирует курьера, создаёт уникальный заказ и возвращает
    (courier_id, order_id). После теста курьер удаляется.
    """
    from faker import Faker
    fake = Faker()

    # Уникальные данные курьера
    creds = {
        "login": fake.user_name(),
        "password": fake.password(),
        "name": fake.name()
    }
    create_courier(creds)
    courier_id = login_courier(creds["login"], creds["password"])

    # Уникальные данные заказа (база из OrderData + уникальные имена)
    order_data = {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": f"{fake.city()}, {fake.street_name()} {fake.building_number()}",
        "metroStation": 4,
        "phone": "+7 800 555 55 50",
        "rentTime": fake.random_int(min=1, max=12),
        "deliveryDate": "2025-12-31",
        "comment": fake.sentence(),
        "color": ["BLACK"]
    }
    track = create_order(order_data)
    # API /api/v1/orders/accept/{id} ожидает order id, а не track
    order_id = get_order_id_by_track(track)

    yield courier_id, order_id

    # Очистка
    try:
        delete_courier(courier_id)
    except Exception:
        pass
