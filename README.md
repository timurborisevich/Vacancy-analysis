# Анализ вакансий

### Цель:  
Анализ имеющихсяна рынке труда вакансий по данным HeadHunter для интересующих специальностей.

### Результаты для профессий в сфере 1С:  

[Опубликованный в Power BI отчет](https://app.powerbi.com/view?r=eyJrIjoiN2FmOTk4ZjItOTQzOS00YjNiLTkwZWEtNGRmZTU2YzlkZDIyIiwidCI6ImU4NGU3MzcwLWFlMDUtNDZmZS04MDBmLTk4NjNlYzY1MDViMiIsImMiOjh9&pageName=ReportSection)

[Статья с описанием реализации и результатов](https://infostart.ru/1c/articles/1659077/)

### Прочее:

[Документация по API HH](https://github.com/hhru/api)

Схема БД:
![DB Scheme](https://github.com/timurborisevich/Vacancy-analysis/blob/master/DB_scheme.PNG "")</code>

1. Таблица "Vacancies_for_load" содержит список id вакансий, по которым далее будут выполняться точечные запросы. 
Заполняется на первой итерации.
2. Таблица "Vacancies" - основная таблица для анализа. Содержит список вакансий c загруженными атрибутами с HH. 
3. Таблица "Vacancies_key_skills" содержит список ключевых навыков по каждой вакансии.  

<code>[Power BI Desktop](https://github.com/timurborisevich/DataLearn/blob/main/Module_03/Vacancies_analysis.pbix "")</code>

Скриншоты дашбордов:

![Scrin1](https://github.com/timurborisevich/Vacancy-analysis/blob/master/Scrin1.PNG "")</code>

![Scrin2](https://github.com/timurborisevich/Vacancy-analysis/blob/master/Scrin2.PNG "")</code>
