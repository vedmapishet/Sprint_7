"""Утилиты для работы с API и генерации тестовых данных."""

import allure
import requests
from faker import Faker

from constant import BASE_URL, ENDPOINTS, REQUEST_TIMEOUT
from data import OrderData, TestData


def _get_session() -> requests.Session:
    """Создаёт новую сессию с правильными заголовками."""
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    return session


@allure.step("Регистрация курьера и получение учётных данных")
def register_new_courier() -> dict:
    """Генерирует уникальные учётные данные для нового курьера."""
    fake = Faker()
    return {
        "login": fake.user_name(),
        "password": fake.password(),
        "name": fake.name()
    }


@allure.step("Регистрация курьера через API")
def create_courier(payload: dict) -> requests.Response:
    """Регистрирует курьера на API и возвращает ответ."""
    url = f"{BASE_URL}{ENDPOINTS['create_courier']}"
    session = _get_session()
    try:
        response = session.post(url, json=payload, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response
    finally:
        session.close()


@allure.step("Вход курьера в систему, возврат id и учётных данных")
def login_courier(login: str, password: str) -> int:
    """
    Выполняет вход курьера по login/password и возвращает его id.

    Raises:
        RuntimeError: если вход не выполнен успешно.
    """
    url = f"{BASE_URL}{ENDPOINTS['login_courier']}"
    session = _get_session()
    try:
        auth_payload = {"login": login, "password": password}
        response = session.post(url, json=auth_payload, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()

        data = response.json()
        courier_id = data.get("id")
        if courier_id is None:
            raise RuntimeError(
                f"Ожидался 'id' в ответе входа, получен: {data}"
            )
        return courier_id
    finally:
        session.close()


@allure.step("Создание заказа, возврат track-номера")
def create_order(data: dict | None = None) -> str:
    """
    Создаёт заказ через API и возвращает track-номер.

    Args:
        data: данные заказа; по умолчанию используются данные из OrderData.single_order.

    Raises:
        RuntimeError: если заказ не создан.
    """
    if data is None:
        data = OrderData.single_order

    url = f"{BASE_URL}{ENDPOINTS['orders']}"
    session = _get_session()
    try:
        response = session.post(url, json=data, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()

        track = response.json().get("track")
        if track is None:
            raise RuntimeError(
                f"Ожидался 'track' в ответе создания заказа, получен: {response.json()}"
            )
        return track
    finally:
        session.close()


@allure.step("Получение order id по track-номеру")
def get_order_id_by_track(track: str) -> int:
    """
    Запрашивает статус заказа по track-номеру и возвращает order id.

    Raises:
        RuntimeError: если ответ не содержит order.id.
    """
    url = f"{BASE_URL}{ENDPOINTS['track_order']}"
    session = _get_session()
    try:
        response = session.get(url, params={"t": track}, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()

        order_data = response.json().get("order", {})
        order_id = order_data.get("id")
        if order_id is None:
            raise RuntimeError(
                f"Ожидался 'order.id' в ответе трекинга, получен: {response.json()}"
            )
        return order_id
    finally:
        session.close()


@allure.step("Принятие заказа курьером")
def accept_order(track: str, courier_id: int) -> requests.Response:
    """
    Принимает заказ курьером по track-номеру.

    Raises:
        RuntimeError: если ответ не содержит ожидаемого поля.
    """
    url = f"{BASE_URL}{ENDPOINTS['take_order']}{track}"
    params = {"courierId": courier_id}
    session = _get_session()
    try:
        response = session.put(url, params=params, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response
    finally:
        session.close()


@allure.step("Удаление курьера по id")
def delete_courier(courier_id: int) -> requests.Response:
    """
    Удаляет курьера по id.

    Raises:
        RuntimeError: если удаление не выполнено.
    """
    url = f"{BASE_URL}{ENDPOINTS['create_courier']}/{courier_id}"
    session = _get_session()
    try:
        response = session.delete(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response
    finally:
        session.close()
