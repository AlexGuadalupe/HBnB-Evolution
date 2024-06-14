# HBnB Evolution

**Group Project : Alexandra Guadalupe, Joshua Maldonado, Emmanuel Torres**

## Introduction

**HBnB Evolution** is a web application designed to facilitate the management of vacation rentals. It allows users to browse, book, and review properties, as well as manage their own listings if they're hosts. The application is built using **Flask**, a lightweight and flexible web framework for Python.

## Project Structure

The project is structured into several tasks, each focusing on a specific aspect of development:

1. **UML Design**: Lay the foundation of the application by creating a Unified Modeling Language (UML) design to visualize the system's structure.
2. **Classes and Business Logic Implementation**: Implement the classes and business logic based on the UML design, ensuring proper functionality and adherence to requirements.
3. **Persistence Implementation**: Design a flexible data management system using an interface-based approach to handle CRUD operations across different entity types.
4. **User Management Endpoints**: Create RESTful endpoints for managing user entities, including operations for creation, retrieval, updating, and deletion.
5. **Country and City Management Endpoints**: Develop endpoints for managing country and city entities, with operations for retrieval, creation, updating, and deletion.
6. **Amenity Management Endpoints**: Implement endpoints for managing amenity entities, providing functionalities for CRUD operations.
7. **Places Management Endpoints**: Create endpoints for managing place entities, allowing operations such as creation, retrieval, updating, and deletion.
8. **Review Management Endpoints**: Implement functionality for managing reviews, including operations for creation, retrieval, updating, and deletion.
9. **Containerize the Application**: Containerize the Flask application using Docker, ensuring consistency and scalability across different environments.

## UML Diagram


## Usage

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/AlexGuadalupe/HBnB-Evolution.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd HBnB-Evolution
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Run the Flask development server**:
    ```bash
    flask run
    ```

2. **Access the application**:
    Open your web browser and navigate to `http://localhost:5000`.

### Running Tests

To run the unit tests for each task, use the following command:
```bash
python3 -m unittest model.tests.test_*filename*

Task Breakdown
1. UML Design

    Lay the foundation of the application by creating a Unified Modeling Language (UML) design to visualize the system's structure.

2. Classes and Business Logic Implementation

    Implement the classes and business logic based on the UML design.
    Ensure proper functionality and adherence to requirements.

3. Persistence Implementation

    Design a flexible data management system using an interface-based approach.
    Handle CRUD operations across different entity types.

4. User Management Endpoints

    Create RESTful endpoints for managing user entities.
    Include operations for creation, retrieval, updating, and deletion.

5. Country and City Management Endpoints

    Develop endpoints for managing country and city entities.
    Provide operations for retrieval, creation, updating, and deletion.

6. Amenity Management Endpoints

    Implement endpoints for managing amenity entities.
    Ensure functionalities for CRUD operations.

7. Places Management Endpoints

    Create endpoints for managing place entities.
    Allow operations such as creation, retrieval, updating, and deletion.

8. Review Management Endpoints

    Implement functionality for managing reviews.
    Include operations for creation, retrieval, updating, and deletion.

9. Containerize the Application

    Containerize the Flask application using Docker.
    Ensure consistency and scalability across different environments.
