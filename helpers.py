import allure
from faker import Faker
import requests
from constant import Constants

@allure.step("Получение id курьера")
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

    response = requests.post(Constants.url + Constants.creat_courier, data=payload)

    if response.status_code == 201:  # если регистрация прошла успешно (код ответа 201)
        log_data = {"login": login, "password": password}


    response = requests.post(Constants.url + Constants.login_courier, headers=Constants.headers,
                             json=log_data)
    id_courier = response.json()['id']

    return id_courier

@allure.step("Получение id заказа")
def creat_track_order(data):
    response = requests.post(f'{Constants.url}{Constants.created_orders}', headers=Constants.headers, json=data)
    tr = response.json()['track']
    response = requests.get(f'{Constants.url}{Constants.track}{tr}', headers=Constants.headers)
    id = response.json()['order']['id']
    return id

@allure.step("Регистрация курьера и получение его логина и пароля")
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

    response = requests.post(f'{Constants.url}{Constants.creat_courier}', data=payload)

    if response.status_code == 201:  # если регистрация прошла успешно (код ответа 201)
        log_courier = {"login": login, "password": password}
    return log_courier

@allure.step("Регистрация курьера")
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