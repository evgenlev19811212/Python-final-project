from page.API_YouGile import apiYouGile
import allure
import pytest

api = apiYouGile()


@pytest.mark.api
@allure.title("Тестирование создания нового проекта через API")
@allure.description("Тест проверяет корректность создания нового проекта")
@allure.feature("Работа с проектами")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_project_positive(API_key: str) -> None:
    """
    Тест проверяет корректность создания нового проекта.
    """
    with allure.step("Создание нового проекта через API"):
        resp = api.create_project(API_key)

    with allure.step("Извлечение id созданного проекта из тела ответа"):
        project_Id = resp.json()['id']

    with allure.step("Проверка статус-кода ответа 201"):
        assert resp.status_code == 201

    with allure.step("Удаление тестовых данных"):
        del_Id = api.delete_project(API_key, project_Id)

    with allure.step("Проверка удаления"):
        assert del_Id == project_Id


@pytest.mark.api
@allure.title("Тестирование невозможности создания нового проекта без названия через API") # noqa
@allure.description("Тест проверяет НЕсоздание проекта без названия")
@allure.feature("Работа с проектами")
@allure.severity(allure.severity_level.MINOR)
def test_create_project_negative(API_key: str) -> None:
    """
    Тест проверяет НЕсоздание проекта без названия
    """

    with allure.step("Запрос на создание проекта без названия через API"):
        resp = api.create_project(API_key, "")

    with allure.step("Проверка НЕсоздания: статус-код 400"):
        assert resp.status_code == 400

    with allure.step("Проверка НЕсоздания: в теле ответа сообщение 'title should not be empty'"):  # noqa
        assert resp.json()["message"] == ["title should not be empty"]


@pytest.mark.api
@allure.title("Тестирование редактирования названия проекта через API")
@allure.description("Тест проверяет редактирование названия проекта")
@allure.feature("Работа с проектами")
@allure.severity(allure.severity_level.CRITICAL)
def test_edit_project_positive(API_key: str) -> None:
    """
    Тест проверяет редактирование названия проекта.
    """
    with allure.step("Создание нового проекта через API"):
        resp = api.create_project(API_key)

    with allure.step("Извлечение id созданного проекта из тела ответа"):
        project_Id = resp.json()['id']

    with allure.step("Проверка статус-кода ответа 201"):
        assert resp.status_code == 201

    with allure.step("Редактирование названия проекта"):
        resp_edit = api.edit_project(API_key, project_Id)

    with allure.step("Проверка статус-кода ответа 200"):
        assert resp_edit.status_code == 200

    with allure.step("Проверка: id проекта не изменился"):
        assert resp_edit.json()['id'] == project_Id

    with allure.step("Удаление тестовых данных"):
        del_Id = api.delete_project(API_key, project_Id)

    with allure.step("Проверка удаления"):
        assert del_Id == project_Id


@pytest.mark.api
@allure.title("Тестирование невозможности проекта без названия при редактировании через API") # noqa
@allure.description("Тест проверяет невозможность оставить проект без названия при редактировании") # noqa
@allure.feature("Работа с проектами")
@allure.severity(allure.severity_level.MINOR)
def test_edit_project_negative(API_key: str) -> None:
    """
    Тест проверяет невозможность оставить
    проект без названия при редактировании.
    """
    with allure.step("Создание нового проекта через API"):
        resp = api.create_project(API_key)

    with allure.step("Извлечение id созданного проекта из тела ответа"):
        project_Id = resp.json()['id']

    with allure.step("Проверка статус-кода ответа 201"):
        assert resp.status_code == 201

    with allure.step("Редактирование названия проекта: без названия"):
        resp_edit = api.edit_project(API_key, project_Id, "")

    with allure.step("Проверка НЕредактирования: статус-код 400"):
        assert resp_edit.status_code == 400

    with allure.step("Проверка НЕредактирования: в теле ответа сообщение 'title should not be empty'"): # noqa
        assert resp_edit.json()["message"] == ["title should not be empty"]

    with allure.step("Удаление тестовых данных"):
        del_Id = api.delete_project(API_key, project_Id)

    with allure.step("Проверка удаления"):
        assert del_Id == project_Id


@pytest.mark.api
@allure.title("Тестирование получения проекта по его id через API")
@allure.description("Тест проверяет корректность получения проекта по его id")
@allure.feature("Работа с проектами")
@allure.severity(allure.severity_level.NORMAL)
def test_get_for_id_positive(API_key: str) -> None:
    """
    Тест проверяет корректность получения проекта по его id.
    """
    with allure.step("Создание нового проекта через API"):
        resp = api.create_project(API_key)

    with allure.step("Извлечение id созданного проекта из тела ответа"):
        project_Id = resp.json()['id']

    with allure.step("Проверка статус-кода ответа 201"):
        assert resp.status_code == 201

    with allure.step("Получение проекта по id"):
        resp_get = api.get_for_id(API_key, project_Id)

    with allure.step("Проверка получения: статус-код 200"):
        assert resp_get.status_code == 200

    with allure.step("Проверка получения: id в теле ответа идентичен id созданного проекта"): # noqa
        assert resp_get.json()['id'] == project_Id

    with allure.step("Проверка получения: название проекта в теле ответа совпадает с названием созданного"): # noqa
        assert resp_get.json()['title'] == "Best Of Project"

    with allure.step("Удаление тестовых данных"):
        del_Id = api.delete_project(API_key, project_Id)

    with allure.step("Проверка удаления"):
        assert del_Id == project_Id


@pytest.mark.api
@allure.title("Тестирование получения проекта по некорректному id через API")
@allure.description("Тест проверяет НЕполучение проекта по некорректному id")
@allure.feature("Работа с проектами")
@allure.severity(allure.severity_level.MINOR)
def test_get_for_id_negative(API_key: str) -> None:
    """
    Тест проверяет НЕполучение проекта по некорректному id.
    """
    with allure.step("Получение проекта по некорректному id 123"):
        resp = api.get_for_id(API_key, "123")

    with allure.step("Проверка НЕполучения: статус-код 404"):
        assert resp.status_code == 404

    with allure.step("Проверка НЕполучения: в теле ответа сообщение 'Проект не найден'"): # noqa
        assert resp.json()["message"] == "Проект не найден"

    with allure.step("Проверка НЕполучения: в теле ответа ошибка 'Not Found'"):
        assert resp.json()["error"] == "Not Found"
