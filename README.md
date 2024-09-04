# FastAPI Assignment

This project uses the FastAPI library to create a simple and straightforward API system.

### Requirements:

#### Development Guidelines

- Use FastAPI, Uvicorn, SQLAlchemy, and Alembic for this assignment.
- Use PostgreSQL for database storage.
- Feel free to add more features to the application to demonstrate your understanding of the problem and/or framework.

#### Evaluation Criteria

- Understanding of FastAPI components.
- Project structure.
- Application of validation, models, queries, routing, and authorization.
- API route design.

#### Database Tables: The following tables are used in this project:

- **User**: `id`, `email`, `username`, `first_name`, `last_name`, `hashed_password`, `is_active`, `is_admin`
- **Company**: `id`, `name`, `description`, `mode`, `rating`
- **Task**: `id`, `summarize`, `description`, `status`, `priority`

# Project Structure

The overall file structure of the project is as follows:
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

# CRUD and Routes summary

### CRUD Functions:

- **Get a Single Record**: Retrieves a record from the database by its unique ID.
- **Get Multiple Records**: Retrieves a list of records with optional pagination (skip and limit).
- **Create a New Record**: Creates a new record using the provided data and saves it to the database.
- **Update an Existing Record**: Updates an existing record with new data.
- **Delete a Record**: Removes a record from the database.

### User Routes:

- **Create User (POST /users/)**: Creates a new user.
- **Read User (GET /users/{user_id})**: Retrieves a single user by ID.
- **Read Users (GET /users/)**: Retrieves multiple users with optional pagination.
- **Update User (PUT /users/{user_id})**: Updates an existing user.
- **Delete User (DELETE /users/{user_id})**: Deletes a user by ID.

### Company Routes:

- **Create Company (POST /companies/)**: Creates a new company.
- **Read Company (GET /companies/{company_id})**: Retrieves a single company by ID.
- **Read Companies (GET /companies/)**: Retrieves multiple companies with optional pagination.
- **Update Company (PUT /companies/{company_id})**: Updates an existing company.
- **Delete Company (DELETE /companies/{company_id})**: Deletes a company by ID.

### Task Routes:

- **Create Task (POST /tasks/)**: Creates a new task.
- **Read Task (GET /tasks/{task_id})**: Retrieves a single task by ID.
- **Read Tasks (GET /tasks/)**: Retrieves multiple tasks with optional pagination.
- **Update Task (PUT /tasks/{task_id})**: Updates an existing task.
- **Delete Task (DELETE /tasks/{task_id})**: Deletes a task by ID.

# How to use file
