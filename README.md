# Healthcare User Management System

A Django REST Framework application for user signup and login with role-based dashboards for Patients and Doctors.

## Features

- User signup with profile picture and address
- User login with token authentication
- Role-based dashboards (Patient and Doctor)
- Password confirmation validation
- User filtering and search capabilities
- RESTful API endpoints

## User Types

1. **Patient** - Regular users who can sign up and access patient dashboard
2. **Doctor** - Medical professionals who can sign up and access doctor dashboard

## Signup Fields

- First Name
- Last Name
- Profile Picture (optional)
- Username
- Email ID
- Password
- Confirm Password
- Address (Line 1, City, State, Pincode)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd BANAO
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/`

## API Endpoints

### Authentication

- **POST** `/api/signup/` - User signup
- **POST** `/api/login/` - User login

### Dashboards

- **GET** `/api/patient/dashboard/` - Patient dashboard (requires authentication)
- **GET** `/api/doctor/dashboard/` - Doctor dashboard (requires authentication)

### User Management

- **GET** `/api/users/` - List all users with filtering (requires authentication)

## API Usage Examples

### Signup

```bash
POST /api/signup/
Content-Type: application/json

{
  "first_name": "John",
  "last_name": "Doe",
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepassword123",
  "confirm_password": "securepassword123",
  "user_type": "patient",
  "address": {
    "line1": "123 Main Street",
    "city": "New York",
    "state": "NY",
    "pincode": "10001"
  }
}
```

### Login

```bash
POST /api/login/
Content-Type: application/json

{
  "username": "johndoe",
  "password": "securepassword123"
}
```

Response includes:
- `token` - Authentication token (use in subsequent requests)
- `redirect_url` - Dashboard URL based on user type

### Access Dashboard

```bash
GET /api/patient/dashboard/
Authorization: Token <your-token-here>
```

or

```bash
GET /api/doctor/dashboard/
Authorization: Token <your-token-here>
```

### Filter Users

```bash
GET /api/users/?user_type=patient
GET /api/users/?search=john
GET /api/users/?ordering=-created_at
```

## Project Structure

```
healthcare_project/
├── accounts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py          # User, Patient, Doctor, Address models
│   ├── serializers.py     # API serializers
│   ├── urls.py            # App URL routing
│   └── views.py           # API views
├── healthcare_project/
│   ├── __init__.py
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL routing
│   ├── wsgi.py
│   └── asgi.py
├── manage.py
├── requirements.txt
└── README.md
```

## Models

- **User**: Custom user model extending AbstractUser with user_type and profile_picture
- **Address**: One-to-one relationship with User, stores address details
- **Patient**: Profile model for patients
- **Doctor**: Profile model for doctors

## Security Features

- Password validation
- Token-based authentication
- CORS configuration
- Production-ready security settings

## Deployment

### Environment Variables

For production, set the following environment variables:

```bash
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com
```

### Production Settings

The project includes production-ready security settings that activate when `DEBUG=False`:
- SSL redirect
- Secure cookies
- XSS protection
- Content type nosniff

### Static Files

Collect static files for production:

```bash
python manage.py collectstatic
```

## Testing

You can test the API using:

- **Postman**
- **curl**
- **Django REST Framework browsable API** (available at endpoints when DEBUG=True)

## Admin Panel

## Sample Testing outputs

<img width="1920" height="1080" alt="Screenshot (234)" src="https://github.com/user-attachments/assets/6b493a8f-0f7d-4f21-8f4a-de172aa2d380" />


Access the Django admin panel at `/admin/` after creating a superuser.

## License

This project is open source and available for use.

