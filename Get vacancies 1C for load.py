from Functions import GetAreas, SaveVacanciesIdForLoad

vacancy_type = 'программист 1С'
text = 'NAME:"1С" AND (программист OR архитектор OR проектировщик OR разработчик)'
areas = GetAreas()

stop_names = ['консультант', 'менеджер', 'аналитик', 'методолог', 'внедрен', 'сопровожден', 'преподаватель',
              'тестировщик', 'битрикс', 'руководитель проект']

SaveVacanciesIdForLoad(text, vacancy_type, areas, stop_names)