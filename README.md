# HBnB Evolution Project: Part 1 Guide

## Proyecto Grupal

## Autores

- Alexandra Guadalupe ([GitHub](https://github.com/AlexGuadalupe))
- Joshua Maldonado ([GitHub](https://github.com/J-Bunny560))
- Emmanuel Torres ([GitHub](https://github.com/Emahnny))


Diagrama Simple UML:
https://www.mermaidchart.com/app/projects/5c64fbcc-ac6d-44df-a128-d02116d04292/diagrams/a93c32c7-6274-4a94-882d-995d71dfe205/version/v0.1/edit



Welcome to the first leg of our exciting journey - creating our very own web application, HBnB Evolution, modeled after AirBnB using Python and Flask!

## What’s Cooking in Part 1?

### Sketching with UML
- **Objective**: Draw out the backbone of our application using UML (Unified Modeling Language).
- **Goal**: Create architectural blueprints for classes and components interactions.

### Testing Our Logic
- **Objective**: Ensure everything works as planned.
- **Goal**: Create tests for the API and business logic.

### Building the API
- **Objective**: Implement the API using Flask.
- **Goal**: Create an API that integrates with our business logic and file-based persistence.

### File-Based Data Storage
- **Objective**: Start with a file-based system for data storage.
- **Goal**: Choose a format (text, JSON, XML) with future database integration in mind.

### Packaging with Docker
- **Objective**: Containerize the application.
- **Goal**: Use Docker to wrap the app for easy deployment.

## The Three Layers of Our API Cake

1. **Services Layer**: Handles all requests and responses.
2. **Business Logic Layer**: Processes and decision-making.
3. **Persistence Layer**: Manages data storage.

## The Data Model: Key Entities

- **Places**: Characteristics like name, description, address, city, latitude, longitude, host, number of rooms, bathrooms, price per night, max guests, amenities, and reviews.
- **Users**: Owners (hosts) or reviewers (commenters) of places. Attributes include email, password, first name, and last name. A user can be a host for multiple places and can also write reviews for places they don’t own.
- **Reviews**: Represent user feedback and ratings for a place. This is where users share their experiences.
- **Amenities**: Features of places, like Wi-Fi, pools, etc. Users can pick from a catalog or add new ones.
- **Country and City**: Every place is tied to a city, and each city belongs to a country. This is important for categorizing and searching places.

## Business Logic: Rules to Live By

- **Unique Users**: Each user is unique and identified by their email.
- **One Host per Place**: Every place must have exactly one host.
- **Flexible Hosting**: A user can host multiple places or none at all.
- **Open Reviewing**: Users can write reviews for places they don’t own.
- **Amenity Options**: Places can have multiple amenities from a catalog, and users can add new ones.
- **City-Country Structure**: A place belongs to a city, cities belong to countries, and a country can have multiple cities.

## Key Attributes for Entities

- **Unique ID (UUID4)**: Every object - whether it’s a Place, User, Review, Amenity, or City - must have a unique identifier. This ID should be generated using UUID4 to ensure global uniqueness.
- **Creation Date (created_at)**: This attribute will record the date and time when an object is created.
- **Update Date (updated_at)**: Similarly, each object should have an attribute to record the last update made.

## Tasks

### 0. UML Design
- **Objective**: Develop a comprehensive UML diagram including all entities (Places, Users, Reviews, Amenities, Country, City) and their relationships.
- **Goal**: Plan and visualize the system’s structure.

### 1. Classes and Business Logic Implementation
- **Objective**: Implement the classes as per the UML diagram.
- **Goal**: Apply business rules and write unit tests.

### 2. Persistence Implementation
- **Objective**: Design a flexible data management system.
- **Goal**: Develop an interface-based persistence layer and implement a DataManager class.

### 3. Implement the User Management Endpoints
- **Objective**: Create RESTful endpoints for managing user entities.
- **Goal**: Implement routes for adding, retrieving, updating, and deleting users.

### 4. Implement the Country and City Management Endpoints
- **Objective**: Create endpoints for managing Country and City entities.
- **Goal**: Develop endpoints to retrieve pre-loaded country data and manage city entities.

### 5. Implement the Amenity Management Endpoints
- **Objective**: Create endpoints for managing amenities.
- **Goal**: Develop routes for adding, retrieving, updating, and deleting amenities.

### 6. Implement the Places Management Endpoints
- **Objective**: Create endpoints for managing places.
- **Goal**: Develop routes for creating, retrieving, updating, and deleting place entities.

### 7. Implement the Review Management Endpoints
- **Objective**: Create endpoints for managing reviews.
- **Goal**: Develop routes for adding, retrieving, updating, and deleting reviews.

### 8. Containerize the Application
- **Objective**: Containerize the application using Docker.
- **Goal**: Create a Dockerfile, manage application port via environment variables, and implement data persistence.