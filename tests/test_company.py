from src.company import Company


def test_company_init(raw_company, raw_vacancy):
    """ Тест инициализации класса Company """

    company = Company(*raw_company.keys(), *raw_company.values())
    assert company.company_name == 'Skyeng'
    assert company.url_vacancies == 'https://api.hh.ru/vacancies?employer_id=1122462'
    assert company.lst_vacancies == []