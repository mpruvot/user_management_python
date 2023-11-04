# User Management System in Python

**IMPORTANT:** I'm building this project using only the core Python libraries, avoiding any external dependencies.

## Overview

I've embarked on a journey to reconstruct a `user management` system from scratch in Python. The first milestone in this project is to establish a user management functionality that is both efficient and scalable.

## The UsersManager Class

The `UsersManager` class is the cornerstone of my system, tasked with the comprehensive management of users.

### Instance Variables
- `user_list`: Begins empty and will be populated with user instances as they are created.

### Enums
I've introduced a `UserType` enum to differentiate between user roles such as admin and visitor. Enums are a neat feature in Python, and I delved into them with the help of the [Python Enum documentation](https://docs.python.org/fr/3/library/enum.html).

### Methods to Implement

1. `new(self, user_type: UserType, name: str) -> User`: This method is crucial for creating and adding a new user to the `user_list`, ensuring no duplicates.
    - **Exception**: `UserAlreadyExist`
    
2. `delete(self, user_type: UserType, name: str) -> None`: This method allows for the removal of a user.
    - **Exception**: `UserNotFound`

3. `get(self, user_type: UserType, name: str) -> User`: This method fetches a user from the list.
    - **Exception**: `UserNotFound`

4. `all(self) -> list[User | None]`: Returns a list of all users.

5. `get_by_type(self, type: UserType) -> list[User]`: Retrieves all users of a specified type.

6. `add(self, user: User) -> None`: Adds a new user to the list.

7. `multiple_add(self, users: list[User])`: Adds multiple users to the list at once.

## The User Class

I've also designed the `User` class to represent individual users.

### Instance Variables
- `name`
- `type`: Corresponds to the `UserType` enum.

### Properties
- `is_admin`: A boolean property that returns `true` if the user is an admin. I learned about properties from [this Python property resource](https://realpython.com/python-property/).

### Methods to Implement
- `__str__`
- `__gt__`
- `__lt__`
- `__eq__`

For comparison methods, I've established that an admin is always greater than a visitor.

---

