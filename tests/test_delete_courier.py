import allure
import pytest
import requests

from helpers import login_courier as log
from constant import Constants
from data import ResponsBody

class TestDelCourier:
    id_courier = log()
    @allure.title('DELETE запрос - Успешное удаление учетной записи')
    @pytest.mark.parametrize(("id_courier", "status_code", "json"), [
        (
                pytest.param(id_courier, 200, ResponsBody.respons_body)
        )
    ])
    def test_delete_courier(self, id_courier, status_code, json):
        id = f"{id_courier}"
        response_delete = requests.delete(f"{Constants.url}{Constants.creat_courier}/{id_courier}", data = {'id': {id}})

        # проверим, что удаление выполнено успешно
        assert response_delete.status_code == 200
        assert response_delete.json() == json

    @allure.title('DELETE запрос - запрос с несуществующим id')
    @pytest.mark.parametrize(("id_courier", "status_code", "json"), [
        (
                pytest.param(id_courier, 404, ResponsBody.respons_body_404)
        )
    ])
    def test_delete_courier_fail(self, id_courier, status_code, json):
        id = f"{id_courier}"
        response_delete = requests.delete(f"{Constants.url}{Constants.creat_courier}/{id_courier}", data={'id': {id}})

        # проверим, что удаление выполнено успешно
        assert response_delete.status_code == status_code
        assert response_delete.json() == json

    @allure.title('DELETE запрос - запрос без id')
    @pytest.mark.parametrize(("id_courier", "status_code", "json"), [
    (
        pytest.param(id_courier, 500, ResponsBody.respons_body_500)
    )
    ])

    def test_delete_courier_fail_2(self, id_courier, status_code, json):
        id = f"{id_courier}"
        response_delete = requests.delete(f"{Constants.url}{Constants.creat_courier}/:id", data={'id': {id}})

        assert response_delete.status_code == status_code
        assert response_delete.json() == json