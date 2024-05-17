import uuid
from abc import ABC, abstractmethod

class Users(ABC):
    def __init__(self, id=None, name=None, email=None, password=None, status=None):
        self.id = id 
        self.name = name
        self.email = email
        self.password = password
        self.status = status

    @abstractmethod
    def get_user_type(self):
        pass

    def __str__(self):
        return f"{self.id}, {self.name}, {self.email}, {self.password}, {self.status}, {self.get_user_type()}"
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'status': self.status,
            'user_type': self.get_user_type()
        }
    
    def active_users(self):
        self.status = 'active'
        return self.status
        
    def deactive_users(self):
        self.status = 'disabled'
        return self.status

    def _gerar_uuid(self):
        self.id = str(uuid.uuid4())
        return self.id

    def __eq__(self, other):
        if isinstance(other, Users):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

    def __lt__(self, other):
        return self.name < other.name

class AdminUser(Users):
    def get_user_type(self):
        return "Admin"

class RegularUser(Users):
    def get_user_type(self):
        return "Regular"

class GuestUser(Users):
    def get_user_type(self):
        return "Guest"
