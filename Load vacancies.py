from Functions import GetAndWriteVacanciesData, UpdateInfo

vacancy_type = 'программист 1С'
new_load = False
GetAndWriteVacanciesData(vacancy_type, new_load)

update_date = '2022-05-06'
dollar_exchange = 69.4
euro_exchange = 73.25
UpdateInfo(update_date, dollar_exchange, euro_exchange)