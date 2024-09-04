# FastAPI Assignment

This project uses the FastAPI library to create a simple and straightforward API system.

# Requirements:

> ### Development Guidelines

- Use FastAPI, Uvicorn, SQLAlchemy, and Alembic for this assignment.
- Use PostgreSQL for database storage.
- Feel free to add more features to the application to demonstrate your understanding of the problem and/or framework.

> ### Evaluation Criteria

- Understanding of FastAPI components.
- Project structure.
- Application of validation, models, queries, routing, and authorization.
- API route design.

> ### Database Tables:

#### The following tables are used in this project:

- **User**: `id`, `email`, `username`, `first_name`, `last_name`, `hashed_password`, `is_active`, `is_admin`
- **Company**: `id`, `name`, `description`, `mode`, `rating`
- **Task**: `id`, `summarize`, `description`, `status`, `priority`

# Project Structure

The overall file structure of the project is as follows:

```
fastapi_project/
├── alembic/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ ├── crud.py
│ ├── database.py
│ ├── deps.py
│ ├── routes/
│ │ ├── init.py
│ │ ├── user.py
│ │ ├── company.py
│ │ ├── task.py
├── alembic.ini
├── requirements.txt
└── README.md
```

# CRUD and Routes summary

> ### CRUD Functions:

- **Get a Single Record**: Retrieves a record from the database by its unique ID.
- **Get Multiple Records**: Retrieves a list of records with optional pagination (skip and limit).
- **Create a New Record**: Creates a new record using the provided data and saves it to the database.
- **Update an Existing Record**: Updates an existing record with new data.
- **Delete a Record**: Removes a record from the database.

> ### User Routes:

- **Create User (POST /users/)**: Creates a new user.
- **Read User (GET /users/{user_id})**: Retrieves a single user by ID.
- **Read Users (GET /users/)**: Retrieves multiple users with optional pagination.
- **Update User (PUT /users/{user_id})**: Updates an existing user.
- **Delete User (DELETE /users/{user_id})**: Deletes a user by ID.

> ### Company Routes:

- **Create Company (POST /companies/)**: Creates a new company.
- **Read Company (GET /companies/{company_id})**: Retrieves a single company by ID.
- **Read Companies (GET /companies/)**: Retrieves multiple companies with optional pagination.
- **Update Company (PUT /companies/{company_id})**: Updates an existing company.
- **Delete Company (DELETE /companies/{company_id})**: Deletes a company by ID.

> ### Task Routes:

- **Create Task (POST /tasks/)**: Creates a new task.
- **Read Task (GET /tasks/{task_id})**: Retrieves a single task by ID.
- **Read Tasks (GET /tasks/)**: Retrieves multiple tasks with optional pagination.
- **Update Task (PUT /tasks/{task_id})**: Updates an existing task.
- **Delete Task (DELETE /tasks/{task_id})**: Deletes a task by ID.

# Setup instructions:

### 1. Clone the Repository

```bash
git clone <repository_url>
cd fastapi_assignment
```

### 2. Create and Activate a Virtual Environment

> #### 2.1 Using the available virtual environment

```bash
#Acivate virtual envirorment

## On Windows
.\venv\Scripts\activate

## On macOS/Linux
source venv/bin/activate
```

> #### 2.2 Create your own new virtual environment

```bash
# Create new virtual envirorment
python -m venv venv
```

```bash
# Activate virtual envirorment

## On Windows
.\venv\Scripts\activate

## On macOS/Linux
source venv/bin/activate
```

```bash
# Install requirements dependencies
pip install -r requirements.txt
```

### 3. Configure PostgreSQL

```PostgreSQL
CREATE DATABASE fastapi_db;
CREATE USER fastapi_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE fastapi_db TO fastapi_user;
```

### 4. Configure Alembic

Fill in your PostgreSQL connection string to initiate and connect

```bash
# alembic.ini
[alembic]
script_location = alembic
sqlalchemy.url = postgresql://fastapi_user:password@localhost/fastapi_db
```

### 5. Initialize Alembic

```bash
alembic init alembic
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

### 6. Running the Application

> #### 6.1 Start the FastAPI Application

```bash
uvicorn app.main:app --reload
```

> #### 6.2 Access the API
>
> Open your browser and navigate to http://127.0.0.1:8000. You should see a JSON response:

```json
{
  "Hello": "World"
}
```

> #### 6.3 Access documentation

- Swagger UI: http://127.0.0.1:8000/docs

- ReDoc: http://127.0.0.1:8000/redoc
