import allure
import pytest
import requests

from constant import Constants
from data import ResponsBody
from data import DataTest
from data import creat_track_order as tr
from data import login_courier as log


class TestTakeOrder:
    id_courier = log()

    track = tr(DataTest.data_add_color)

    @allure.title('PUT запрос - Заказ успешно принят курьером')
    @allure.step("Отправка PUT запроса с заголовком, track, id_courier")
    @pytest.mark.parametrize(("id_courier", "status_code", "track", "json"), [
        (
                pytest.param(291712, 200, track, ResponsBody.respons_body)
        )
    ])
    def test_take_order_correct(self, id_courier, status_code, track,json):
        response = requests.put(f'{Constants.url}/api/v1/orders/accept/{track}?courierId={id_courier}', headers = Constants.headers)
        assert response.status_code == status_code
        assert response.json() == json

    @allure.title('PUT запрос - Запрос вернул ошибку')
    @allure.step("Отправка PUT запроса с заголовком, и невалидными track, id_courier")
    @pytest.mark.parametrize(("id_courier", "status_code", "json", "track"), [
        (
                pytest.param('', 400, {"code": 400, "message": "Недостаточно данных для поиска"}, 777)
        ),
        (
                pytest.param(776152, 404, {"code": 404, "message": "Курьера с таким id не существует"},779)
        ),
        (
                pytest.param(DataTest.data_courier, 404, {"code": 404, "message": 'Заказа с таким id не существует'},779220)
        ),
        (
                pytest.param(DataTest.data_courier, 409, {"code": 409, "message": "Этот заказ уже в работе"},238523)
        )
    ])
    def test_take_order_error(self, id_courier, status_code, json, track):
        response = requests.put(f'{Constants.url}/api/v1/orders/accept/{track}?courierId={id_courier}',
                                headers=Constants.headers)
        assert response.status_code == status_code
        assert response.json() == json