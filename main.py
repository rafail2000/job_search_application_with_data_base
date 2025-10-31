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



if __name__ == '__main__':
    main()

