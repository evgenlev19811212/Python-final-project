# Python-final-project

## Шаблон для автоматизации тестирования на python

### Стек:
- pytest
- selenium
- requests
- allure
- config

### Струткура:
- ./test - тесты
- ./pages - описание страниц

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Тест-план Финального проекта](https://beasteam.yonote.ru/share/48be1488-4c9c-499f-b982-4e31b9bcce8f)
- [Отчет о тестировании Финального проекта](https://beasteam.yonote.ru/share/9ab82551-315f-4382-a6b6-375c5ac7feaa)

### Шаги
1. Склонировать проект 'git clone https://github.com/evgenlev19811212/Python-final-project.git'
2. Установить зависимости 'pip install -r requirements.txt'
3. Запустить тесты 'pytest'
4. Запустить тесты 'pytest -m "api"'
5. Запустить тесты 'pytest -m "ui"'
6. Запустить тесты 'pytest --alluredir allure-result'
7. Ознакомиться с отчётом 'allure serve allure-result'

### Библиотеки (!)
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install requests
- pip install allure-pytest