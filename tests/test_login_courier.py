import allure
import pytest
import requests

from constant import Constants
from helpers import reg_courier
from data import DataTest


class TestLoginCourier:
    data_login = reg_courier()

    @allure.title('POST запрос - Логин курьера в системе. Положительный кейс')
    @pytest.mark.parametrize(("data", "status_code"), [
        (
                pytest.param(data_login, 200)
        )
    ])
    def test_login_courier_correct(self, data, status_code):
        response = requests.post(Constants.url + Constants.login_courier, headers = Constants.headers, json = data)
        assert response.status_code == status_code
        assert 'id' in response.json()


    @allure.title('POST запрос - Логин курьера в системе. Негативная проверка')
    @pytest.mark.parametrize(("data", "status_code", "json"), [
        (
                pytest.param(DataTest.data_not_login, 400,
                                 {'code': 400, 'message': 'Недостаточно данных для входа'})
        ),
        (
                pytest.param(DataTest.data_fail_login_and_password, 404,
                                 {"code": 404, "message": "Учетная запись не найдена"})
        ),
        (
                pytest.param(DataTest.data_not_correct, 400,
                                 {"code": 400, "message": "Недостаточно данных для входа"})
        ),
        (
                pytest.param(DataTest.data_not_log, 400,
                                 {"code": 400, "message": "Недостаточно данных для входа"})
        ),
    ])
    def test_login_courier_fail(self, data, status_code, json):
        response = requests.post(Constants.url + Constants.login_courier, headers = Constants.headers, json = data)
        assert response.status_code == status_code
        assert response.json() == json