import allure
import pytest
import requests

from data import login_courier as log
from constant import Constants
from data import ResponsBody

class TestDelCourier:
    id_courier = log()
    @allure.title('DELETE запрос - Успешное удаление учетной записи')
    @allure.step("Отправка DELETE запроса с заголовком и данными созданного ранее курьера")
    @pytest.mark.parametrize(("id_courier", "status_code", "json"), [
        (
                pytest.param(id_courier, 200, ResponsBody.respons_body)
        )
    ])
    def test_delete_courier(self, id_courier, status_code, json):
        id = f"{id_courier}"
        response_delete = requests.delete(f"{Constants.url}/api/v1/courier/{id_courier}", data = {'id': {id}})

        # проверим, что удаление выполнено успешно
        assert response_delete.status_code == 200
        assert response_delete.json() == json

    @allure.title('DELETE запрос - запрос с несуществующим id')
    @allure.step("Отправка DELETE запрос с несуществующим id")
    @pytest.mark.parametrize(("id_courier", "status_code", "json"), [
        (
                pytest.param(id_courier, 404, ResponsBody.respons_body_404)
        )
    ])
    def test_delete_courier_fail(self, id_courier, status_code, json):
        id = f"{id_courier}"
        response_delete = requests.delete(f"{Constants.url}/api/v1/courier/{id_courier}", data={'id': {id}})

        # проверим, что удаление выполнено успешно
        assert response_delete.status_code == status_code
        assert response_delete.json() == json

    @allure.title('DELETE запрос - запрос без id')
    @allure.step("Отправка DELETE запрос без id")
    @pytest.mark.parametrize(("id_courier", "status_code"), [
    (
        pytest.param(id_courier, 500)
    )
    ])

    def test_delete_courier_fail_2(self, id_courier, status_code):
        id = f"{id_courier}"
        response_delete = requests.delete(f"{Constants.url}/api/v1/courier/:id", data={'id': {id}})

        # проверим, что удаление выполнено успешно
        assert response_delete.status_code == status_code