import psycopg2

from src.company import Company


class PostgresDB:
    """ Класс для работы с базой данных """

    def __init__(self, dbname: str,
                 user: str,
                 password: str,
                 host: str='localhost',
                 port: str='5432') -> None:

        self.cur = None
        self.conn = None
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self._create_database_if_not_exist()
        self._connect_to_database()
        self._create_tables()

    def _connect_to_database(self, db_name: str=None):
        """ Подключение к базе данных """
        try:
            conn = psycopg2.connect(dbname=db_name,
                                    user=self.user,
                                    password=self.password,
                                    host=self.host,
                                    port=self.port
                                    )
            return conn
        except Exception as e:
            print(f"Ошибка подключения к базе данных: {e}")

    def _create_database_if_not_exist(self):
        """ Создание базы данных если её не существует"""

        conn = self._connect_to_database('postgres')
        conn.autocommit = True
        cur = conn.cursor()

        try:
            cur.execute(f'CREATE DATABASE {self.dbname}')
        except Exception as e:
            print(f"{e}")

        cur.close()
        conn.close()

    def _create_tables(self):
        """ Функция для создания таблиц companies и vacancies """

        try:
            self.conn = self._connect_to_database(self.dbname)
            self.cur = self.conn.cursor()
            with self.conn:
                self.cur.execute("""
                                    CREATE TABLE IF NOT EXISTS companies (
                                        company_id SERIAL PRIMARY KEY,
                                        company_name VARCHAR(255) UNIQUE NOT NULL
                                    );
        
                                    CREATE TABLE IF NOT EXISTS vacancies (
                                        vacancy_id SERIAL PRIMARY KEY,
                                        company_id INTEGER REFERENCES companies(company_id),
                                        vacancy_name VARCHAR(255) NOT NULL,
                                        salary REAL,
                                        url VARCHAR(255)
                                    );
                                """)
                print("Таблицы созданы успешно")
        except Exception as e:
            print(e)

    def insert_data(self, companies: list[Company]):
        """ Функция для вставки данных в таблицу """

        with self.conn:
            for company in companies:
                self.cur.execute(
                    f"INSERT INTO companies (company_name) VALUES (%s)",
                    (company.company_name,))

        counter = 0
        with self.conn:
            for company in companies:
                counter += 1
                for vacancy in company.lst_vacancies:
                    self.cur.execute(
                        f"""INSERT INTO vacancies (company_id, vacancy_name, salary, url)
                        VALUES (%s, %s, %s, %s)""",
                        (counter, vacancy.vacancy_name, vacancy.salary, vacancy.url)
                    )

        self.cur.close()
        self.conn.close()

    def get_companies_and_vacancies_count(self):
        """ Получает список всех компаний и количество вакансий у каждой компании. """

        self.conn = self._connect_to_database(self.dbname)
        self.cur = self.conn.cursor()
        with self.conn:
            self.cur.execute(f"""SELECT company_name, COUNT(*)
            FROM companies
            JOIN vacancies USING(company_id)
            GROUP BY company_name;"""
                             )
        data = self.cur.fetchall()
        data_dict = [{"company": d[0], "count_vacancy": d[1]} for d in data]
        self.cur.close()
        self.conn.close()

        return data_dict

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.
        """

        self.conn = self._connect_to_database(self.dbname)
        self.cur = self.conn.cursor()
        with self.conn:
            self.cur.execute(f"""SELECT company_name, vacancy_name, salary, url
            FROM companies
            JOIN vacancies USING(company_id);
            """
                             )
        data = self.cur.fetchall()
        data_dict = [{"company_name": d[0], "vacancy_name": d[1], "salary": d[2], "url": d[3]} for d in data]
        self.cur.close()
        self.conn.close()

        return data_dict

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям.
        """

        self.conn = self._connect_to_database(self.dbname)
        self.cur = self.conn.cursor()
        with self.conn:
            self.cur.execute(f"""SELECT vacancy_name, AVG(salary)
            FROM vacancies
            WHERE salary IS NOT NULL
            GROUP BY vacancy_name;
            
            """
                             )
        data = self.cur.fetchall()
        data_dict = [{"vacancy_name": d[0], "AVG(salary)": d[1]} for d in data]
        self.cur.close()
        self.conn.close()

        return data_dict

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий, у которых
        зарплата выше средней по всем вакансиям.
        """

        self.conn = self._connect_to_database(self.dbname)
        self.cur = self.conn.cursor()
        with self.conn:
            self.cur.execute(f"""
            SELECT vacancy_name
            FROM vacancies
            WHERE salary IS NOT NULL and salary > (SELECT AVG(salary) FROM vacancies WHERE salary IS NOT NULL);
            """
                             )
        data = self.cur.fetchall()
        data_dict = [{"vacancy_name": d[0]} for d in data]
        self.cur.close()
        self.conn.close()

        return data_dict

    def get_vacancies_with_keyword(self, keyword: str):
        """
        Получает список всех вакансий, в названии которых
        содержатся переданные в метод слова, например python.
        """

        self.conn = self._connect_to_database(self.dbname)
        self.cur = self.conn.cursor()
        with self.conn:
            self.cur.execute(f"""
            SELECT vacancy_name
            FROM vacancies
            WHERE vacancy_name LIKE '{keyword}';
            """
                             )
        data = self.cur.fetchall()
        data_dict = [{"vacancy_name": d[0]} for d in data]
        self.cur.close()
        self.conn.close()

        return data_dict