# Python User Management System

This project is a Python-based user management system developed without external libraries.

## Project Details

The system is designed to manage users, with a focus on simplicity and scalability.

## UsersManager Class

`UsersManager` is responsible for user operations within the system.

### Instance Variables
- `user_list`: A list that stores user instances.

### Enums
- `UserType`: An enum to classify user roles.

### Methods
- `new`: Adds a new user, ensuring uniqueness.
  - Raises `UserAlreadyExist` if the user already exists.
- `delete`: Removes a user.
  - Raises `UserNotFound` if the user does not exist.
- `get`: Retrieves a user's details.
  - Raises `UserNotFound` if the user does not exist.
- `all`: Returns a list of all users.
- `get_by_type`: Fetches users of a specific type.
- `add`: Adds a user to the system.
- `multiple_add`: Adds multiple users simultaneously.

## User Class

Represents a user within the system.

### Instance Variables
- `name`: The name of the user.
- `type`: The role of the user, based on `UserType`.

### Properties
- `is_admin`: Indicates if the user is an admin.

### Comparison Methods
Implemented to determine the hierarchy between user roles, with admin being the highest.

---

The system is part of an ongoing learning process in Python programming, emphasizing practical application and understanding of core concepts.
