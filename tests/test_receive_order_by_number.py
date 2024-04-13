import allure
import pytest
import requests

from constant import Constants


class TestReceiveOrder:

    @allure.title('GET запрос - Успешное получение заказа по его номеру')
    @allure.step("Отправка GET запроса с заголовком")
    def test_receive_order(self):
        response = requests.get(f'{Constants.url}{Constants.track}779220', headers = Constants.headers)
        assert response.status_code == 200

    @allure.title('GET запрос - Запрос без номера')
    @allure.step("Отправка GET без номера")
    def test_receive_order_without_number(self):
        response = requests.get(f'{Constants.url}{Constants.track}', headers=Constants.headers)
        assert response.status_code == 400

    @allure.title('GET запрос - Запрос с несуществующим номером заказа')
    @allure.step("Отправка GET с невалидным номером заказа")
    def test_receive_order_with_non_existent_number(self):
        response = requests.get(f'{Constants.url}{Constants.track}77920', headers=Constants.headers)
        assert response.status_code == 404