from fastapi import FastAPI
from .routes import user, company, task
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(company.router, prefix="/companies", tags=["companies"])
app.include_router(task.router, prefix="/tasks", tags=["tasks"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)