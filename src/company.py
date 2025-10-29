from abc import ABC


class AbstractCompany(ABC):
    """ Абстрактный класс компании """

    pass


class Company(AbstractCompany):
    """ Класс компания """

    def __init__(self, company_name: str, url_vacancies: str, lst_vacancies: list=None) -> None:
        """ Инициализация класса компании """

        self.company_name = company_name
        self.url_vacancies = url_vacancies
        self.lst_vacancies = lst_vacancies if lst_vacancies is not None else []