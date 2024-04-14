import allure
import pytest
import requests

from data import DataTest
from constant import Constants
from helpers import register_new_courier as reg_courier
from data import ResponsBody



class TestCreateCourier:
    data = reg_courier()

    @allure.title('POST запрос - Успешное создание учетной записи')
    @pytest.mark.parametrize(("data", "status_code", "json"), [
        (
                pytest.param(data, 201, ResponsBody.respons_body)
        )
    ])
    def test_create_courier(self, data, status_code, json):
        response = requests.post(Constants.url + Constants.creat_courier, headers = Constants.headers, json = data)
        assert response.status_code == status_code
        assert response.json() == json

    @allure.title('POST запрос - Тестирование заполнения всех полей и создание пользователя с логином, который уже зарегистрирован')
    @pytest.mark.parametrize(("data", "status_code", "json"), [
        (
                pytest.param(DataTest.data_409, 409,
                             ResponsBody.respons_body_409)
        ),
        (
                pytest.param(DataTest.data_400, 400,
                             ResponsBody.respons_body_400)
        )
    ])
    def test_create_courier_fail(self, data, status_code, json):
        response = requests.post(Constants.url + Constants.creat_courier, headers = Constants.headers, json = data)
        assert response.status_code == status_code
        assert response.json() == json