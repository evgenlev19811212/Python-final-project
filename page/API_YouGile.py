import requests
from dotenv import load_dotenv
import os
import allure


class apiYouGile:
    def __init__(self) -> None:
        """
        Конструктор класса apiYouGile.
        Передаёт URL из переменной в файле .env.

        """
        load_dotenv()
        self.url = os.getenv('base_url')

    @allure.step("Получение списка компаний")
    def get_companies(self) -> str:
        """
        Получает список компаний.
        Возвращает id первой компании из списка.

        :return IdCompany: str — id первой компании из списка.
        """
        load_dotenv()
        login = os.getenv('login')
        password = os.getenv('password')
        body = {
                "login": login,
                "password": password
                }
        resp = requests.post(self.url+'/api-v2/auth/companies', json=body)
        IdCompany = resp.json()['content'][0]['id']
        return IdCompany

    @allure.step("Получение списка ключей авторизации по id компании")
    def get_keys(self, IdCompany: str) -> str:
        """
        Получает список ключей авторизации для конкретной компании по её id.
        Возвращает первый ключ из списка.

        :param IdCompany: str — id компании.
        :return API_key: str — первый ключ из списка.
        """
        load_dotenv()
        login = os.getenv('login')
        password = os.getenv('password')
        body = {
                "login": login,
                "password": password,
                "companyId": IdCompany
                }
        resp = requests.post(self.url+'/api-v2/auth/keys/get', json=body)
        API_key = resp.json()[0]['key']
        return API_key

    @allure.step("Создание нового проекта")
    def create_project(self, API_key: str, title: str = "Best Of Project") -> dict: # noqa
        """
        Создаёт новый проект.
        Возвращает тело ответа.

        :param API_key: str — ключ авторизации конкретной компании.
        :param title: str — название проекта. По умолчанию задано
        "Best Of Project", но можно задать своё при вызове метода.
        :return resp: dict — тело ответа.
        """
        body = {
                "title": title,
                "users": {"0c895364-f956-4810-a0e0-4011d09f603b": "admin"}
                }
        headers = {
                    "Authorization": f"Bearer {API_key}"
                    }
        resp = requests.post(f"{self.url}/api-v2/projects", json=body, headers=headers) # noqa
        return resp

    @allure.step("Редактирование названия существующего проекта по его id")
    def edit_project(self, API_key: str, project_Id: str, title: str = "Best Project Of My Company") -> dict: # noqa
        """
        Редактирует название существующего проекта по его id.
        Возвращает тело ответа.

        :param API_key: str — ключ авторизации конкретной компании.
        :param project_Id: str — id проекта.
        :param title: str — название проекта. По умолчанию задано
        "Best Project Of My Company", но можно задать своё при вызове метода.
        :return resp: dict — тело ответа.
        """
        body = {
                "title": title
                }
        headers = {
                    "Authorization": f"Bearer {API_key}"
                    }
        resp = requests.put(f"{self.url}/api-v2/projects/{project_Id}", json=body, headers=headers) # noqa
        return resp

    @allure.step("Получение проекта по его id")
    def get_for_id(self, API_key: str, project_Id: str) -> dict:
        """
        Получает проект по его id.
        Возвращает тело ответа.

        :param API_key: str — ключ авторизации конкретной компании.
        :param project_Id: str — id проекта.
        :return resp: dict — тело ответа.
        """
        headers = {
                    "Authorization": f"Bearer {API_key}"
                    }
        resp = requests.get(f"{self.url}/api-v2/projects/{project_Id}", headers=headers) # noqa
        return resp

    @allure.step("Удаление проекта по его id")
    def delete_project(self, API_key: str, project_Id: str) -> str:
        """
        Удаляет проект по его id.
        Возвращает id удалённого проекта.

        :param API_key: str — ключ авторизации конкретной компании.
        :param project_Id: str — id проекта.
        :return del_Id: str — id удалённого проекта.
        """
        headers = {
                    "Authorization": f"Bearer {API_key}"
                    }
        body = {
                "deleted": True
                }
        resp = requests.put(f"{self.url}/api-v2/projects/{project_Id}", json=body, headers=headers) # noqa
        del_Id = resp.json()['id']
        return del_Id
