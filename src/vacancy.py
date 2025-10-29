from abc import ABC, abstractmethod


class AbstractVacancy(ABC):
    """ Абстрактный клас вакансии """

    @staticmethod
    @abstractmethod
    def validate_name(vacancy_name: dict) -> (str, bool):
        """ Абстрактный метод проверки названия вакансии"""


    @staticmethod
    @abstractmethod
    def validate_salary(salary: dict) -> (float, bool):
        """ Абстрактный метод проверки наличия зарплаты вакансии """


    @staticmethod
    @abstractmethod
    def validate_url(url: dict) -> (str, bool):
        """ Абстрактный метод проверки наличия url вакансии """



class Vacancy(AbstractVacancy):
    """ Класс вакансии """

    def __init__(self, data_vacancy: dict) -> None:
        """ Инициализация вакансии """

        self.vacancy_name = self.validate_name(data_vacancy)
        self.salary = self.validate_salary(data_vacancy)
        self.url = self.validate_url(data_vacancy)

    def __repr__(self):
        return f"{__class__}, {self.vacancy_name}, {self.salary}, {self.url}"

    @staticmethod
    def validate_name(vacancy_name: dict) -> (str, bool):
        """ Проверка названия вакансии """

        if vacancy_name.get('name', False):
            return vacancy_name['name']

    @staticmethod
    def validate_salary(salary: dict) -> (float, bool):
        """ Проверка наличия зарплаты вакансии """

        if not salary.get('salary'):
            return
        elif salary.get('salary').get('from'):
            return salary['salary']['from']
        elif salary.get('salary').get('to'):
            return salary['salary']['to']

    @staticmethod
    def validate_url(url: dict) -> (str, bool):
        """ Проверка наличия url вакансии """

        if url.get('url', False):
            return url['url']
