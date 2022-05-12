import requests
from sqlalchemy import engine as sql
import time
import datetime
import pandas as pd
from DB_config import server, user, password, port, database

# Функция возвращает массив всех возможных area_id
# Это необходимо для дальнейшей детализации запросов по вакансиям, т.к. API HH не возвращает более 2000 записей
def GetLeafs(element, areas_leafs):
    areas = element['areas']
    if len(areas) == 0:
        areas_leafs.append(element['id'])
    else:
        for l in range(len(areas)):
            GetLeafs(areas[l], areas_leafs)

def GetAreas():
    areas_leafs = []
    areas_Json = requests.get('https://api.hh.ru/areas').json()
    for e in range(len(areas_Json)):
        GetLeafs(areas_Json[e], areas_leafs)

    print('Получено {} местоположений'.format(len(areas_leafs)))
    # Дальнейшие изощрения необходимы для дальнейшей детализации запросов по вакансиям, т.к. API HH не возвращает более 2000 записей

    areas_leafs.remove('1') # Москва
    areas_leafs.remove('2') # Санкт-Петербург
    areas_leafs.remove('4') # Новосибирск
    areas_leafs.remove('3') # Екаеринбург
    areas_leafs.remove('88') # Казань
    areas_leafs.remove('66') # Нижний Новгород
    areas = [areas_leafs[d:d+500] for d in range(0, len(areas_leafs), 500)] # Длина get-запроса не позволяет вставить больше за раз
    areas.append('1')
    areas.append('2')
    areas.append('4')
    areas.append('3')
    areas.append('88')
    areas.append('66')

    return areas

# Функция для получения id всех вакансий, удовлетворяющих условиям. На вход принимает в виде параметра
# text - Переданное значение ищется в полях вакансии, указанных в параметре search_field.
# areas - регионы для поиска
def SaveVacanciesIdForLoad(text, vacancy_type, areas, stop_names):

    connection_str = 'postgresql://{}:{}@{}:{}/{}'.format(user, password, server, port, database)
    eng = sql.create_engine(connection_str)
    conn = eng.connect()
    # conn.execute('truncate table "public".Vacancies_for_load')
    conn.execute('DELETE FROM public.Vacancies_for_load WHERE vacancy_type= \'{}\''.format(vacancy_type))

    vacanciesId = set()
    vacancy_count = 0

    for area in areas:
        params = {
        'text': text,
        'area': area,
        'page': 0, # Индекс страницы поиска на HH
        'per_page': 100 # Кол-во вакансий на 1 странице
        }

        req = requests.get('https://api.hh.ru/vacancies', params).json()
        if req['found'] == 0:
            continue
        else:
            for p in range(req['pages']):
                params['page'] = p
                reqp = requests.get('https://api.hh.ru/vacancies', params).json()

                for item in reqp['items']:

                    wrong_vac = False
                    for stop_name in stop_names:
                        if stop_name in item['name'].lower():
                            wrong_vac = True

                    if not wrong_vac:
                        len_old = len(vacanciesId)
                        vacanciesId.add(item['id'])
                        len_new = len(vacanciesId)
                        if len_new > len_old:
                            conn.execute('INSERT INTO public.vacancies_for_load (id, vacancy_type) VALUES(\'{}\', \'{}\')'.format(item['id'], vacancy_type))

                            vacancy_count += 1
                            if vacancy_count % 100 == 0:
                                print('Для обработки записано {} вакансий'.format(vacancy_count))
    conn.close()


# Функция выполняет получение и запись данных в SQL по списку вакансий
def GetAndWriteVacanciesData(vacancy_type, new_load):
    update_date = datetime.datetime.now().strftime('%d-%m-%Y')

    currencies = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']

    df_index = ['id','vacancy_type', 'name', 'update_date', 'schedule','experience','area_name','url','employment','salary_from',\
                'salary_to','salary_currency','currency_exchange' ,'salary_gross','archived','created_date','published_date',\
                'emloyer_name', 'employer_url','employer_trusted','status','has_test','premium']
    df_vacancies = pd.DataFrame(columns=df_index)

    df_index = ['id', 'vacancy_type', 'name']
    df_key_skills = pd.DataFrame(columns=df_index)

    connection_str = 'postgresql://{}:{}@{}:{}/{}'.format(user, password, server, port, database)
    eng = sql.create_engine(connection_str)
    conn = eng.connect()
    if new_load:
        conn.execute('DELETE FROM public.Vacancies WHERE vacancy_type= \'{}\''.format(vacancy_type))
        conn.execute('DELETE FROM public.Vacancies_key_skills WHERE vacancy_type= \'{}\''.format(vacancy_type))

    vacancies_for_load = pd.read_sql('SELECT * FROM "public".Vacancies_for_load WHERE vacancy_type= \'{}\''.format(vacancy_type), conn)

    vacancy_count = 0

    for i, row in vacancies_for_load.iterrows():
        # time.sleep(0.25)
        id = row['id']

        df_vacancies = df_vacancies.iloc[0:0]
        df_key_skills = df_key_skills.iloc[0:0]

        req = requests.get('https://api.hh.ru/vacancies/{}'.format(id)).json()
        name = req['name']
        try:
            schedule = req['schedule']['name']
        except:
            schedule = None
        try:
            experience = req['experience']['name']
        except:
            experience = None
        try:
            area_name = req['area']['name']
        except:
            area_name = None
        url = req['alternate_url']
        try:
            employment = req['employment']['name']
        except:
            employment = None
        try:
            salary_from = req['salary']['from']
        except:
            salary_from = None
        try:
            salary_to = req['salary']['to']
        except:
            salary_to = None
        try:
            salary_currency = req['salary']['currency']
        except:
            salary_currency = None
        try:
            if salary_currency == 'RUR':
                currency_exchange = 1
            elif salary_currency == 'BYR':
                currency_exchange = currencies['BYN']['Value']/currencies['BYN']['Nominal']
            else:
                currency_exchange = currencies[salary_currency]['Value']/currencies[salary_currency]['Nominal']
        except:
            currency_exchange = None
        try:
            salary_gross = req['salary']['gross']
        except:
            salary_gross = None
        archived = req['archived']
        created_date = req['created_at'][0:10]
        published_date = req['published_at'][0:10]
        try:
            emloyer_name = req['employer']['name']
        except:
            emloyer_name = None
        try:
            employer_url = req['employer']['alternate_url']
        except:
            employer_url = None
        try:
            employer_trusted = req['employer']['trusted']
        except:
            employer_trusted = None
        try:
            status = req['type']['name']
        except:
            status = None
        has_test = req['has_test']
        premium = req['premium']

        vacancy_data = [id, vacancy_type, name, update_date, schedule, experience, area_name, url, employment, salary_from,
                        salary_to, salary_currency, currency_exchange, salary_gross, archived, created_date, published_date, emloyer_name,
                        employer_url, employer_trusted, status, has_test, premium]
        df_vacancies.loc[0] = vacancy_data

        key_skills = req['key_skills']
        for k in key_skills:
            key_skills_data = [id, vacancy_type, k['name']]
            df_key_skills.loc[0] = key_skills_data

        df_vacancies.to_sql('vacancies', conn, schema='public', if_exists='append', index=False)
        df_key_skills.to_sql('vacancies_key_skills', conn, schema='public', if_exists='append', index=False)
        conn.execute('DELETE FROM public.vacancies_for_load WHERE id=\'{}\' AND vacancy_type= \'{}\''.format(id, vacancy_type))

        vacancy_count += 1
        if vacancy_count % 100 == 0:
            print('В SQL загружено {} вакансий'.format(vacancy_count))

    # В базе необходимо почистить дубли строк вакансий по ключу "Работодатель-название вакансии",
    # т.к. один работодатель часто дублирует одну и ту же вакансию по разным городам, а это испортит статистику
    conn.execute('DELETE FROM public.Vacancies v1 USING public.Vacancies v2 WHERE v1.id < v2.id and v1.vacancy_type = \'{}\' ' \
                 'AND v1.name = v2.name and v1.employer_url = v2.employer_url'.format(vacancy_type))

    conn.close()
    print('Запись данных вакансий в SQL завершена')