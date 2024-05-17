from users import Users,AdminUser,RegularUser,GuestUser
class UsersBuilder:
    def __init__(self, user_type):
        if user_type == "Admin":
            self.user = AdminUser()
        elif user_type == "Regular":
            self.user = RegularUser()
        elif user_type == "Guest":
            self.user = GuestUser()
        else:
            raise ValueError("Invalid user type")

    def with_id(self, id):
        self.user.id = id
        return self

    def with_name(self, name):
        self.user.name = name
        return self

    def with_email(self, email):
        self.user.email = email
        return self

    def with_password(self, password):
        self.user.password = password
        return self

    def with_status(self, status):
        self.user.status = status
        return self

    def build(self):
        if self.user.id is None:
            self.user._gerar_uuid()
        return self.user
