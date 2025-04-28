# Project Architecture

This directory contains documentation related to the architecture of this Django project, including business logic, data models, and system design.

## Contents

### [Business Logic](./business-logic.md)

Defines the core business logic, model relationships, and business rules of the application, including:
- Core business features
- Model relationships
- Data flow
- Business rules
- User roles and permissions

### [Data Model](./data-model.md)

Contains the Entity Relationship Diagram (ERD) and detailed descriptions of the data model, including:
- Core entities and their attributes
- Relationships between entities
- Data types and constraints

### [System Design](./system-design.md)

Outlines the system design, components, and their interactions, including:
- System architecture
- Component interactions
- Data flow
- Deployment architecture

## Architecture Overview

The application follows a layered architecture with clear separation of concerns:

1. **Presentation Layer**: Handles user interface and user interactions
2. **Business Logic Layer**: Contains the core business rules and logic
3. **Data Access Layer**: Manages data persistence and retrieval
4. **Infrastructure Layer**: Provides cross-cutting concerns like logging, security, etc.

## Design Principles

- **Separation of Concerns**: Each component has a single responsibility
- **Dependency Inversion**: High-level modules don't depend on low-level modules
- **Interface Segregation**: Clients shouldn't depend on interfaces they don't use
- **Single Responsibility**: Each class has only one reason to change
- **Open/Closed**: Software entities should be open for extension but closed for modification

## Technology Stack

- **Backend**: Django 5
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Docker, Nginx, Gunicorn

## Relationship to Knowledge Base

While this documentation is specific to this project's architecture, general Django architecture patterns and best practices can be found in the `../../knowledge/patterns/` directory. 