"""Тесты на создание курьера."""

import allure

from data import TestData, ExpectedResponses
from constant import BASE_URL, ENDPOINTS, REQUEST_TIMEOUT
from helpers import _get_session, register_new_courier


class TestCreateCourier:

    @allure.title("POST /api/v1/courier — Успешное создание учетной записи")
    def test_create_courier_success(self):
        """Создаём курьера с уникальными данными из register_new_courier()."""
        url = f"{BASE_URL}{ENDPOINTS['create_courier']}"
        creds = register_new_courier()
        session = _get_session()
        try:
            response = session.post(url, json=creds, timeout=REQUEST_TIMEOUT)
            assert response.status_code == 201
            assert response.json() == ExpectedResponses.success_created
        finally:
            session.close()

    @allure.title("POST /api/v1/courier — Дублирование логина (409)")
    def test_create_courier_duplicate_login(self):
        url = f"{BASE_URL}{ENDPOINTS['create_courier']}"
        session = _get_session()
        try:
            response = session.post(url, json=TestData.duplicate_login_data, timeout=REQUEST_TIMEOUT)
            assert response.status_code == 409
            assert response.json() == ExpectedResponses.error_409_duplicate_login
        finally:
            session.close()

    @allure.title("POST /api/v1/courier — Пустые обязательные поля (400)")
    def test_create_courier_empty_fields(self):
        url = f"{BASE_URL}{ENDPOINTS['create_courier']}"
        session = _get_session()
        try:
            response = session.post(url, json=TestData.empty_fields_data, timeout=REQUEST_TIMEOUT)
            assert response.status_code == 400
            assert response.json() == ExpectedResponses.error_400_insufficient_data
        finally:
            session.close()
