from main import *
from my_exceptions import *
import cmd

manager = UserManager([])

type_mapping = {
    "admin": UserType.ADMIN,
    "guest": UserType.GUEST,
}


def check_user_type(user_type: str):
    if user_type.lower() in ["admin", "guest"]:
        return True
    else:
        return False


class UserManagerShell(cmd.Cmd):
    intro = "Welcome To UserManager: Type help or ? to list commands.\n".center(50)
    prompt = "Please enter a command > "
    file = None

    def do_exit(self, arg):
        "Exit the program"
        print("Thanks for using UserManager ! BYE !")
        return True
    
    def do_quit(self, arg):
        "Exit the program"
        print("Thanks for using UserManager ! BYE !")
        return True

    def do_create(self, arg):
        "Create a new User"

        args = arg.split()

        if len(args) < 2:
            print("Error: Missing arguments. Usage: create [UserType] [name]")
            return
        user_type, name = args
        enum_user_type = type_mapping.get(user_type.lower())
        if check_user_type(user_type):
            try:
                manager.new(enum_user_type, name)
                print(f"{user_type}: {name} succesfully created !")
            except UserAlreadyExistError:
                print(f"{user_type} {name} already exist !")
        else:
            print("Error: Wrong arguments. Expected: [admin] or [guest]")

    def do_list(self, arg):
        "List all Users: if a type is specified, display all Users by Type"

        user_type = arg
        enum_user_type = type_mapping.get(user_type.lower())
        if not arg:
            try:
                list_users = manager.all()
                for i in list_users:
                    print(i.name)
            except EmptyUserListError:
                print("List is Empty !")
        elif check_user_type(user_type):
            try:
                list_by_type = manager.get_by_type(enum_user_type)
                for i in list_by_type:
                    print(i.name)
            except EmptyUserListError:
                print("List is Empty !")
        else:
            print("Error: Wrong arguments. Expected: list [admin] or [guest]")

    def do_delete(self, arg):
        "Delete users by role and name if specified. Otherwise, delete all users from a specified role"
        args = arg.split()
        if len(args) == 2:
            user_type, name = args
        elif len(args) == 1:
            user_type = args[0]
            name = None
        else:
            print(
                "Error: Missing arguments. Usage: delete [UserType] or [UserType][name]"
            )
            return
        enum_user_type = type_mapping.get(user_type.lower())
        if check_user_type(user_type) and name:
            try:
                manager.delete(enum_user_type, name)
                print(f"{user_type}: {name} succefully deleted !")
            except UserNotFoundError:
                print(f"{user_type} {name} does not exist !")
        elif check_user_type(user_type) and not name:
            confirmation = input(
                "Are you sure you want to delete all users of this type? (y/n) > "
            )
            if confirmation.lower() == "y":
                try:
                    manager.delete_by_role(enum_user_type)
                    print(f"All users of type {user_type} succefully deleted !")
                except UserNotFoundError:
                    print(f"No users of type {user_type} found!")
            else:
                print("Operation Cancelled !")
        else: 
            print(
                "Error: Wrong arguments. Usage: delete [UserType] or [UserType][name]"
            )


if __name__ == "__main__":
    UserManagerShell().cmdloop()
