from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# Initialize FastAPI application
app = FastAPI(
    title="Task Management API",
    description="A simple REST API for managing tasks using FastAPI",
    version="1.0.0"
)

# Data Models
class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Task title")
    description: Optional[str] = Field(None, max_length=500, description="Task description")
    completed: bool = Field(False, description="Task completion status")

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int = Field(..., description="Unique task identifier")
    created_at: datetime = Field(default_factory=datetime.now, description="Creation timestamp")

# In-memory storage
tasks_db: List[Task] = []
next_id = 1

# TODO: Implement the following endpoints:
# 1. GET /tasks - List all tasks
# 2. POST /tasks - Create a new task
# 3. GET /tasks/{task_id} - Get a specific task
# 4. PUT /tasks/{task_id} - Update a task
# 5. DELETE /tasks/{task_id} - Delete a task
# 6. Add query parameters for filtering by status
# 7. Add query parameters for pagination (skip, limit)
# 8. Add Bearer token authentication

@app.get("/", tags=["root"])
async def read_root():
    """Root endpoint - API is running"""
    return {"message": "Welcome to Task Management API. Visit /docs for documentation."}

# Add your endpoints here
