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
2.Set up your virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3.Install the required packages:

   ```bash
   pip install -r requirements.txt

4.Configure your database settings in settings.py:

   ```python
   DATABASE_URL = "postgresql://username:password@localhost/Listify"
   Replace username, password, and Listify with your actual PostgreSQL credentials and database name.

