from user_facade import UserFacade

def main():
    facade = UserFacade()

    print("Factory Method, Builder, Strategy")
    print("Pattern Strategy")
    print(".")
    
    print("Perfil Admin  strategy bcrypt")
    admin = facade.create_admin(name="belem", email="belem@example.com")
    print(admin.to_json())
    print(".")
    print(".")
    
    print("Perfil RegularUser Strategy Short")
    regular = facade.create_regular_user(name="luciana", email="lucianab@example.com")
    print(regular.to_json())
    print(".")
    print(".")
    
    print("Perfil Guest strategy Bcrypt")
    guest = facade.create_guest(name="edson", email="edson@example.com")
    print(guest.to_json())

if __name__ == "__main__":
    main()
