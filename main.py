from src.api import HeadHunterAPI

companies_url = {'Skyeng': 'https://api.hh.ru/vacancies?employer_id=1122462',
                  'Яндекс Практикум': 'https://api.hh.ru/vacancies?employer_id=5008932'
                  }


def main():
    hh = HeadHunterAPI(companies_url)
    print([i.__dict__ for i in hh.companies])

if __name__ == '__main__':
    main()

