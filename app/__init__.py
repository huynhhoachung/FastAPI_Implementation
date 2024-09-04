from fastapi import FastAPI
from .routes import user, company, task

# Create the FastAPI app
app = FastAPI()

# Include the routers from the routes module
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(company.router, prefix="/companies", tags=["companies"])
app.include_router(task.router, prefix="/tasks", tags=["tasks"])

# Define a simple root endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}