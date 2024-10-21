# Task-Manager

## Introduction

This guide provides step-by-step instructions for setting up the backend, along with links to the deployed backend, Swagger documentation, and Redoc.

## Prerequisites

Ensure the following tools are installed on your system:

- **Python 3.12.2**
- **pip** (Python package manager)
- **virtualenv** (optional but recommended)
- **Git** (to clone the repository)

## Getting Started

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/priyanshukatiyar14/Task-Manager.git
cd Task-Manager
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

Create and activate a virtual environment:

On macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory and add the following environment variables:

```
DATABASE_URL=your_database_url_here
ALLOWED_HOSTS=localhost,your_backend_deployed_url
SECRET_KEY=your_secret_key_here
```

Replace `your_database_url_here`, `your_backend_deployed_url`, and `your_secret_key_here` with your actual credentials.

### 5. Apply Migrations

Run the following command to apply the database migrations:

```bash
python manage.py migrate
```

### 6. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Access the project in your web browser at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Deployed Links

- Project Deployed URL: https://task-manager-pyq0.onrender.com
- Swagger Documentation URL: https://task-manager-pyq0.onrender.com/docs/schema/swagger-ui/
- Redoc URL: https://task-manager-pyq0.onrender.com/docs/schema/redoc/

## Task Endpoints

### 1. List and Create Tasks

- **Endpoint**: `/tasks/`
- **Method**: `GET`, `POST`
- **Description**:
  - `GET`: Retrieve a list of all tasks.
  - `POST`: Create a new task.
- **Request Body** (for POST):

```json
{
  "name": "Task Name",
  "description": "Task Description",
  "task_type": "feature" // or "bug"
}
```

- **Responses**:
  - `200 OK`: List of tasks.
  - `201 Created`: Task created successfully.
  - `400 Bad Request`: Validation errors.

### 2. Retrieve, Update, and Delete a Task

- **Endpoint**: `/tasks/<task_id>/`
- **Method**: `GET`, `PUT`, `DELETE`
- **Description**:
  - `GET`: Retrieve a specific task by ID.
  - `PUT`: Update an existing task.
  - `DELETE`: Delete a specific task.
- **Request Body** (for PUT):

```json
{
  "name": "Updated Task Name",
  "description": "Updated Task Description",
  "task_type": "bug" // or "feature"
}
```

- **Responses**:
  - `200 OK`: Task details.
  - `204 No Content`: Task deleted successfully.
  - `404 Not Found`: Task not found.
  - `400 Bad Request`: Validation errors.

### 3. Assign Users to a Task

- **Endpoint**: `/tasks/assign/`
- **Method**: `POST`
- **Description**: Assign one or more users to a specific task.
- **Request Body**:

```json
{
  "task_id": "<task_id>",
  "user_ids": ["<user_id_1>", "<user_id_2>"]
}
```

- **Responses**:
  - `201 Created`: Users assigned successfully.
  - `404 Not Found`: Task not found.
  - `400 Bad Request`: Validation errors.

### 4. Retrieve Tasks for a Specific User

- **Endpoint**: `/tasks/user/<user_id>/`
- **Method**: `GET`
- **Description**: Retrieve all tasks assigned to a specific user.
- **Responses**:
  - `200 OK`: List of tasks assigned to the user.
  - `404 Not Found`: User not found.

## User Endpoints

### 1. List and Create Users

- **Endpoint**: `/users/`
- **Method**: `GET`, `POST`
- **Description**:
  - `GET`: Retrieve a list of all users.
  - `POST`: Create a new user.
- **Request Body** (for POST):

```json
{
  "name": "User Name",
  "email": "user@example.com",
  "mobile_number": "1234567890",
  "role": "developer" // or "manager" or "tester"
}
```

- **Responses**:
  - `200 OK`: List of users.
  - `201 Created`: User created successfully.
  - `400 Bad Request`: Validation errors.

### 2. Retrieve, Update, and Delete a User

- **Endpoint**: `/users/<user_id>/`
- **Method**: `GET`, `PUT`, `DELETE`
- **Description**:
  - `GET`: Retrieve a specific user by ID.
  - `PUT`: Update an existing user.
  - `DELETE`: Delete a specific user.
- **Request Body** (for PUT):

```json
{
  "name": "Updated User Name",
  "email": "updated_user@example.com",
  "mobile_number": "0987654321",
  "role": "tester" // or "manager" or "developer"
}
```

- **Responses**:
  - `200 OK`: User details.
  - `204 No Content`: User deleted successfully.
  - `404 Not Found`: User not found.
  - `400 Bad Request`: Validation errors.

## Models

### Task Model

- `id`: UUID (Primary Key)
- `name`: CharField (Max Length: 255)
- `description`: TextField
- `task_type`: CharField (Choices: `feature`, `bug`)
- `completed_at`: DateTimeField (nullable)
- `status`: CharField (Choices: `pending`, `in_progress`, `completed`)
- `assigned_users`: ManyToManyField (Related to User)
- `created_at`: DateTimeField (Auto Now Add)
- `updated_at`: DateTimeField (Auto Now)

### User Model

- `id`: UUID (Primary Key)
- `name`: CharField (Max Length: 255)
- `email`: EmailField (Unique)
- `mobile_number`: CharField (Unique, Max Length: 15)
- `role`: CharField (Choices: `manager`, `developer`, `tester`)
- `created_at`: DateTimeField (Auto Now Add)
- `updated_at`: DateTimeField (Auto Now)

## Error Handling

All endpoints return appropriate error messages and status codes in case of failures, including validation errors, not found errors, and internal server errors.
