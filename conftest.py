import pytest
from page.API_YouGile import apiYouGile
from selenium import webdriver
from page.UI_YouGile import AuthPage
import allure


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


@pytest.fixture(scope="session")
def driver():
    """
    Открывает и настраивает браузер.
    """
    with allure.step("Открыть и настроить браузер"):
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        driver.maximize_window()
        yield driver

    with allure.step("Закрыть браузер"):
        driver.quit()


@pytest.fixture(scope="session")
def auth(driver) -> None:
    """
    Осуществляет вход в профиль пользователя на
    всю тестовую сессию.
    """
    auth = AuthPage(driver)
    auth.send_login()
    auth.click_login()
