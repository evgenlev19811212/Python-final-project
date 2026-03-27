from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure


class AuthPage:
    def __init__(self, driver: webdriver) -> None:
        """
        Конструктор класса AuthPage.
        Передаёт в webdriver url страницы авторизации.

        :param driver: webdriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.driver.get("https://ru.yougile.com/team/")

    @allure.step("Заполнение формы авторизации")
    def send_login(self) -> None:
        """
        Вводит логин и пароль в форму авторизации.
        """
        load_dotenv()
        login = os.getenv('login')
        password = os.getenv('password')
        self.driver.find_element(By.CSS_SELECTOR, '[type="email"]'
                                 ).send_keys(login)
        self.driver.find_element(By.CSS_SELECTOR, '[type="password"]'
                                 ).send_keys(password)

    @allure.step("Нажатие кнопки входа в аккаунт")
    def click_login(self) -> None:
        """
        Нажимает кнопку входа в аккаунт.
        """
        self.driver.find_element(By.CSS_SELECTOR, ".hint__cnt").click()


class MainPage:
    def __init__(self, driver: webdriver) -> None:
        """
        Конструктор класса MainPage.
        Инициализирует экземпляр страницы с драйвером браузера и
        механизмом ожидания элементов.

        Создаёт объект WebDriverWait с таймаутом 30 секунд для
        стабильного поиска элементов на странице. Это позволяет
        избежать ошибок из‑за асинхронной загрузки контента.

        :param driver: webdriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 1)

    @allure.step("Нажатие плюсика создания проекта")
    def create_project_click(self) -> None:
        """
        Кликает плюсик создания проекта.
        """
        self.wait.until(EC.element_to_be_clickable(
                        (By.XPATH,
                         "//span[text()='Добавить проект с задачами']"))
                        ).click()

    @allure.step("Ввод названия проекта")
    def create_project_title(self, title: str) -> None:
        """
        Очищает поле ввода и вводит название проекта.

        :param title: str — название проекта.
        """
        self.driver.find_element(By.CSS_SELECTOR,
                                 '[placeholder="Введите название проекта…"]'
                                 ).clear()
        self.driver.find_element(By.CSS_SELECTOR,
                                 '[placeholder="Введите название проекта…"]'
                                 ).send_keys(title)

    def is_create_project_button_active(self) -> bool:
        """
        Проверяет, активна ли кнопка добавления проекта с помощью EC.

        return bool: True если кнопка активна, False если неактивна
        """
        try:
            self.wait.until(EC.element_to_be_clickable((
                By.XPATH, "//div[text()='Добавить проект с задачами']"))
                ).click()
            return True
        except Exception:
            return False

    @allure.step("Нажатие кнопки отмены добавления проекта")
    def create_cancel_click(self) -> None:
        """
        Нажимает кнопку отмены добавления.
        """
        self.wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[text()='Отмена']"))).click()

    @allure.step("Нажатие кнопки добавления проекта")
    def create_project_click_button(self) -> None:
        """
        Нажимает кнопку добавления проекта.
        """
        self.wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[text()='Добавить проект с задачами']"))).click()

    @allure.step("Название на карточке проекта")
    def proj_card(self) -> str:
        """
        Считывает и возвращает название с карточки созданного проекта.

        :return proj_card: str - текст названия.
        """
        proj_card = self.wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '[data-testid="project-title"]'))).text
        return proj_card

    def len_proj_list(self) -> int:
        proj_list = self.wait.until(EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, '[data-testid="project-title"]')))
        return len(proj_list)

    @allure.step("Переименование проекта")
    def edit_project(self, title: str, new_title: str) -> None:
        cards = self.wait.until(EC.presence_of_all_elements_located((
            By.CSS_SELECTOR, '[data-testid="project-title"]')))
        for card in cards:
            if title in card.text:
                css = '[class="flex-none h-16 w-16 flex items-center justify-center"]' # noqa
                self.wait.until(EC.element_to_be_clickable((
                    By.CSS_SELECTOR, css))).click()
                self.wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//div[text()='Переименовать']"))).click()
                xpath = '//input[@placeholder="Введите название проекта…"]'
                project_title = self.wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, xpath)))
                project_title.send_keys(Keys.BACKSPACE * 20)
                project_title.send_keys(new_title, Keys.ENTER)
            break

    @allure.step("Удаление проекта")
    def delete_project(self, title: str = None, new_title: str = None) -> None:
        """
        Удаляет созданный для теста проект.
        :param title: str — название проекта.
        :param new_title: str — название проекта.
        """
        cards = self.wait.until(EC.presence_of_all_elements_located((
            By.CSS_SELECTOR, '[data-testid="project-title"]')))
        if title is not None:
            for card in cards:
                if title in card.text:
                    css = '[class="flex-none h-16 w-16 flex items-center justify-center"]' # noqa
                    self.driver.find_element(By.CSS_SELECTOR, css).click()
                    self.wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//div[text()='Удалить']"))).click()
                    css = '[class="flex bg-action-attention-default text-invert px-16 py-12 plain-text-semibold hover:bg-action-attention-hover active:bg-action-attention-pressed rounded-8 w-fit cursor-pointer select-none"]' # noqa
                    self.wait.until(EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, css))).click()

        if new_title is not None:
            for card in cards:
                if new_title in card.text:
                    css = '[class="flex-none h-16 w-16 flex items-center justify-center"]' # noqa
                    self.driver.find_element(By.CSS_SELECTOR, css).click()
                    self.wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//div[text()='Удалить']"))).click()
                    css = '[class="flex bg-action-attention-default text-invert px-16 py-12 plain-text-semibold hover:bg-action-attention-hover active:bg-action-attention-pressed rounded-8 w-fit cursor-pointer select-none"]' # noqa
                    self.wait.until(EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, css))).click()

    @allure.step("Дублирование проекта")
    def double_project(self, title: str) -> None:
        """
        Дублирует созданный для теста проект.
        :param title: str — название проекта.
        """
        cards = self.wait.until(EC.presence_of_all_elements_located((
            By.CSS_SELECTOR, '[data-testid="project-title"]')))
        for card in cards:
            if title in card.text:
                css = '[class="flex-none h-16 w-16 flex items-center justify-center"]' # noqa
                self.driver.find_element(By.CSS_SELECTOR, css).click()
                self.wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//div[text()='Дублировать']"))).click()
                self.wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//span[text()='Ok']"))).click()
                break

    @allure.step("Очистка тестового пространства")
    def clear_test_space(self) -> None:
        """
        Удаляет все карточки проектов без привязки к названию.
        """
        try:
            card = self.wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '[data-testid="project-title"]')))
            for card in card:
                css = '[class="flex-none h-16 w-16 flex items-center justify-center"]' # noqa
                self.driver.find_element(By.CSS_SELECTOR, css).click()
                self.wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//div[text()='Удалить']"))).click()
                css = '[class="flex bg-action-attention-default text-invert px-16 py-12 plain-text-semibold hover:bg-action-attention-hover active:bg-action-attention-pressed rounded-8 w-fit cursor-pointer select-none"]' # noqa
                self.wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, css))).click()
        except Exception:
            return None
