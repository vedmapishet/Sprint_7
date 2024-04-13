import allure
import pytest
import requests

from constant import Constants
from data import DataTest


class TestCreateOrder:

    @allure.title('POST запрос - Создание заказа')
    @allure.description(
        "Тестируем заполнение параметра color, а также"
        "наличие слова track в теле ответа")
    @allure.step("Отправка POST запроса с набором тестовых данных для создания заказа (можно выбрать один цвет, оба цвета и оставить пустым)")
    @pytest.mark.parametrize(("data", "status_code"), [
        (
                pytest.param(DataTest.data_for_order, 201)
        ),
        (
                pytest.param(DataTest.data_add_color, 201)
        ),
        (
                pytest.param(DataTest.data_not_color, 201)
        )
    ])
    def test_create_courier(self, data, status_code):
        response = requests.post(Constants.url + Constants.created_orders, headers = Constants.headers, json = data)
        assert response.status_code == status_code
        assert 'track' in response.json()