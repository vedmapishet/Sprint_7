"""Тесты на принятие заказа курьером."""

import allure

from data import ExpectedResponses
from constant import BASE_URL, ENDPOINTS, REQUEST_TIMEOUT
from helpers import _get_session


class TestTakeOrder:

    @allure.title("PUT /api/v1/orders/accept/{track} — Заказ успешно принят")
    def test_take_order_success(self, courier_and_order):
        """Курьер и заказ создаются уникально в одном fixture."""
        courier_id, track = courier_and_order
        url = f"{BASE_URL}{ENDPOINTS['take_order']}{track}"
        params = {"courierId": courier_id}
        session = _get_session()
        try:
            response = session.put(url, params=params, timeout=REQUEST_TIMEOUT)
            assert response.status_code == 200
            assert response.json() == ExpectedResponses.success_created
        finally:
            session.close()

    @allure.title("PUT /api/v1/orders/accept/{track} — Недостаточно данных (400)")
    def test_take_order_insufficient_data(self, created_order_track):
        """Пустой courierId должен вернуть 400."""
        url = f"{BASE_URL}{ENDPOINTS['take_order']}{created_order_track}"
        params = {"courierId": ""}
        session = _get_session()
        try:
            response = session.put(url, params=params, timeout=REQUEST_TIMEOUT)
            assert response.status_code == 400
            assert response.json() == ExpectedResponses.error_400_insufficient_search_data
        finally:
            session.close()

    @allure.title("PUT /api/v1/orders/accept/{track} — Курьер не существует (404)")
    def test_take_order_nonexistent_courier(self, created_order_track):
        url = f"{BASE_URL}{ENDPOINTS['take_order']}{created_order_track}"
        params = {"courierId": 999999}
        session = _get_session()
        try:
            response = session.put(url, params=params, timeout=REQUEST_TIMEOUT)
            assert response.status_code == 404
            assert response.json() == ExpectedResponses.error_404_courier_does_not_exist
        finally:
            session.close()

    @allure.title("PUT /api/v1/orders/accept/{track} — Заказ не найден (404)")
    def test_take_order_nonexistent_order(self, registered_courier_id):
        url = f"{BASE_URL}{ENDPOINTS['take_order']}000000"
        params = {"courierId": registered_courier_id}
        session = _get_session()
        try:
            response = session.put(url, params=params, timeout=REQUEST_TIMEOUT)
            assert response.status_code == 404
            assert response.json() == ExpectedResponses.error_404_order_not_found
        finally:
            session.close()
