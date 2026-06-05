# Appointment Management System

## Project Overview

The Appointment Management System is a backend-driven web application developed using Django. The system provides a structured and secure platform for managing clinical appointments, enabling authenticated users to schedule, track, update, and manage appointment records efficiently.

The application focuses on secure appointment lifecycle management, ensuring that users can only access and modify data that they own while maintaining industry-standard security practices.

---

## Key Features

* User authentication and account management
* Appointment creation and scheduling
* Appointment status tracking and management
* Appointment confirmation ticket generation
* Secure session-based authentication
* Object-level ownership validation
* User-specific appointment history
* Responsive interface powered by Bootstrap 5
* CSRF-protected form submissions
* Secure password storage using Django's built-in authentication framework

---

## Technology Stack

### Backend Framework

* Django 6.0
* Python 3.14

### Database

* SQLite3

### Frontend

* Bootstrap 5
* Django Templates

### Architecture Pattern

The project follows the **Model-View-Controller (MVC)** architectural pattern:

* **Models** handle data representation and database interactions.
* **Views** process requests, apply business logic, and generate responses.
* **Templates** provide presentation logic and user interface rendering.

This separation of concerns improves maintainability, scalability, and code organization.

---

## Technical Implementation

### Authentication & Authorization

The application utilizes Django's built-in authentication system for user registration, login, logout, and session management.

Key security controls include:

#### Secure Password Hashing

Passwords are never stored in plaintext. Django automatically applies:

* Salted password hashing
* Industry-standard password hashing algorithms
* Secure password verification mechanisms

This protects user credentials against common attack vectors such as rainbow table attacks and credential exposure.

#### CSRF Protection

All form submissions are protected using Django's Cross-Site Request Forgery (CSRF) middleware.

Benefits include:

* Prevention of unauthorized form submissions
* Validation of request origin
* Protection against forged user actions

#### Object-Level Ownership Verification

Each appointment is associated with its creator.

Before any appointment is viewed, modified, or deleted, the system verifies ownership to ensure:

* Users can only access their own appointments
* Unauthorized data access is prevented
* Data isolation between user accounts is maintained

Example workflow:

1. User authenticates successfully.
2. User creates an appointment.
3. Appointment is linked to the authenticated user.
4. Any future access request verifies ownership before processing.

---

## Session Management

The application uses Django's secure session framework.

Features include:

* Server-side session storage
* Automatic session handling
* Authenticated user persistence
* Secure logout functionality
* Session-based access control

Protected views require authentication before access is granted.

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/abhi-s-aji/appointment-management-system
cd appointment-management-system
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Linux / macOS

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create an Administrative User (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Access the Application

Open your browser and navigate to:

```bash
http://127.0.0.1:8000/
```

---

## Project Structure

```bash
appointment-management-system/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── appointments/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│
├── users/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
└── project/
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    └── asgi.py
```

---

## Security Considerations

The application incorporates several security measures provided by Django and reinforced through application-level validation:

* CSRF protection enabled on all forms
* Secure salted password hashing
* Authentication-required protected routes
* Object-level ownership verification
* Session-based authentication
* Server-side validation of user input
* Prevention of unauthorized appointment access

These controls help ensure confidentiality, integrity, and controlled access to appointment data.

---

## Professional Reflection

This project demonstrates the implementation of a secure and maintainable backend system using Django's proven development framework. By following the MVC architectural pattern, enforcing strong authentication controls, implementing object-level authorization, and leveraging Django's built-in security mechanisms, the system provides a reliable foundation for appointment management workflows.

The architecture emphasizes scalability, separation of concerns, and security best practices, making it suitable as a foundation for future enterprise-level healthcare scheduling and appointment management solutions.
## Security Note

This repository was developed as a learning and portfolio project to demonstrate Django development skills. During development, temporary administrative setup utilities were used to simplify testing and local development. These utilities have since been removed, and the project has been refactored to follow more secure authentication and account-management practices.

The current codebase does not contain hardcoded credentials, automated administrative account creation, or account-promotion logic. This cleanup was performed as part of the project's security review and reflects an important learning step in secure software development.
