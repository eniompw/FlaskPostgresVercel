# Vercel Flask Login

A simple Flask web application with PostgreSQL database integration, designed for deployment on Vercel.

## Live Demo

[w3login.vercel.app](https://w3login.vercel.app)

## Features

- Flask web framework
- PostgreSQL database integration
- User authentication system with session management
- Login/logout functionality
- Flash messages for user feedback
- Secure parameterized SQL queries
- Serverless deployment on Vercel

## Prerequisites

- Python 3.x
- PostgreSQL database
- Vercel account (for deployment)

## Environment Variables

Create a `.env` file or set the following environment variables:

```
POSTGRES_URL=your_postgresql_connection_string
SECRET_KEY=your_secret_key_for_sessions
```

The PostgreSQL connection string should be in the format:
```
postgresql://user:password@host:port/database
```

**Note:** If `SECRET_KEY` is not set, a default development key will be used (not recommended for production).

## Installation

1. Clone the repository:
```bash
git clone https://github.com/eniompw/FlaskPostgresVercel.git
cd FlaskPostgresVercel
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
```bash
export POSTGRES_URL="your_postgresql_connection_string"
export SECRET_KEY="your_secret_key"
```

## Local Development

Run the Flask application locally:
```bash
python app.py
```

Or using Flask CLI:
```bash
flask run
```

## Usage

1. **Initialize the database:**
   - Visit `/create` to create the Users table

2. **Add a test user:**
   - Visit `/insert` to add a test user (Username: Bob, Password: 123)

3. **Login:**
   - Navigate to `/` (home page)
   - Enter credentials (Bob / 123)
   - Click "Login"

4. **After successful login:**
   - You'll be redirected to the success page
   - Your username will be displayed
   - Click "Logout" to end the session

5. **View all users (optional):**
   - Visit `/select` to see all users in the database

## API Endpoints

### Main Routes
- `GET /` - Home page (login interface)
- `POST /login` - Authenticate user credentials
- `GET /success` - Success page (requires active session)
- `GET /logout` - Logout and clear session

### Database Management Routes (for testing/setup)
- `GET /create` - Creates the Users table in the database
- `GET /insert` - Inserts a test user (Bob/123)
- `GET /select` - Retrieves and displays all users

## Database Schema

**Users Table:**
- `Username` VARCHAR(20) - Primary Key
- `Password` VARCHAR(20)

## Deployment

This application is configured for deployment on Vercel using the `vercel.json` configuration file.

```bash
vercel deploy
```

## References

* [Based on Vercel Flask](https://github.com/eniompw/vercel-flask)
* [Based on Flask Login](https://github.com/eniompw/FlaskLogin)
* [PostgreSQL Tutorial](https://www.postgresqltutorial.com/postgresql-python/query/)
* [Flask Postgres](https://github.com/eniompw/FlaskPostgres)

## Security Note

⚠️ This is a demo application. For production use, implement additional security measures:
- **Hash passwords** (use bcrypt or similar) - currently passwords are stored in plain text
- ✅ Parameterized queries are used to prevent SQL injection
- ✅ Session management is implemented
- Add comprehensive input validation and sanitization
- ✅ Environment variables are used for sensitive data
- Implement HTTPS in production
- Add CSRF protection
- Implement rate limiting for login attempts
- Add password strength requirements
- Consider using an ORM like SQLAlchemy
