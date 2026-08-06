# Flask Task Manager REST API

## A fully functioning REST API beginner friendly project built with Flask ,SQLAlchemy, PostgreSQL and JWT authentication

This project is a beginner friendly REST API built with Flask that allows users to register, authenticate and manage their own tasks. It handles backend fundamentals such as RESTful API design, CRUD operations, JWT authentication, password hashing, SQLAlchemy ORM, pagiantion, and input validation. Every file in this repositry is expected to work and provides users with a sample .env.example file to create your own secret keys and configuration values.

## Features
- User registration and login
- JWT access and refresh tokens as user logs in
- Password hashing
- Create, view, update, and delete tasks
- View, update, and delete users
- User authorization (each user can only interact with their own tasks)
- Pagination for retreiving tasks and users
- Error handling

## Installation
1. Clone the repository
2. Create a virtual environment
    #### macOS / linux
    - python3 -m venv .venv
    - source .venv/bin/activate

    #### Windows
    - python -m venv .venv
    - .venv\Scripts\activate
3. Install required packages
    - pip install -r requirements.txt
4. Create a .env file using .env.example
5. Set up PostgreSQL
    - Use psql postgres to connect with Postgresql
    - If you don't already have a Postgresql user, create one with a password: CREATE USER username WITH PASSWORD 'your_password'; 
    - Create task manager database with user as owner: CREATE DATABASE TASK_MANAGER OWNER username;
    - Create the tables: python3 create_db.py
6. Start the application 
    - flask run

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /auth/register | Register users|
| POST | /auth/login | Login to receive access and refresh tokens|
| POST | /auth/refresh | Use refresh token to obtain a new access token | 

#### Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /user/all_users | Get all users in database (only name and email) |
| PATCH | /user/<user_id> | Update user information|
| DELETE | /user/<user_id> | Delete user |

### Tasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /task/my_tasks | Gets all task from current user |
| POST | /task/create | Create a task for user |
| PATCH | task/task_id | Update user tasks |
| DELETE | task/task_id | Delete user task |
