$sqlite3 mydb.db  
sqlite3>.quit  

* Foreign keys:  
  PRAGMA foreign_keys=ON  

sqlite3>**create table** clients(  
  client_id integer not null primary key AUTOINCREMENT,  
  lastname varchar(64)  not null,                             --not null meanning mentatory for input  
  firstname varchar(64) not null,  
  address varchar(64),  
  city_state_zip varchar(64)  
);    

sqlite3>__create table__ doctors(  
  doctor_id integer not null primary key AUTOINCREMENT,  
  lastname varchar(64)  not null,  
  firstname varchar(64) not null,  
  specialty varchar(64)  
);  

sqlite3>__alter table__ doctors __add__   address varchar(64)  not null default '' ;    
sqlite3>__alter table__ doctors __add__   city_state_zip varchar(64)  not null default '';    

sqlite3>__create table__ appointments(  
  appoint_id integer not null primary key AUTOINCREMENT,  
  appt_date datetime not null,  
  fk_client_id int not null,                 -- foreign key constraint  
  fk_doctor_id int,                            -- foreign key constraint  
  service varchar(64) not null,  
  seen boolean,  
  FOREIGN KEY (fk_client_id) REFERENCES clients (client_id), -- foreign key constraint  
  FOREIGN KEY (fk_doctor_id) REFERENCES doctors (doctor_id) -- foreign key constraint  
);     

sqlite3>__create table__ bill_items(  
  item_id integer not null primary key AUTOINCREMENT,    -- charge or payment  
  fk_client_id int,                                -- foreign key constraint  
  fk_doctor_id int,                              -- foreign key constraint  
  fk_appoint_id int,                             -- foreign key constraint  
  date     datetime  not null,  
  amount  decimal(8,2) not null,  
  FOREIGN KEY (fk_client_id) REFERENCES clients (client_id), -- foreign key constraint  
  FOREIGN KEY (fk_doctor_id) REFERENCES doctors (doctor_id), -- foreign key constraint  
  FOREIGN KEY (fk_appoint_id) REFERENCES appointments (appoint_id) -- constraint  
);  

sqlite3>.schema  
  to see what tables you have created.  

sqlite3>__insert into__ clients  
  (lastname,firstname,address,city_state_zip)  
   values ('Lee', 'Sophia', NULL, 'Berkeley, CA, 94703');    

sqlite3>__update__ clients __set__ address = '239 Parker St'  __where__ client_id = 1;  

sqlite3>__insert into__ clients  
  (lastname,firstname,address,city_state_zip)  
   values ('Smith', 'Jame', '124 Maple St', 'Albany, CA, 94710');    

sqlite3>__insert into__ clients  
  (lastname,firstname,address,city_state_zip)  
   values ('Bolivar', 'Jose', '2594 Post Ave', 'Berkeley, CA, 94705');    

sqlite3>__select__ * __from__ clients;  
  sqlite> select * from clients;   
1|Lee|Sophia|239 Parker St|Berkeley, CA, 94703  
2|Smith|Jame|124 Maple St|Albany, CA, 94710  
3|Bolivar|Jose|2594 Post Ave|Berkeley, CA, 94705  

sqlite> __select__ lastname __from__ clients __where__ client_id<3;  
Lee  
Smith  

sqlite> __select__ firstname,lastname __from__ clients __where__ client_id=3;  
Jose|Bolivar  

sqlite> __select__ *  __from__ clients __where__ client_id=3;  
3|Bolivar|Jose|2594 Post Ave|Berkeley, CA, 94705  

sqlite> __select__ * __from__ clients __where__ firstname __like__ 'So%';  
1|Lee|Sophia|239 Parker St|Berkeley, CA, 94703  

sqlite> __select__ * __from__ clients __where__ firstname like 'J%' __order by__ lastname;  
3|Bolivar|Jose|2594 Post Ave|Berkeley, CA, 94705  
2|Smith|Jame|124 Maple St|Albany, CA, 94710  


sqlite3>drop table XXX;  

sqlite> __DELETE FROM__ table __WHERE__ condition  

Lecture 2  
-------  
$squlite3 XXX.db  
**select count(*) from** XXX;  

__SELECT__ * __FROM__ department __WHERE__ name = 'cardiac'  
__SELECT__ (name, location) __FROM__ departments  
__SELECT__ * __FROM__ departments __WHERE__ id = 1  


* Example:  
__PRAGMA__ foreign_keys=ON;  

__create table__ pos_strand(  
  seq MEDIUMTEXT  
);  

__create table__ neg_strand(  
  seq MEDIUMTEXT  
);  

__create table__ genes(  
  name varchar(64) NOT NULL PRIMARY KEY,  
  pos_left integer,  
  pos_right integer,  
  strand char(1),  
  length integer,  
  seq text(8196),  
  type varchar(16),  
  subtype varchar(16),  
  reference text(512)  
);  

__create table__ promoters(  
  name varchar(64) NOT NULL PRIMARY KEY,  
  pos_plus1 integer,  
  strand varchar(1),  
  seq text(256),  
  sigma_factor varchar(64),  
  for_gene_type varchar(16)  
);  

__create table__ terminators(  
  terminator_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,  
  pos_left INTEGER,  
  pos_right INTEGER,  
  length INTEGER,  
  strand CHAR(1),  
  seq TEXT(256)  
);  

__create table__ transcript_units(  
  tu_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,  
  name VARCHAR(64) NOT NULL,  
  prom_name VARCHAR(64),  
  fk_gene_name VARCHAR(64),  
  FOREIGN KEY(fk_gene_name)REFERENCES genes(name)  
);  


__.import__ ecoliM54_1string.txt pos_strand  
__.import__ ecoliM54RevComp_1string.txt neg_strand  
__.separator__ ","  
__.import__ genes.csv genes  
__.import__ knownPromoters.csv promoters  
__.import__ knownTerms.csv terminators  
__.import__ tu.csv transcript_units  


__SELECT__ avg(c) __FROM__ (__SELECT__ suject

SELECT	avg(c)	FROM	(SELECT	subject_id,	sum(length_of_stay)	AS	c	FROM

admissions	GROUP	BY	subject_id)
