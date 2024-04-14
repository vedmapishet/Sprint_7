import allure
import requests

from constant import Constants


class TestGetAllOrder:

    @allure.title('GET запрос - Успешная выгрузка всех заказов')
    def test_get_all_order(self):
        response = requests.get(Constants.url + Constants.created_orders, headers = Constants.headers)
        assert response.status_code == 200
        result = response.json()
        assert type(result['orders'][0]) == dict