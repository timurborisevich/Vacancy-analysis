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
 "id"             varchar(12) NOT NULL,
 vacancy_type     varchar(100) NOT NULL,
 name             varchar(300) NOT NULL,
 schedule         varchar(50) NULL,
 experience       varchar(50) NULL,
 area_name        varchar(150) NULL,
 url              varchar(200) NULL,
 employment       varchar(100) NULL,
 salary_from      numeric NULL,
 salary_to        numeric NULL,
 salary_currency  varchar(5) NULL,
 salary_gross     boolean NULL,
 archived         boolean NULL,
 created_date     date NULL,
 published_date   date NULL,
 emloyer_name     varchar(200) NULL,
 employer_url     varchar(200) NULL,
 employer_trusted boolean NULL,
 status           varchar(50) NULL,
 has_test         boolean NULL,
 premium          boolean NULL,
 CONSTRAINT PK_8 PRIMARY KEY ( "id" )
);

truncate table "public".Vacancies

select * from "public".Vacancies limit 10 


-- ************************************** Vacancies_key_skills
drop table if EXISTS "public".Vacancies_key_skills CASCADE

CREATE TABLE Vacancies_key_skills
(
  "id" 			varchar(12) NOT NULL,
  vacancy_type  varchar(100) NOT NULL,
  name 			varchar(300) NOT NULL
);

truncate table "public".Vacancies_key_skills

select * from "public".Vacancies_key_skills limit 10 


-- ************************************** "public".Update_date
drop table if EXISTS "public".Update_date cascade

CREATE TABLE "public".Update_date
(
 update_date     date NOT NULL,
 dollar_exchange numeric NULL,
 euro_exchange   numeric NULL
);

truncate table "public".Update_date

select * from "public".Update_date limit 10 