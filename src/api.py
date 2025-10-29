#
#
# class HeadHunterAPI(AbstractHeadHunterAPI):
#     """ Класс для работы с API HeadHunter """
#
#     def __init__(self, company_name: str, vacancy_name: str, salary: float, description: str, url: str) -> None:
#         self.url = 'https://api.hh.ru/vacancies'
#         self.headers = {'User-Agent': 'HH-User-Agent'}
#         self.params = {'text': '', 'page': 0, 'per_page': 100}
#         self.vacancies = []
#
#     @staticmethod
#     def _validate_status_cod(response: requests.models.Response) -> bool:
#         """ Метод проверки ответа сервера """
#
#         if response.status_code != 200:
#             print(f"status_cod {response.status_code}")
#             return True
#
#     def _load_vacancies(self, keyword: str) -> None:
#         """ Метод загрузки вакансий """
#
#         self.params['text'] = keyword
#         while self.params.get('page') != 20:
#             response = requests.get(self.url, headers=self.headers, params=self.params)
#             if self._validate_status_cod(response):
#                 break
#             vacancies = response.json()['items']
#             self.vacancies.extend(vacancies)
#             self.params['page'] += 1