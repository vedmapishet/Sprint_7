"""Тестовые данные для автотестов."""


class TestData:
    """Тестовые данные для создания курьера."""

    # Данные для тестирования дублирования логина (ожидаемый статус 409)
    duplicate_login_data = {
        "login": "test_duplicate",
        "password": "1234",
        "firstName": "test"
    }

    # Данные с пустыми обязательными полями (ожидаемый статус 400)
    empty_fields_data = {
        "login": "",
        "password": "",
        "firstName": ""
    }

    # Данные для тестирования входа: отсутствует login
    missing_login_field = {
        "login": "",
        "password": "1234"
    }

    # Данные для тестирования входа: пробелы вместо login и password
    whitespace_credentials = {
        "login": " ",
        "password": " "
    }

    # Данные для тестирования входа: полностью пустые поля
    empty_credentials = {
        "login": "",
        "password": ""
    }

    # Данные для тестирования входа: отсутствует login
    missing_login_for_auth = {
        "password": "1234"
    }


class OrderData:
    """Тестовые данные для создания заказов."""

    single_order = {
        "firstName": "One",
        "lastName": "Two",
        "address": "Moscow, Arbat 23",
        "metroStation": 4,
        "phone": "+7 800 555 55 50",
        "rentTime": 6,
        "deliveryDate": "2024-05-05",
        "comment": "One color",
        "color": ["BLACK"]
    }

    multi_color_order = {
        "firstName": "Two",
        "lastName": "One",
        "address": "Moscow, Arbat 23",
        "metroStation": 4,
        "phone": "+7 800 555 55 50",
        "rentTime": 5,
        "deliveryDate": "2024-05-05",
        "comment": "Two color",
        "color": ["BLACK", "GREY"]
    }

    no_color_order = {
        "firstName": "Four",
        "lastName": "Five",
        "address": "Moscow, Arbat 24",
        "metroStation": 4,
        "phone": "+7 800 555 55 50",
        "rentTime": 5,
        "deliveryDate": "2024-05-05",
        "comment": "No color"
    }


class ExpectedResponses:
    """Ожидаемые тела ответов от API."""

    success_created = {"ok": True}

    error_409_duplicate_login = {
        "code": 409,
        "message": "Этот логин уже используется. Попробуйте другой."
    }

    error_400_insufficient_data = {
        "code": 400,
        "message": "Недостаточно данных для создания учетной записи"
    }

    error_404_courier_not_found = {
        "code": 404,
        "message": "Курьера с таким id нет."
    }

    error_500_invalid_input = {
        "code": 500,
        "message": "invalid input syntax for type integer: \":id\""
    }

    error_400_login_insufficient_data = {
        "code": 400,
        "message": "Недостаточно данных для входа"
    }

    error_404_account_not_found = {
        "code": 404,
        "message": "Учетная запись не найдена"
    }

    error_404_courier_does_not_exist = {
        "code": 404,
        "message": "Курьера с таким id не существует"
    }

    error_404_order_not_found = {
        "code": 404,
        "message": "Заказа с таким id не существует"
    }

    error_409_order_already_in_progress = {
        "code": 409,
        "message": "Этот заказ уже в работе"
    }

    error_400_insufficient_search_data = {
        "code": 400,
        "message": "Недостаточно данных для поиска"
    }
