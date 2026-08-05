# Flask Task Manager Rest API

## A fully functioning REST API beginner friendly project built with Flask ,SQlAlchemy, and JWT authentication

This project is a beginner friendly REST API built with Flask that allows users to register, authenticate and manage their own tasks. It handles backend fundamentals such as RESTful API design, CRUD operations, JWT authentication, password hashing, SQLAlchemy ORM, pagiantion, and input validation. Every file in this repositry is expected to work and provides users with a sample .env.example file to create your own secret keys and configuration values.

## Features
- User registration and login
- JWT access and refresh tokens as user logs in
- secure passwrods due to hashing
- create, view, update, and delete tasks
- view, update, and delete users
- user authorization (each user can only interact with their own tasks)
- pagination for retreiving tasks and users
- error handling

## Installation
1. clone the repository
2. create a virtual environment
    #### macOS / linux
    - python3 -m venv .venv
    - source .venv/bin/activate

    #### Windows
    - python -m venv .venv
    - .venv\Scripts\activate
3. install required packages
    - pip install -r requirements.txt
4. create a .env file using .env.example
5. create the database
    - python create_db.py
6. start the application 
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
