import os
from users import Users, AdminUser, RegularUser, GuestUser
from users_builder import UsersBuilder
from password_strategy import GeneratePassword, BcryptStrategy, ShortPasswordStrategy

class UserFacade:
    def __init__(self):
        self.bcrypt_strategy = BcryptStrategy()
        self.short_password_strategy = ShortPasswordStrategy()
    
    def create_admin(self, name, email):
        builder = UsersBuilder("Admin")
        password_gen = GeneratePassword(self.bcrypt_strategy)
        password = password_gen.criptografar(str(os.getenv("PASSWORDADMIN")))
        return builder.with_name(name).with_email(email).with_password(password).with_status("active").build()

    def create_regular_user(self, name, email):
        builder = UsersBuilder("Regular")
        password_gen = GeneratePassword(self.short_password_strategy)
        password = password_gen.criptografar(str(os.getenv("PASSWORDREGULAR")) )
        return builder.with_name(name).with_email(email).with_password(password).with_status("active").build()

    def create_guest(self, name, email):
        builder = UsersBuilder("Guest")
        password_gen = GeneratePassword(self.bcrypt_strategy)
        password = password_gen.criptografar(str(os.getenv("PASSWORDGUEST")))
        return builder.with_name(name).with_email(email).with_password(password).with_status("active").build()
 
