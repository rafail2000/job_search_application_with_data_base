from src.vacancy import Vacancy


def test_vacancy_init(raw_vacancy):
    """ Тесты инициализации класса Vacancy """

    vacancy1 = Vacancy(raw_vacancy[0])
    vacancy2 = Vacancy(raw_vacancy[1])

    assert vacancy1.vacancy_name == "Куратор студентов"
    assert vacancy1.salary == 50000
    assert vacancy2.salary == 50000
    assert vacancy1.url == "https://api.hh.ru/vacancies/125673844?host=hh.ru"

def test_vacancy_repr(raw_vacancy):
    """ Тест магического метода __repr__ """

    vacancy1 = Vacancy(raw_vacancy[0])

    assert repr(vacancy1) == "<class 'src.vacancy.Vacancy'>, Куратор студентов, 50000, https://api.hh.ru/vacancies/125673844?host=hh.ru"