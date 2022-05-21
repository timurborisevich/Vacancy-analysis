-- ************************************** Vacancies_key_skills
drop table if EXISTS "public".Vacancies_for_load CASCADE

CREATE TABLE Vacancies_for_load
(
  "id" 			varchar(12) NOT null,
  vacancy_type  varchar(100) NOT NULL
);

truncate table "public".Vacancies_for_load

select * from "public".Vacancies_for_load limit 10 

-- ************************************** "public".Vacancies
drop table if EXISTS "public".Vacancies cascade

CREATE TABLE "public".Vacancies
(
 "id"             	varchar(12) NOT NULL,
 vacancy_type     	varchar(100) NOT NULL,
 name             	varchar(300) NOT NULL,
 update_date      	date NULL,
 schedule         	varchar(50) NULL,
 experience       	varchar(50) NULL,
 area_name        	varchar(150) NULL,
 url              	varchar(200) NULL,
 employment       	varchar(100) NULL,
 salary_from      	numeric NULL,
 salary_to        	numeric NULL,
 salary_currency 	varchar(5) NULL,
 currency_exchange	numeric NULL,
 salary_gross     	boolean NULL,
 archived         	boolean NULL,
 created_date     	date NULL,
 published_date   	date NULL,
 employer_name     	varchar(200) NULL,
 employer_url     	varchar(200) NULL,
 employer_trusted 	boolean NULL,
 status           	varchar(50) NULL,
 has_test         	boolean NULL,
 premium          	boolean NULL
);

CREATE INDEX vacancies_id_idx ON public.vacancies (id);
CREATE INDEX vacancies_vacancy_type_idx ON public.vacancies (vacancy_type);

truncate table "public".Vacancies

select * from "public".Vacancies limit 10 


-- ************************************** Vacancies_key_skills
drop table if EXISTS "public".Vacancies_key_skills CASCADE

CREATE TABLE Vacancies_key_skills
(
  "id" 			varchar(12) NOT null,
  vacancy_type  varchar(100) NOT NULL,
  name 			varchar(300) NOT NULL
);

CREATE INDEX vacancies_key_skills_id_idx ON public.vacancies_key_skills (id);
CREATE INDEX vacancies_key_skills_vacancy_type_idx ON public.vacancies_key_skills (vacancy_type);

truncate table "public".Vacancies_key_skills

select * from "public".Vacancies_key_skills limit 10 

