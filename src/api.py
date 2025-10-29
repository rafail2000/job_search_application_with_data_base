import requests

from src.company import Company
from src.vacancy import Vacancy


class AbstractHeadHunterAPI:
    """ Абстрактный метод для работы с API HeadHunter """


class HeadHunterAPI(AbstractHeadHunterAPI):
    """ Класс для работы с API HeadHunter """

    def __init__(self, companies_dict: dict) -> None:
        self.companies_dict = companies_dict
        self.companies = []

        self.append_vacancies()

    @staticmethod
    def load_vacancies(url):
        response = requests.get(url)
        return response.json()["items"]

    # @staticmethod
    # def validate_status_cod(response: requests.models.Response) -> bool:
    #     """ Метод проверки ответа сервера """
    #
    #     if response.status_code != 200:
    #         print(f"status_cod {response.status_code}")
    #         return True

    def append_vacancies(self) -> None:
        """ Метод загрузки вакансий """

        for k, v in self.companies_dict.items():
            vacancies = self.load_vacancies(v)
            self.companies.append(Company(k, v, [Vacancy(i) for i in vacancies]))

