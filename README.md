# Автотесты для Stellar Burgers

---

## Описание проекта

Автоматизация тестирования веб-приложения [Stellar Burgers](https://stellarburgers.education-services.ru/) с помощью
**Selenium** и **pytest**.

---

## Как установить

1. Установить зависимости:

```
pip install -r requirements.txt
```

2. Установить `Google Chrome` и/или `Mozilla Firefox`.

---

## Как запустить

Для запуска всех тестов:

```
pytest -v
```

Для запуска в определённом браузере (Chrome по умолчанию):

```
pytest -v --browser chrome
pytest -v --browser firefox
```

---

## Результаты allure

Собрать отчёты allure:

```
pytest --alluredir=allure_results
```

Открыть результаты в браузере

```
allure serve allure_results
```
