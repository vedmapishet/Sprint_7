"""Тесты на создание заказов."""

import allure

from data import OrderData, ExpectedResponses
from constant import BASE_URL, ENDPOINTS, REQUEST_TIMEOUT
from helpers import _get_session


class TestCreateOrder:

    @allure.title("POST /api/v1/orders — Создание заказа с одним цветом")
    def test_create_order_single_color(self):
        url = f"{BASE_URL}{ENDPOINTS['orders']}"
        session = _get_session()
        try:
            response = session.post(
                url, json=OrderData.single_order, timeout=REQUEST_TIMEOUT
            )
            assert response.status_code == 201
            assert "track" in response.json()
        finally:
            session.close()

    @allure.title("POST /api/v1/orders — Создание заказа с несколькими цветами")
    def test_create_order_multi_color(self):
        url = f"{BASE_URL}{ENDPOINTS['orders']}"
        session = _get_session()
        try:
            response = session.post(
                url, json=OrderData.multi_color_order, timeout=REQUEST_TIMEOUT
            )
            assert response.status_code == 201
            assert "track" in response.json()
        finally:
            session.close()

    @allure.title("POST /api/v1/orders — Создание заказа без указания цвета")
    def test_create_order_no_color(self):
        url = f"{BASE_URL}{ENDPOINTS['orders']}"
        session = _get_session()
        try:
            response = session.post(
                url, json=OrderData.no_color_order, timeout=REQUEST_TIMEOUT
            )
            assert response.status_code == 201
            assert "track" in response.json()
        finally:
            session.close()
