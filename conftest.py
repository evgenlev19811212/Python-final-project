import pytest
from page.API_YouGile import apiYouGile


@pytest.fixture(scope="session")
def API_key() -> str:
    """
    Получает ключ авторизации для использования его
    в течение всей тестовой сессии.

    :return API_key: str - ключ авторизации
    """
    api = apiYouGile()
    IdCompany = api.get_companies()
    API_key = api.get_keys(IdCompany)
    return API_key
