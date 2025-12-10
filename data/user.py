from dataclasses import dataclass


@dataclass(frozen=True)
class UserTestData:
    NAME: str = "Иван"
    EMAIL: str = "ivanov9940124@ya.ru"
    PASSWORD: str = "SoStrong123"
