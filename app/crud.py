from sqlalchemy.orm import Session
from . import models, schemas



# Get a single user by ID
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Get a user by email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Create a new user
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, username=user.username,
                          first_name=user.first_name, last_name=user.last_name,
                          hashed_password=fake_hashed_password, is_active=user.is_active, is_admin=user.is_admin)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Update an existing user
def update_user(db: Session, user_id: int, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db_user.email = user.email
        db_user.username = user.username
        db_user.first_name = user.first_name
        db_user.last_name = user.last_name
        db_user.hashed_password = user.password + "notreallyhashed"
        db_user.is_active = user.is_active
        db_user.is_admin = user.is_admin
        db.commit()
        db.refresh(db_user)
    return db_user

# Delete a user
def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user




# Get a single company by ID
def get_company(db: Session, company_id: int):
    return db.query(models.Company).filter(models.Company.id == company_id).first()

# Get all companies
def get_companies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Company).offset(skip).limit(limit).all()

# Create a new company
def create_company(db: Session, company: schemas.CompanyCreate):
    db_company = models.Company(name=company.name, description=company.description,
                                mode=company.mode, rating=company.rating)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

# Update an existing company
def update_company(db: Session, company_id: int, company: schemas.CompanyCreate):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if db_company:
        db_company.name = company.name
        db_company.description = company.description
        db_company.mode = company.mode
        db_company.rating = company.rating
        db.commit()
        db.refresh(db_company)
    return db_company

# Delete a company
def delete_company(db: Session, company_id: int):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if db_company:
        db.delete(db_company)
        db.commit()
    return db_company



# Get a single task by ID
def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

# Get all tasks
def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Task).offset(skip).limit(limit).all()

# Create a new task
def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(summarize=task.summarize, description=task.description,
                          status=task.status, priority=task.priority)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Update an existing task
def update_task(db: Session, task_id: int, task: schemas.TaskCreate):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task:
        db_task.summarize = task.summarize
        db_task.description = task.description
        db_task.status = task.status
        db_task.priority = task.priority
        db.commit()
        db.refresh(db_task)
    return db_task

# Delete a task
def delete_task(db: Session, task_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task