from page.UI_YouGile import MainPage
from page.API_YouGile import apiYouGile
import allure
import pytest


@pytest.mark.ui
@allure.title("Тестирование создания нового проекта через UI")
@allure.description("Тест проверяет корректность создания нового проекта")
@allure.feature("Работа с проектами")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_project_positive(auth, API_key, driver, clear):
    """
    Тест проверяет корректность создания нового проекта.
    """
    api = apiYouGile()
    main = MainPage(driver)
    title = "New Project"

    with allure.step("Количество проектов до начала теста 0"):
        project_list_before = api.get_project_list(API_key)

    with allure.step("Создание нового проекта через UI"):
        main.create_project_click()
        main.create_project_title(title)
        main.create_project_click_button()

    with allure.step("Название на карточке проекта"):
        project_card = main.proj_card()

    with allure.step("Название на карточке совпадает с заданным"):
        assert title in project_card
        (f"Элемент не содержит текст {title}. Текущий текст: {project_card}")

    with allure.step("Количество проектов после создания"):
        project_list_after = api.get_project_list(API_key)

    with allure.step("Количество проектов увеличилось на 1"):
        assert project_list_after - project_list_before == 1

    with allure.step("Удаление тестовых данных"):
        main.clear_test_space()

    with allure.step("Количество проектов после удаления 0"):
        api.get_project_list(API_key)


@pytest.mark.ui
@allure.title("Тестирование дублирования проектов")
@allure.description("Тест проверяет дублирование проектов")
@allure.feature("Работа с проектами")
@allure.severity(allure.severity_level.NORMAL)
def test_double_project(auth, driver, API_key, clear) -> None:
    """
    Тест проверяет дублирование проектов.
    """
    api = apiYouGile()
    main = MainPage(driver)
    title = "New Project"

    with allure.step("Количество проектов до начала теста 0"):
        project_list_before = api.get_project_list(API_key)

    with allure.step("Создание нового проекта через UI"):
        main.create_project_click()
        main.create_project_title(title)
        main.create_project_click_button()

    with allure.step("Название на карточке проекта"):
        project_card = main.proj_card()

    with allure.step("Проверка совпадения названия на карточке с заданным"):
        assert title in project_card
        (f"Элемент не содержит текст {title}. Текущий текст: {project_card}")

    with allure.step("Количество проектов после создания"):
        project_list_after = api.get_project_list(API_key)

    with allure.step("Количество проектов увеличилось на 1"):
        assert project_list_after - project_list_before == 1

    with allure.step("Дублирование проекта"):
        main.double_project(title)

    with allure.step("Количество проектов после создания и дублирования"):
        project_list_double = api.get_project_list(API_key)

    with allure.step("Количество проектов увеличилось ещё на 1"):
        assert project_list_double - project_list_before == 2

    with allure.step("Название на карточке дублированного проекта"):
        double_project_card = main.proj_card()

    with allure.step("Проверка совпадения названия на карточке с заданным"):
        assert double_project_card == f"{project_card} (2)"

    with allure.step("Удаление тестовых данных"):
        main.clear_test_space()

    with allure.step("Количество проектов после удаления 0"):
        api.get_project_list(API_key)


@pytest.mark.ui
@allure.title("Тестирование переименования проектов")
@allure.description("Тест проверяет переименование проектов")
@allure.feature("Работа с проектами")
@allure.severity(allure.severity_level.CRITICAL)
def test_edit_project_positive(auth, driver, API_key, clear):
    """
    Тест проверяет возможность переименования проектов.
    """
    api = apiYouGile()
    main = MainPage(driver)
    title = "New Project"
    new_title = "Newest Project"

    with allure.step("Количество проектов до начала теста 0"):
        project_list_before = api.get_project_list(API_key)

    with allure.step("Создание нового проекта через UI"):
        main.create_project_click()
        main.create_project_title(title)
        main.create_project_click_button()

    with allure.step("Название на карточке проекта"):
        project_card = main.proj_card()

    with allure.step("Проверка совпадения названия на карточке с заданным"):
        assert title in project_card
        (f"Элемент не содержит текст {title}. Текущий текст: {project_card}")

    with allure.step("Количество проектов после создания"):
        project_list_after = api.get_project_list(API_key)

    with allure.step("Количество проектов увеличилось на 1"):
        assert project_list_after - project_list_before == 1

    with allure.step("Переименование проекта"):
        main.edit_project(title, new_title)

    with allure.step("Название на карточке проекта"):
        project_card = main.proj_card()

    with allure.step("Проверка совпадения названия на карточке с заданным"):
        assert new_title in project_card
        (f"Элемент не содержит текст {new_title}.Текущий текст: {project_card}"
         )

    with allure.step("Удаление тестовых данных"):
        main.clear_test_space()

    with allure.step("Количество проектов после удаления 0"):
        api.get_project_list(API_key)


@pytest.mark.ui
@allure.title("Тестирование невозможности создания нового проекта с названием из пробелов") # noqa
@allure.description("Тест проверяет НЕсоздание проекта с названием из пробелов") # noqa
@allure.feature("Работа с проектами")
@allure.severity(allure.severity_level.MINOR)
def test_create_project_negative(auth, driver, clear) -> None:
    """
    Тест проверяет НЕсоздание проекта с названием из пробелов.
    """
    main = MainPage(driver)

    with allure.step("Создание нового проекта через UI"):
        main.create_project_click()
        main.create_project_title("     ")
        button = main.is_create_project_button_active()

    with allure.step("Проверка неактивности кнопки"):
        assert button is False

    with allure.step("Нажатие кнопки отмены"):
        main.create_cancel_click()


@pytest.mark.ui
@allure.title("Тестирование невозможности пустого названия при переименовании проекта") # noqa
@allure.description("Тест проверяет НЕпереименование проекта")
@allure.feature("Работа с проектами")
@allure.severity(allure.severity_level.MINOR)
def test_edit_project_negative(auth, driver, API_key, clear):
    """
    Тест проверяет возможность переименования проектов.
    """
    api = apiYouGile()
    main = MainPage(driver)
    title = "New Project"
    new_title = ""

    with allure.step("Количество проектов до начала теста 0"):
        project_list_before = api.get_project_list(API_key)

    with allure.step("Создание нового проекта через UI"):
        main.create_project_click()
        main.create_project_title(title)
        main.create_project_click_button()

    with allure.step("Название на карточке проекта"):
        project_card = main.proj_card()

    with allure.step("Проверка совпадения названия на карточке с заданным"):
        assert title in project_card
        (f"Элемент не содержит текст {title}. Текущий текст: {project_card}")

    with allure.step("Количество проектов после создания"):
        project_list_after = api.get_project_list(API_key)

    with allure.step("Количество проектов увеличилось на 1"):
        assert project_list_after - project_list_before == 1

    with allure.step("Переименование проекта"):
        main.edit_project(title, new_title)

    with allure.step("Название на карточке проекта"):
        project_card = main.proj_card()

    with allure.step("Название не изменилось"):
        assert title in project_card
        (f"Элемент не содержит текст {title}.Текущий текст: {project_card}"
         )

    with allure.step("Удаление тестовых данных"):
        main.clear_test_space()

    with allure.step("Количество проектов после удаления 0"):
        api.get_project_list(API_key)
