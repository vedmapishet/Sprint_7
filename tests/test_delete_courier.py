"""Тесты на удаление курьера."""

import allure

from data import ExpectedResponses
from constant import BASE_URL, ENDPOINTS, REQUEST_TIMEOUT
from helpers import _get_session


class TestDeleteCourier:

    @allure.title("DELETE /api/v1/courier/{id} — Успешное удаление")
    def test_delete_courier_success(self, registered_courier_id):
        courier_id = registered_courier_id
        url = f"{BASE_URL}{ENDPOINTS['create_courier']}/{courier_id}"
        session = _get_session()
        try:
            response = session.delete(url, timeout=REQUEST_TIMEOUT)
            assert response.status_code == 200
            assert response.json() == ExpectedResponses.success_created
        finally:
            session.close()

    @allure.title("DELETE /api/v1/courier/{id} — Удаление несуществующего курьера (404)")
    def test_delete_nonexistent_courier(self):
        """Попытка удалить курьера с заведомо несуществующим ID."""
        fake_id = 999999
        url = f"{BASE_URL}{ENDPOINTS['create_courier']}/{fake_id}"
        session = _get_session()
        try:
            response = session.delete(url, timeout=REQUEST_TIMEOUT)
            assert response.status_code == 404
            assert response.json() == ExpectedResponses.error_404_courier_not_found
        finally:
            session.close()
