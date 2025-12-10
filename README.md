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

2. Установить `Google Chrome` и `Mozilla Firefox`.

---

## Как запустить

Для запуска всех тестов:

```
pytest -v
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
