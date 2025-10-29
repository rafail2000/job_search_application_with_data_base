import pytest


@pytest.fixture
def raw_vacancy():
    """ Фикстура с сырыми данными вакансии с сайта HeadHunter """

    return ({
        "id": "125673844",
        "premium": False,
        "name": "Куратор студентов",
        "department": False,
        "has_test": False,
        "response_letter_required": True,
        "area": {
            "id": "53",
            "name": "Краснодар",
            "url": "https://api.hh.ru/areas/53"
        },
        "salary": {
            "from": False,
            "to": 50000,
            "currency": "RUR",
            "gross": False
        },
        "salary_range": {
            "from": False,
            "to": 50000,
            "currency": "RUR",
            "gross": False,
            "mode": {
                "id": "MONTH",
                "name": "За месяц"
            },
            "frequency": False
        },
        "type": {
            "id": "open",
            "name": "Открытая"
        },
        "address": False,
        "response_url": False,
        "sort_point_distance": False,
        "published_at": "2025-10-27T09:32:33+0300",
        "created_at": "2025-10-27T09:32:33+0300",
        "archived": False,
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=125673844",
        "show_logo_in_search": False,
        "show_contacts": False,
        "insider_interview": False,
        "url": "https://api.hh.ru/vacancies/125673844?host=hh.ru",
        "alternate_url": "https://hh.ru/vacancy/125673844",
        "relations": [],
        "employer": {
            "id": "5008932",
            "name": "Яндекс Практикум",
            "url": "https://api.hh.ru/employers/5008932",
            "alternate_url": "https://hh.ru/employer/5008932",
            "logo_urls": {
                "original": "https://img.hhcdn.ru/employer-logo-original/900953.png",
                "90": "https://img.hhcdn.ru/employer-logo/4044499.png",
                "240": "https://img.hhcdn.ru/employer-logo/4044500.png"
            },
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=5008932",
            "country_id": 1,
            "accredited_it_employer": False,
            "trusted": True
        }
    },
    {
        "id": "125673844",
        "premium": False,
        "name": "Куратор студентов",
        "department": False,
        "has_test": False,
        "response_letter_required": True,
        "area": {
            "id": "53",
            "name": "Краснодар",
            "url": "https://api.hh.ru/areas/53"
        },
        "salary": {
            "from": 50000,
            "to": False,
            "currency": "RUR",
            "gross": False
        },
        "salary_range": {
            "from": False,
            "to": False,
            "currency": "RUR",
            "gross": False,
            "mode": {
                "id": "MONTH",
                "name": "За месяц"
            },
            "frequency": False
        },
        "type": {
            "id": "open",
            "name": "Открытая"
        },
        "address": False,
        "response_url": False,
        "sort_point_distance": False,
        "published_at": "2025-10-27T09:32:33+0300",
        "created_at": "2025-10-27T09:32:33+0300",
        "archived": False,
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=125673844",
        "show_logo_in_search": False,
        "show_contacts": False,
        "insider_interview": False,
        "url": "https://api.hh.ru/vacancies/125673844?host=hh.ru",
        "alternate_url": "https://hh.ru/vacancy/125673844",
        "relations": [],
        "employer": {
            "id": "5008932",
            "name": "Яндекс Практикум",
            "url": "https://api.hh.ru/employers/5008932",
            "alternate_url": "https://hh.ru/employer/5008932",
            "logo_urls": {
                "original": "https://img.hhcdn.ru/employer-logo-original/900953.png",
                "90": "https://img.hhcdn.ru/employer-logo/4044499.png",
                "240": "https://img.hhcdn.ru/employer-logo/4044500.png"
            },
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=5008932",
            "country_id": 1,
            "accredited_it_employer": False,
            "trusted": True
        }
    })
