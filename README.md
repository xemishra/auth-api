## Auth API
A JWT-based authentication API built with FastAPI and PostgreSQL.
## Features
- User Registration
- User Login
- JWT Authentication
- Password Hashing
- PostgreSQL Database
- SQLAlchemy ORM
- Alembic Database Migrations
- Environment Variable Support
- Clean Project Structure
- REST API Architecture

## Tech Stack
- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [JWT Authentication](https://www.jwt.io/)
- [Pydantic](https://pydantic.dev/docs/validation/latest/get-started/)

## Installation
### 1. Clone Repository
```bash
git clone https://github.com/xemishra/auth-api.git
cd auth-api
```
### 2. Create Virtual Environment
#### Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```
#### Linux / Mac:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### Environment Variables
This project already includes a `.env.example` file.
Rename it to `.env`:
#### Windows:
```bash
rename .env.example .env
```
#### Linux / Mac:
```bash
mv .env.example .env
```
Then update the values inside .env according to your local setup.
### Database Setup
Run Alembic Migrations
```bash
alembic upgrade head
```
This will create all required database tables.
### Run the Server
```bash
uvicorn app.main:app --reload
```
Server will run at:
```bash
http://127.0.0.1:8000
```
## API Documentation
FastAPI automatically provides interactive API docs.
### Swagger UI:
```bash
http://127.0.0.1:8000/docs
```
### ReDoc:
```bash
http://127.0.0.1:8000/redoc
```
## Authentication Flow
- Register a new user
- Login with credentials
- Receive JWT access token
- Use token to access protected routes
## Example Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `api/auth/register` | Register user |
| POST | `api/auth/login` | User login |
| GET | `/` | Access home page |
### Examples
POST - http://localhost:8000/api/auth/register
Body:
```json
{
    "name": "Shivanand Mishra",
    "email": "user@example.com",
    "password": "example@123",
    "confirm_password": "example@123"
}
```
POST - http://localhost:8000/api/auth/login
Body:
```json
{
    "email": "user@example.com",
    "password": "example@123"
}
```
After successful login, you will receive an access token.
Use this token in the Authorization header to access protected routes such as the home page.
Example:
GET - http://localhost:8000
Authorization: Bearer your_access_token
## Development
### Create New Migration
```bash
alembic revision --autogenerate -m "message"
```
### Apply Migration
```bash
alembic upgrade head
```
## Security Features
- Password hashing using bcrypt
- JWT token authentication
- Environment variable protection
- Database migration management
## Future Improvements
- Refresh Tokens
- Email Verification
- Password Reset
- OAuth Authentication
- Role-Based Access Control
- Docker Support
- CI/CD Pipeline
- Unit Testing
## Author
GitHub: [auth-api](https://github.com/xemishra/auth-api)

## License
This project is open source and available under the MIT License.
