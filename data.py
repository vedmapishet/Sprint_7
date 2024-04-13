from datetime import datetime
from faker import Faker
import requests

headers = {"Content-Type": "application/json"}
data_add_color = {
        "firstName": "Two",
        "lastName": "One",
        "address": "Moskow, Arbat 23",
        "metroStation": 4,
        "phone": "+7 800 555 55 50",
        "rentTime": 5,
        "deliveryDate": "2024-05-05",
        "comment": "Two color",
        "color": [
            "BLACK",
            "GREY"
        ]
    }


def login_courier():
    fake = Faker()
    login = fake.user_name()
    password = fake.password()
    firstName = fake.name()
    log_data = {}
    payload = {
        "login": login,
        "password": password,
        "firstName": firstName
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:  # если регистрация прошла успешно (код ответа 201)
        log_data = {"login": login, "password": password}


    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', headers=headers,
                             json=log_data)
    id_courier = response.json()['id']

    return id_courier

def creat_track_order(data):
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', headers=headers, json=data)
    tr = response.json()['track']
    response = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t={tr}', headers=headers)
    id = response.json()['order']['id']
    return id






class DataTest:
    data_200 = {
    "id": "253230"
    }

    data_201 = {
        "login": f'tree+{datetime.now().strftime("%m%d%Y%H%M%S")}',
        "password": "1234",
        "firstName": "tree"
    }

    data_409 = {
        "login": "ttest",
        "password": "1234",
        "firstName": "test"
    }

    data_404 = {
    "id": "3"
    }

    data_400 = {
        "login": "",
        "password": "",
        "firstName": ""
    }

    data_not_login = {
        "login": "",
        "password": "1234"
    }

    data_fail_login_and_password = {
        "login": " ",
        "password": " "
    }

    data_not_correct = {
        "login": "",
        "password": ""
    }

    data_not_log = {
        "password": "1234"
    }

    data_for_order = {
        "firstName": "One",
        "lastName": "Two",
        "address": "Moskow, Arbat 23",
        "metroStation": 4,
        "phone": "+7 800 555 55 50",
        "rentTime": 6,
        "deliveryDate": "2024-05-05",
        "comment": "One color",
        "color": [
            "BLACK"
        ]
    }

    data_add_color = {
        "firstName": "Two",
        "lastName": "One",
        "address": "Moskow, Arbat 23",
        "metroStation": 4,
        "phone": "+7 800 555 55 50",
        "rentTime": 5,
        "deliveryDate": "2024-05-05",
        "comment": "Two color",
        "color": [
            "BLACK",
            "GREY"
        ]
    }

    data_not_color = {
        "firstName": "Four",
        "lastName": "Five",
        "address": "Moskow, Arbat 24",
        "metroStation": 4,
        "phone": "+7 800 555 55 50",
        "rentTime": 5,
        "deliveryDate": "2024-05-05",
        "comment": "Not solor"
    }
    data_courier = 3333

    data_login = {
        "login": "ninja11a",
        "password": "1234"
    }

    data_not_delivery = {
        "firstName": "Why",
        "lastName": "eto",
        "address": "Moskow, Arbat 25",
        "metroStation": 4,
        "phone": "+7 800 555 55 50",
        "rentTime": 5,
        "deliveryDate": "",
        "comment": "not delivery",
        "color": [
            "BLACK"
        ]
    }

    def reg_courier():
        fake = Faker()
        login = fake.user_name()
        password = fake.password()
        firstName = fake.name()
        log_courier = {}
        payload = {
            "login": login,
            "password": password,
            "firstName": firstName
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        if response.status_code == 201:  # если регистрация прошла успешно (код ответа 201)
            log_courier = {"login": login, "password": password}
        return log_courier


class Courier:
    def register_new_courier():
        fake = Faker()
        login = fake.user_name()
        password = fake.password()
        firstName = fake.name()
        reg_data = {
            "login": login,
            "password": password,
            "name": firstName
        }
        return reg_data
class ResponsBody:
    respons_body = {"ok": True}
    respons_body_409 = {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
    respons_body_400 = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
    respons_body_404 = {"code": 404, "message": "Курьера с таким id нет."}