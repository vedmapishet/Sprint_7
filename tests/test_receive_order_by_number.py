"""Тесты на получение заказа по track-номеру."""

import allure
import pytest

from constant import BASE_URL, ENDPOINTS, REQUEST_TIMEOUT
from helpers import _get_session


class TestReceiveOrder:

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("GET /api/v1/orders/track — Успешное получение заказа по номеру")
    def test_receive_order_success(self, created_order_track):
        url = f"{BASE_URL}{ENDPOINTS['track_order']}"
        session = _get_session()
        try:
            response = session.get(
                url, params={"t": created_order_track}, timeout=REQUEST_TIMEOUT
            )
            assert response.status_code == 200
            data = response.json()
            assert "order" in data
            assert "id" in data["order"]
            assert "status" in data["order"]
        finally:
            session.close()

    @allure.title("GET /api/v1/orders/track — Запрос без номера (400)")
    def test_receive_order_without_number(self):
        url = f"{BASE_URL}{ENDPOINTS['track_order']}"
        session = _get_session()
        try:
            response = session.get(url, timeout=REQUEST_TIMEOUT)
            assert response.status_code == 400
        finally:
            session.close()

    @allure.title("GET /api/v1/orders/track — Запрос с несуществующим номером (404)")
    def test_receive_order_non_existent(self):
        url = f"{BASE_URL}{ENDPOINTS['track_order']}"
        fake_track = "000000"
        session = _get_session()
        try:
            response = session.get(
                url, params={"t": fake_track}, timeout=REQUEST_TIMEOUT
            )
            assert response.status_code == 404
        finally:
            session.close()
