from time import sleep
from page.UI_YouGile import MainPage
from page.API_YouGile import apiYouGile
import allure
import pytest


@pytest.mark.ui
@allure.title("Тестирование создания нового проекта через UI")
@allure.description("Тест проверяет корректность создания нового проекта")
@allure.feature("Работа с проектами")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_project_positive(auth, API_key, driver):
    """
    Тест проверяет корректность создания нового проекта.
    """
    api = apiYouGile()
    main = MainPage(driver)

    with allure.step("Количество проектов до начала теста"):
        project_list_before = api.get_project_list(API_key)

    with allure.step("Создание нового проекта через UI"):
        main.create_project_click()
        main.create_project_title()
        main.create_project_click_button()

    with allure.step("Название на карточке проекта"):
        project_card = main.proj_card()

    with allure.step("Количество проектов после создания"):
        project_list_after = api.get_project_list(API_key)

    with allure.step("Проверка совпадения названия на карточке с заданным"):
        assert project_card == "New Project"

    with allure.step("Количество проектов увеличилось на 1"):
        assert project_list_after - project_list_before == 1

    with allure.step("Удаление тестовых данных"):
        main.delete_project()


@pytest.mark.ui
@allure.title("Тестирование невозможности создания нового проекта с названием из пробелов") # noqa
@allure.description("Тест проверяет НЕсоздание проекта с названием из пробелов") # noqa
@allure.feature("Работа с проектами")
@allure.severity(allure.severity_level.MINOR)
def test_create_project_negative(auth, driver) -> None:
    """
    Тест проверяет НЕсоздание проекта с названием из пробелов.
    """
    main = MainPage(driver)

    with allure.step("Создание нового проекта через UI"):
        main.create_project_click()
        main.create_project_title("     ")
        main.create_project_click_button()


@pytest.mark.ui
@allure.title("Тестирование дублирования проектов")
@allure.description("Тест проверяет дублирование проектов")
@allure.feature("Работа с проектами")
@allure.severity(allure.severity_level.MINOR)
def test_double_project(auth, driver, API_key) -> None:
    """
    Тест проверяет дублирование проектов.
    """
    api = apiYouGile()
    main = MainPage(driver)

    with allure.step("Количество проектов до начала теста"):
        project_list_before = api.get_project_list(API_key)

    with allure.step("Создание нового проекта через UI"):
        main.create_project_click()
        main.create_project_title()
        main.create_project_click_button()

    with allure.step("Название на карточке проекта"):
        project_card = main.proj_card()

    with allure.step("Дублирование проекта"):
        main.double_project()

    with allure.step("Количество проектов после создания и дублирования"):
        project_list_after = api.get_project_list(API_key)

    with allure.step("Название на карточке дублированного проекта"):
        double_project_card = main.proj_card()

    with allure.step("Проверка совпадения названия на карточке с заданным"):
        assert double_project_card == f"{project_card} (2)"

    with allure.step("Количество проектов увеличилось на 2"):
        assert project_list_after - project_list_before == 2

    with allure.step("Удаление тестовых данных"):
        main.delete_project()
