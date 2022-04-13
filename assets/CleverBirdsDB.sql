CREATE DATABASE CleverBirds_SIMPLEDB;
USE CleverBirds_SIMPLEDB;

CREATE TABLE TB_Music (
Mus_Id int identity(1,1),
Mus_Name varchar (300) not null,
Mus_Lenght int not null,
Mus_Artist varchar (100) not null,
Mus_Licence varchar (100) not null,
constraint PK_Music primary key clustered (Mus_Id)
); 

CREATE TABLE TB_User (
U_Id int identity(1,1), 
U_Name varchar unique not null,
U_Username varchar unique not null,
U_Password varchar (100) not null,
U_Email varchar (100) not null,
U_Score varchar (100),
U_CharacterName varchar (100) not null, 
U_Gender varchar (100) not null, 
constraint PK_User primary key clustered (U_Id),
); 

CREATE TABLE TB_Game_Instance (
GaI_Id int identity (1,1),
GaI_User_Id int not null,
GaI_date date not null,
constraint PK_Game_Instance primary key clustered (GaI_Id),
constraint FK_Game_Instance_Player foreign key (GaI_User_Id) references TB_User (U_Id),
);



/* 1- constraint para foreign key: nome das duas tabelas q quero relacionar / foreign key (nome da foreign key) references: a tabela q estou relacionando (o id, q eh a PK da outra tabela)  */
/* 1- constraint para primary key: PK-"o nome da tabela que estou" / primary key clustered(nome da minha PK) */

 
