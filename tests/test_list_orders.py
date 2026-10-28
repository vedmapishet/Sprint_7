"""Тесты на получение списка заказов."""

import allure

from constant import BASE_URL, ENDPOINTS, REQUEST_TIMEOUT
from helpers import _get_session


class TestGetAllOrders:

    @allure.title("GET /api/v1/orders — Получение списка всех заказов")
    def test_get_all_orders(self):
        """GET /api/v1/orders может быть долгим — увеличен timeout до 30 сек."""
        url = f"{BASE_URL}{ENDPOINTS['orders']}"
        session = _get_session()
        try:
            response = session.get(url, timeout=30)
            assert response.status_code == 200
            result = response.json()
            # Проверка: поле 'orders' существует и является непустым списком
            assert isinstance(result["orders"], list)
            assert len(result["orders"]) > 0
            # Проверка: каждый элемент — словарь
            assert isinstance(result["orders"][0], dict)
        finally:
            session.close()
