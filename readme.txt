api CRM é a abreviatura em inglês de “customer relationship management”,
POST http://localhost:8000/run_tests

create tables
http://localhost:8000/createtablesforce
http://localhost:8000/companiescadtest


http://127.0.0.1:8000/
http://localhost:8000/


http://127.0.0.1:8000/docs
http://localhost:8000/docs


http://127.0.0.1:8000/items/1


docker ps 



 para fazer os testes locais 
 docker exec -it fastapi_app /bin/bash
 pip install pytest httpx
 pytest
 	 
 
  docker exec -it apicrm_fastapi_app_1 /bin/bash

  forçar fechar o projeto no docker 
  docker stop $(docker ps -q)
  docker-compose down --volumes   
  docker-compose up --build -d   
  
  para acessar o banco mysql 
  docker exec -it apicrm_mysql_1 mysql -u root -p
	pode executar os comando sql 
		DROP DATABASE crm_db;
		CREATE DATABASE crm_db;
		EXIT; 
 para sair exit 

Se você já estiver com os containers em execução, basta rodar o comando abaixo para aplicar as mudanças: 
docker-compose up -d


docker exec -it apicrm_mysql_1 mysql -u root -ppassword
USE crm_db;
SHOW TABLES;



Remova Containers e Volumes Antigos
Se o erro persistir, remova tudo e recrie os containers:
docker-compose down -v
docker-compose up --build


exemplo de cadastro de empresas 
POST
http://localhost:8000/companies
{
    "name": "Tech Corp",
    "description": "Empresa de tecnologia inovadora"
}



Fazer Login e Obter o Token JWT
Faça uma requisição POST para /users/ com:
{
  "username": "admin",
  "email": "admin@example.com",
  "password": "123456"
}



http://localhost:8000/docs
http://localhost:8000/general/hello
http://localhost:8000/general/export-sales

















