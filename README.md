# PYTHON - FastAPI API with JWT Authentication, Docker, and Kubernetes

This project is a RESTful API built with FastAPI, featuring authentication using JWT tokens, containerization with Docker, and orchestration using Kubernetes. The API is fully documented using Swagger (OpenAPI).

---

# 📌 Content  

---

## 🏗 Features

- ✅ FastAPI for high-performance APIs 
- ✅ JWT authentication for secure access 
- ✅ Swagger UI for API documentation
- ✅ MySQL as the database
- ✅ Docker & Docker Compose for containerized deployment
- ✅ Kubernetes (K8s) for orchestration

# Project Structure
  ```
- 📦 app
- ┣ 📂 auth # Authentication logic (JWT)
- ┃ ┗ 📜 auth_handler.py
- ┣ 📂 controllers # Business logic controllers
- ┣ 📂 database # Database connection
- ┃ ┗ 📜 db.py
- ┣ 📂 models # SQLAlchemy models
- ┣ 📂 schemas # Pydantic schemas for data validation
- ┣ 📂 services # Service layer for business logic
- ┣ 📂 views # API route handlers
- ┃ ┣ 📜 company_view.py
- ┃ ┣ 📜 branch_view.py
- ┃ ┗ 📜 user_view.py
- ┗ 📜 main.py # FastAPI application entry point
```

- 📦 deployments # Kubernetes deployment configurations 
- 📦 tests # Unit and integration tests 
- 📜 Dockerfile # Docker build file 
- 📜 docker-compose.yml # Docker Compose configuration 
- 📜 requirements.txt # Python dependencies 
- 📜 README.md # Project documentation 

🚀 Getting Started

1️⃣ Install Dependencies
```
pip install -r requirements.txt
```

2️⃣ Run the API Locally
```
uvicorn app.main:app --reload
API will be available at: http://127.0.0.1:8000/docs (Swagger UI).
```

🐳 Running with Docker
Build and run the container:
```
docker-compose up --build
```

🔐 JWT Authentication

🔹 Generate Token
Send a POST request to:

POST /token
```
{
"username": "admin",
"password": "password123"
}
```
The response will contain an access token:
```
{
"access_token": "your.jwt.token",
"token_type": "bearer"
}
```

🔹 Access Protected Routes
Add the token to the request headers:
makefile
Authorization: Bearer your.jwt.token

## 📜 API Endpoints
```
| Method | Endpoint         | Description        | Auth Required |
| ------ | ---------------- | ------------------ | ------------- |
| GET    | `/companies`     | List companies     | ✅ Yes        |
| POST   | `/companies/`    | Create a company   | ✅ Yes        |
| GET    | `/branches/{id}` | Get branch details | ✅ Yes        |
| POST   | `/branches/`     | Create a branch    | ✅ Yes        |
| POST   | `/users/`        | Register a user    | ❌ No         |
| POST   | `/token`         | Get JWT token      | ❌ No         |
```

## 🛠 Technologies Used
 
- **FastAPI** 🚀  
  A modern, fast (high-performance) web framework for building APIs with Python 3.6+.

- **SQLAlchemy** 🛢  
  SQLAlchemy is the Python SQL toolkit and Object-Relational Mapping (ORM) library.

- **Pydantic** ✅  
  Data validation and settings management using Python type annotations.

- **JWT (Python-Jose)** 🔐  
  JSON Web Tokens for secure authentication.

- **Passlib (Bcrypt)** 🔑  
  A password hashing library that uses bcrypt for secure password storage.

- **MySQL** 🗄  
  An open-source relational database management system.

- **Docker & Docker Compose** 🐳  
  Tools for containerizing and managing multi-container applications.

- **Kubernetes** ☸  
  A platform for automating the deployment, scaling, and management of containerized applications.
 

---

---

# CRM API - Customer Relationship Management

The CRM API is a Customer Relationship Management system designed to manage companies, branches, and related data. 
It provides endpoints to create, update, read, and delete records. 
The API is built using FastAPI and is designed to be run inside Docker containers, which are orchestrated using Docker Compose. 
It includes JWT-based authentication for secure access to the endpoints.


## API Endpoints

```
POST: http://localhost:8000/run_tests
Run tests for the application.

POST: http://localhost:8000/createtablesforce
Force the creation of database tables.

POST: http://localhost:8000/companiescadtest
Test API to create sample companies and branches.
```

## Base URL
```
http://127.0.0.1:8000/
The base URL of the FastAPI app running locally.

http://localhost:8000/
Alias for the above base URL.
```

## API Documentation
```
Swagger UI Docs
http://127.0.0.1:8000/docs
http://localhost:8000/docs
Access the auto-generated Swagger UI documentation for the API.
Accessing Resources
Get Company by ID
GET: http://127.0.0.1:8000/items/1
Retrieve details for a company with ID 1.
Docker Commands
Managing Docker Containers
Check Running Containers
docker ps
List all the running Docker containers.

Access the FastAPI Application Container
docker exec -it fastapi_app /bin/bash
Enter the FastAPI container.

Install Test Dependencies
Once inside the container, run:
pip install pytest httpx
Run the tests with:
pytest

Forcefully Stop All Containers
docker stop $(docker ps -q)
Stop all running containers.
```

## Stop and Rebuild Containers
```
docker-compose down --volumes
docker-compose up --build -d
Stop and rebuild the containers in detached mode.
```
 

## Access MySQL Database in Docker
 
```
docker exec -it apicrm_mysql_1 mysql -u root -p
Access MySQL in the container. After entering your password, you can execute SQL commands like:

DROP DATABASE crm_db;
CREATE DATABASE crm_db;
EXIT;
Apply Changes to Running Containers
If containers are already running, apply the changes by running:
docker-compose up -d
This will apply the changes and restart the containers in detached mode.

Show Tables in the Database
docker exec -it apicrm_mysql_1 mysql -u root -ppassword
After logging into MySQL, run:

USE crm_db;
SHOW TABLES;
```
 

## Example - Register a Company

To register a company, send a POST request to the /companies endpoint:

POST: **http://localhost:8000/companies**

## Request body:

```
{
"name": "Tech Corp",
"description": "Innovative technology company"
}
```

This will create a new company record in the database with the specified name and description.

Troubleshooting
If you encounter issues with the containers or database, follow the steps below:

Ensure containers are up and running:
Run docker-compose up -d to start the containers.

## Rebuild containers if needed:

If changes aren’t reflected or you encounter errors, try rebuilding the containers:

```
docker-compose down -v
docker-compose up --build
```

## Access the MySQL database:

If you need to access the database directly, use:
docker exec -it apicrm_mysql_1 mysql -u root -p
This will allow you to execute SQL commands such as creating or deleting databases.

---

## Remove Old Containers and Volumes

If you encounter persistent errors, remove all containers and volumes:

```
docker-compose down -v
Then rebuild the containers:
docker-compose up --build
```


### See images of the project below
- **Image in general**:
---
![Texto alternativo](https://github.com/sovanderlei/apicrm/blob/main/imagem/Swagger.png)
---
![Texto alternativo](https://github.com/sovanderlei/apicrm/blob/main/imagem/Docker.png)
---
![Texto alternativo](https://github.com/sovanderlei/apicrm/blob/main/imagem/ListagemDados.png)
---
![Texto alternativo](https://github.com/sovanderlei/apicrm/blob/main/imagem/tabelasMysql.png)
---


