class DataTest:

    data_409 = {
        "login": "ttest",
        "password": "1234",
        "firstName": "test"
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


class ResponsBody:
    respons_body = {"ok": True}
    respons_body_409 = {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
    respons_body_400 = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
    respons_body_404 = {"code": 404, "message": "Курьера с таким id нет."}
    respons_body_500 = {"code":500,"message":"invalid input syntax for type integer: \":id\""}