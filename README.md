# Анализ вакансий. Краткая документация.

<code>[Документация по API HH](https://github.com/hhru/api)

Для хранения полученных с HH данных понадобится база данных.
Схема БД:

<code>![DB Scheme](https://github.com/timurborisevich/Vacancy-analysis/blob/master/DB_scheme.PNG "")</code>

1. Таблица "Vacancies_for_load" содержит список id вакансий, по которым далее будут выполняться точечные запросы. 
Заполняется на первой итерации.
2. Таблица "Vacancies" - основная таблица для анализа. Содержит список вакансий c загруженными параметрами.
3. Таблица "Vacancies_key_skills" содержит список ключевых навыков по каждой вакансии. 
Связь записей между таблицами "Vacancies" и "Vacancies_key_skills" = 1 ко многим.
4. Таблица "Update_date" содержит только 1 строку с датой обновления данных и курсами валют.

Скриншоты получившихся дашбордов:

<code>[Power BI](https://github.com/timurborisevich/DataLearn/blob/main/Module_03/DataLearn.pbix "")</code>

