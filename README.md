# Listify Todo App

## Description

Listify is a simple and efficient Todo application built with FastAPI, PostgreSQL, and Docker. It allows users to create, read, update, and delete tasks seamlessly. The app is designed to be user-friendly and serves as a great starting point for learning FastAPI and modern web development practices.

## Features

- Create, read, update, and delete tasks
- Dockerized for easy deployment
- PostgreSQL as the database

## Technologies Used

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **Containerization**: Docker
- **ORM**: SQLAlchemy
- **Pydantic**: Data validation and settings management

## Getting Started

### Prerequisites

- Python 3.8 or higher
- PostgreSQL
- Docker (optional, for containerization)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/abynxv/Listify-TodoApp.git
   cd Listify-TodoApp
2. Set up your virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the required packages:

   ```bash
   pip install -r requirements.txt

4. Configure your database settings in settings.py:

   ```python
   DATABASE_URL = "postgresql://username:password@localhost/Listify"
   Replace username, password, and Listify with your actual PostgreSQL credentials and database name.

Running the Application

You can run the application using Docker or directly with Python.
Using Docker

    Build and run the Docker container:
    
    bash

    sudo docker build -t fastapi-todo-app .
    sudo docker run -d --network host --name my_fastapi_app -e DATABASE_URL="postgresql://username:password@localhost/Listify" fastapi-todo-app

    Access the application at http://localhost:8000.

Running Locally

    Start the FastAPI server:

    bash

    uvicorn app.main:app --reload

    Access the application at http://localhost:8000.

API Endpoints

    GET /todos: Get a list of all tasks
    POST /todos: Create a new task
    GET /todos/{id}: Get a task by ID
    PUT /todos/{id}: Update a task by ID
    DELETE /todos/{id}: Delete a task by ID

![Screenshot from 2024-10-30 17-41-52](https://github.com/user-attachments/assets/f650e8d9-39ce-465b-b8d2-801ba835b5de)

