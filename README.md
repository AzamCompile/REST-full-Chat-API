# Chat API (Django REST Framework)

A RESTful Chat API built with **Django**, **Django REST Framework**, and **PostgreSQL**. This project demonstrates authentication, chat room management, messaging, filtering, searching, pagination, and JWT-based authorization.

## Features

* JWT Authentication
* User Registration
* Chat Rooms
* Messages
* CRUD Operations
* Search & Filtering
* Pagination
* Ordering
* PostgreSQL Database
* RESTful API
* Environment Variables (.env)

## Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* Simple JWT
* Django Filter

## Project Structure

```text
chat_api/
│
├── accounts/
├── chat/
├── config/
├── manage.py
├── requirements.txt
└── .env.example
```

## Installation

Clone the repository:

```bash
git clone https://github.com/AzamCompile/REST-full-Chat-API.git
cd chat-api
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

**Windows**

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=chat_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

## API Endpoints

### Authentication

* POST `/api/accounts/register/`
* POST `/api/token/`
* POST `/api/token/refresh/`

### Chat

* GET `/api/chat/rooms/`
* POST `/api/chat/rooms/`

### Messages

* GET `/api/chat/messages/`
* POST `/api/chat/messages/`
* PUT `/api/chat/messages/{id}/`
* DELETE `/api/chat/messages/{id}/`

## Search

```text
GET /api/chat/messages/?search=hello
```

## Filter

```text
GET /api/chat/messages/?room=1
GET /api/chat/messages/?sender=2
```

## Ordering

```text
GET /api/chat/messages/?ordering=-created_at
```

## Pagination

```text
GET /api/chat/messages/?page=2
```

## Future Improvements

* WebSocket (Django Channels)
* Private Chat
* Group Chat
* File & Image Upload
* Read/Unread Status
* Online Users
* Docker
* Redis
* Celery
* Swagger/OpenAPI
* Unit Tests

## License

This project is intended for learning and portfolio purposes.
