# 💻 About Project

[Complete Guide | Run this project on your computer](https://github.com/danialafjeh/Run-My-Projects-Locally)

# To-Do List RESTful API

A secure and fully functional To-Do List REST API built with Django REST Framework (DRF). This project demonstrates authentication, authorization, user management, task management, pagination, search functionality, and API documentation using Swagger/OpenAPI.

The API follows a permission-based architecture where users can only access and manage their own resources, while administrators have additional privileges for system-wide management and monitoring.

‼️NOTE: This is a portfolio project and it's not a deployed project. so all information saved in database are available and just for examples! there is no real sensitive info.

---

# Features

## User Management

* User registration endpoint
* User authentication using Token Authentication
* User logout functionality
* Token validation endpoint
* Retrieve authenticated user information
* Update authenticated user profile
* Delete user accounts (Admin only)
* Search users by username (Admin only)
* List all users (Admin only)

---

## Task Management

* Create new tasks
* Retrieve all tasks belonging to the authenticated user
* Retrieve a specific task owned by the authenticated user
* Update tasks owned by the authenticated user
* Delete tasks owned by the authenticated user
* Search tasks by username (Admin only)
* Task ownership enforcement

---

## Authentication & Authorization

The project uses Django REST Framework Token Authentication.

Authentication features include:

* Secure token generation during user registration
* Login endpoint for token retrieval
* Logout endpoint with token invalidation
* Authentication verification endpoint

Authorization rules include:

### Regular Users

* Can view their own profile only
* Can update their own profile only
* Can access their own tasks only
* Can create their own tasks
* Can update their own tasks
* Can delete their own tasks

### Administrators

* Can retrieve the complete user list
* Can search users by username
* Can search tasks across all users
* Can delete user accounts
* Cannot delete their own administrator account
* Cannot delete superuser accounts

---

# Security Features

* Token-based authentication
* Owner-based access control
* Admin-only management endpoints
* Superuser deletion protection
* Administrator self-deletion protection
* Passwords stored securely using Django's password hashing system
* Password field excluded from user serialization output
* Unauthorized access prevention through DRF permission classes

---

# Search Functionality

### User Search

Administrators can search users using partial username matching.

Example:

```http
GET /api/search-user/danial
```

Supports case-insensitive matching.

---

### Task Search

Administrators can search tasks by providing a user's username who has their own tasks to see any user's tasks easily.

Example:

```http
GET /api/search-task/danial
```

Returns tasks belonging to matching users.

---

# Pagination

Pagination is implemented using Django REST Framework's PageNumberPagination.

Benefits:

* Reduced response size
* Improved performance
* Easier client-side navigation
* Scalable data retrieval

Paginated endpoints include:

* User list
* User search
* Task list
* Task search

---

# API Documentation

The project includes automatic API documentation powered by OpenAPI and Swagger UI.
NOTE: Because of using APIView, Swagger may missed some of endpoints in documenting. for better analyzing, please read views.py too.
Available documentation endpoints:

```http
/api/schema/
/api/docs/
```

Swagger UI provides an interactive interface for exploring and testing API endpoints.

---

# Technology Stack

### Backend

* Python
* Django
* Django REST Framework (DRF)

### Authentication

* Token Authentication

### Documentation

* drf-spectacular
* Swagger UI
* OpenAPI Schema

### Database

* SQLite3

---

# Architecture Overview

The project follows a RESTful architecture using:

* APIView-based endpoints
* DRF Serializers
* ModelSerializers
* Permission Classes
* Token Authentication
* Pagination System

The design focuses on clarity, security, and maintainability while demonstrating core backend development concepts.

---

# Main API Capabilities

### Authentication

* Register User
* Login User
* Logout User
* Validate Token

### User Operations

* List Users (Admin)
* Retrieve User Details
* Update User Profile
* Delete User (Admin)
* Search Users (Admin)

### Task Operations

* Create Task
* Retrieve Tasks
* Retrieve Task Details
* Update Task
* Delete Task
* Search Tasks (Admin)

---

# Project Goals

This project was developed to demonstrate practical experience with:

* REST API development
* Django REST Framework
* Authentication systems
* Authorization and permissions
* CRUD operations
* API security
* Pagination
* Search implementation
* API documentation
* User-resource ownership control

---

# Purpose

Developed as a backend learning and portfolio project using Django REST Framework, focusing on secure API development, authentication, authorization, and resource ownership management.

