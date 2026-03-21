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