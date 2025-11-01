import os

from dotenv import load_dotenv

from src.api import HeadHunterAPI
from src.postgres_db import PostgresDB

companies_url = {'Skyeng': 'https://api.hh.ru/vacancies?employer_id=1122462',
                 'Яндекс Практикум': 'https://api.hh.ru/vacancies?employer_id=5008932'
                 }


def main():
    hh = HeadHunterAPI(companies_url)

    load_dotenv()

    db_config = {
        'user': os.getenv('POSTGRES_USER'),
        'password': os.getenv('POSTGRES_PASSWORD'),
        'host': os.getenv('POSTGRES_HOST'),
        'port': os.getenv('POSTGRES_PORT'),
        'dbname': os.getenv('POSTGRES_DB')
    }

    db = PostgresDB(**db_config)
    db.insert_data(hh.companies)
    print(db.get_companies_and_vacancies_count())
    print(db.get_all_vacancies())
    print(db.get_avg_salary())
    print(db.get_vacancies_with_higher_salary())
    print(db.get_vacancies_with_keyword('Бухгалтер'))



if __name__ == '__main__':
    main()

