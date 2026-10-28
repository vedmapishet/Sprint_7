"""Тесты на вход курьера в систему."""

import allure

from data import TestData, ExpectedResponses
from constant import BASE_URL, ENDPOINTS, REQUEST_TIMEOUT
from helpers import _get_session


class TestLoginCourier:

    @allure.title("POST /api/v1/courier/login — Успешный вход")
    def test_login_success(self, courier_registered_and_logged):
        """Курьер уже зарегистрирован fixture'ом, входим по login/password."""
        url = f"{BASE_URL}{ENDPOINTS['login_courier']}"
        session = _get_session()
        try:
            auth_payload = {
                "login": courier_registered_and_logged["login"],
                "password": courier_registered_and_logged["password"],
            }
            response = session.post(url, json=auth_payload, timeout=REQUEST_TIMEOUT)
            assert response.status_code == 200
            assert "id" in response.json()
        finally:
            session.close()

    @allure.title("POST /api/v1/courier/login — Отсутствует login (400)")
    def test_login_missing_login_field(self):
        url = f"{BASE_URL}{ENDPOINTS['login_courier']}"
        session = _get_session()
        try:
            response = session.post(
                url, json=TestData.missing_login_field, timeout=REQUEST_TIMEOUT
            )
            assert response.status_code == 400
            assert response.json() == ExpectedResponses.error_400_login_insufficient_data
        finally:
            session.close()

    @allure.title("POST /api/v1/courier/login — Вход по пробелам (404)")
    def test_login_whitespace_credentials(self):
        url = f"{BASE_URL}{ENDPOINTS['login_courier']}"
        session = _get_session()
        try:
            response = session.post(
                url, json=TestData.whitespace_credentials, timeout=REQUEST_TIMEOUT
            )
            assert response.status_code == 404
            assert response.json() == ExpectedResponses.error_404_account_not_found
        finally:
            session.close()

    @allure.title("POST /api/v1/courier/login — Пустые учётные данные (400)")
    def test_login_empty_credentials(self):
        url = f"{BASE_URL}{ENDPOINTS['login_courier']}"
        session = _get_session()
        try:
            response = session.post(
                url, json=TestData.empty_credentials, timeout=REQUEST_TIMEOUT
            )
            assert response.status_code == 400
            assert response.json() == ExpectedResponses.error_400_login_insufficient_data
        finally:
            session.close()

    @allure.title("POST /api/v1/courier/login — Отсутствует поле login (400)")
    def test_login_missing_login_key(self):
        url = f"{BASE_URL}{ENDPOINTS['login_courier']}"
        session = _get_session()
        try:
            response = session.post(
                url, json=TestData.missing_login_for_auth, timeout=REQUEST_TIMEOUT
            )
            assert response.status_code == 400
            assert response.json() == ExpectedResponses.error_400_login_insufficient_data
        finally:
            session.close()
