# FastAPI TDD Workshop

Welcome to the FastAPI TDD Workshop! This repository contains a sample FastAPI application to demonstrate Test-Driven Development (TDD) practices.

## Overview

This application is a simple FastAPI project that includes endpoints to manage posts. The project demonstrates how to use TDD to build and test FastAPI applications using pytest and SQLite.

## Features

- FastAPI for building APIs
- SQLAlchemy for ORM
- SQLite for the database
- Pytest for testing

## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.10 or higher
- Git

### Clone the Repository

```sh
git clone https://github.com/kumaravelabinbev/fastapi-tdd.git
cd fastapi-tdd
```

### Create and Activate Virtual Environment

**On macOS/Linux:**

```sh
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```sh
python3 -m venv venv
.\venv\Scripts\activate
```

### Install Dependencies

```sh
pip install --upgrade pip
pip install -r requirements.txt
```

## Running the Application

To start the FastAPI application:

```sh
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## Running Tests

To run the tests using pytest:

```sh
pytest
```

This will discover and run all tests in the project.

## Project Structure

```plaintext
fastapi-tdd-workshop/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── ...
├── tests/
│   ├── __init__.py
│   └── conftest.py
├── requirements.txt
├── README.md
└── ...
```

- **app/**: Contains the FastAPI application code.
- **tests/**: Contains the test cases for the application.
- **requirements.txt**: Lists the Python dependencies for the project.
- **README.md**: This file.
