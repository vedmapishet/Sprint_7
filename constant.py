"""Конфигурация API-эндпоинтов и параметры HTTP-запросов."""

# Время ожидания ответа сервера (секунды)
REQUEST_TIMEOUT = 10

# Базовый URL API
BASE_URL = "https://qa-scooter.praktikum-services.ru"

# Эндпоинты API
ENDPOINTS = {
    "orders": "/api/v1/orders",
    "login_courier": "/api/v1/courier/login",
    "create_courier": "/api/v1/courier",
    "track_order": "/api/v1/orders/track",
    "take_order": "/api/v1/orders/accept/",
}
