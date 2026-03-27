# Python-final-project

## Проект по автоматизации тестирования на python для YouGile
Проект YouGile представляет собой систему управления проектами и коммуникациями в команде, которая объединяет в себе таск-трекер, корпоративный мессенджер и простую CRM для управления взаимоотношениями с клиентами. Более подробно можно оснакомиться в тест-плане Финального проекта (ссылка приведена ниже).

## Инструкция
Файл "env.txt" переименовать в ".env" (или скопировать содержимое "env.txt" в ".env")
Вписать свои значения в "login" и "password". В API-методах создания и редактирования проектов название проекта задано по умолчанию. Можно указать своё при вызове метода, но в этом случае нужно скорректировать проверку названия в тесте по получению проекта по ID.

### Стек:
- pytest
- selenium
- requests
- allure

### Струткура:
- ./test - тесты
- ./page - описание страниц

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [YouGile](https://ru.yougile.com/)
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