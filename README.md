# selenium-page-object-project


Учебный проект по автоматизации тестирования с использованием Selenium WebDriver и паттерна Page Object.

## Описание

Проект содержит автотесты для интернет-магазина [Oscar Sandbox](http://selenium1py.pythonanywhere.com/).

## Структура проекта

- `conftest.py` — фикстура для запуска браузера с поддержкой параметра `--language`
- `pages/base_page.py` — базовый класс с общими методами
- `pages/product_page.py` — Page Object для страницы товара
- `test_product_page.py` — тесты для страницы товара
- `test_items.py` — тест на наличие кнопки добавления в корзину

## Что проверяется

- Добавление товара в корзину
- Совпадение названия товара в сообщении с названием на странице
- Совпадение цены товара в сообщении с ценой на странице
- Поддержка разных языков интерфейса

## Запуск тестов

```bash
pytest -s test_product_page.py
pytest --language=es test_items.py
