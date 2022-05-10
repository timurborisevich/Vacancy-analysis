# Анализ вакансий

<code>[Документация по API HH](https://github.com/hhru/api)

Для хранения полученных с HH данных понадобится база данных. Схема БД:

<code>![DB Scheme](https://github.com/timurborisevich/Vacancy-analysis/blob/master/DB_scheme.PNG "")</code>

1. Таблица "Vacancies_for_load" содержит список id вакансий, по которым далее будут выполняться точечные запросы. 
Заполняется на первой итерации.
2. Таблица "Vacancies" - основная таблица для анализа. Содержит список вакансий c загруженными атрибутами с HH. 
Также хранит в себе дату обновления данных и курс валюты из вакансии на данную дату.
3. Таблица "Vacancies_key_skills" содержит список ключевых навыков по каждой вакансии. 
Связь записей между таблицами "Vacancies" и "Vacancies_key_skills" = 1 ко многим.

<code>[Отчет Power BI](https://github.com/timurborisevich/DataLearn/blob/main/Module_03/Vacancies_analysis.pbix "")</code>

Скриншоты дашбордов:

<code>![Scrin1](https://github.com/timurborisevich/Vacancy-analysis/blob/master/Scrin1.PNG "")</code>

<code>![Scrin2](https://github.com/timurborisevich/Vacancy-analysis/blob/master/Scrin2.PNG "")</code>
