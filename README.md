## User Management

**IMPORTANT : Aucune librairie externe autorisée.**

Nous allons progressivement recoder `user_management` en Python. Nous allons commencer par la gestion des utilisateurs.

### UsersManager

Tout d'abord, créez une classe `UsersManager` qui représente la gestion de l'ensemble de nos utilisateurs.

#### Variables d'instance
- `user_list`: Sera vide à l'instanciation.

#### Enums
Créez un enum `UserType` pour représenter les types d'utilisateurs (par exemple, admin et visiteur).  
*(cf [Python Enum documentation](https://docs.python.org/fr/3/library/enum.html))*

#### Méthodes à implémenter

1. `new(self, user_type: UserType, name: str) -> User`: Crée un nouvel utilisateur, l'ajoute à `user_list`, et le retourne. Pas de doublon autorisé.  
    - **Exception**: `UserAlreadyExist`
    
2. `delete(self, user_type: UserType, name: str) -> None`: Supprime l'utilisateur.  
    - **Exception**: `UserNotFound`

3. `get(self, user_type: UserType, name: str) -> User`: Retourne l'utilisateur demandé.  
    - **Exception**: `UserNotFound`

4. `all(self) -> list[User | None]`: Retourne tous les utilisateurs.

5. `get_by_type(self, type: UserType) -> list[User]`: Retourne tous les utilisateurs de ce type.
x
6. `add(self, user: User) -> None`: Ajoute l'utilisateur à la liste.

7. `multiple_add(self, users: list[user])`: Ajoute les utilisateurs à la liste.

### User

Ensuite, nous allons nous occuper de la classe `User`.

#### Variables d'instance
- `name`
- `type`: de type `UserType`

#### Properties
- `is_admin`: un booléen qui retourne `true` si `type == UserType.ADMIN`.  
    *(cf [Python Property](https://realpython.com/python-property/))*

#### Méthodes à implémenter
- `__str__`
- `__gt__`
- `__lt__`
- `__eq__`

Pour les méthodes de comparaison, considérez qu'un admin > visiteur.
