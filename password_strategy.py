from abc import ABC, abstractmethod
import bcrypt
import hashlib
import os

class PasswordStrategy(ABC):
    @abstractmethod
    def criptografar(self, senha):
        pass
 

class BcryptStrategy(PasswordStrategy):
    def criptografar(self, senha):
        senha_bytes = senha.encode('utf-8')
        hashed = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())
        return hashed.decode('utf-8')

    def verificar(self, senha, senha_criptografada):
        senha_bytes = senha.encode('utf-8')
        hashed_bytes = senha_criptografada.encode('utf-8')
        return bcrypt.checkpw(senha_bytes, hashed_bytes)
    

class ShortPasswordStrategy(PasswordStrategy):
    def criptografar(self, senha):
        md51 = hashlib.md5()
        md51.update(str(senha).encode())
        hash1 = md51.hexdigest()

        md52 = hashlib.md5()
        md52.update(str(os.getenv('MINHA_CHAVE_SECRETA')).encode())
        hash2 = md52.hexdigest()
        
        md53 = hashlib.md5()
        md53.update(str(os.getenv('MINHA_OUTRA_SECRETA')).encode())
        hash3 = md53.hexdigest()
        return "".join([hash1, hash2, hash3])


class GeneratePassword:
    def __init__(self,strategy):
        self.strategy = strategy
    
    def criptografar(self, senha):
        return self.strategy.criptografar(senha)