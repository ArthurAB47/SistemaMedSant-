from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nome, cpf, email, senha):
        self.__nome = None
        self.__cpf = None
        self.__email = None
        self.__senha = None

        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senha = senha

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if not self.validar_nome(nome):
            raise ValueError("erro: O nome não pode estar vazio!")
        self.__nome = nome.strip()

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        if not self.validar_cpf(cpf):
            raise ValueError("erro: O CPF deve ter exatamente 11 digitos!")
        self.__cpf = cpf

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        if not self.validar_email(email):
            raise ValueError("erro: O email deve conter '@' e '.'!")
        self.__email = email.strip()

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        if not self.validar_senha(senha):
            raise ValueError("erro: A senha deve ter pelo menos 6 caracteres!")
        self.__senha = senha

    def validar_nome(self, nome):
        return isinstance(nome, str) and nome.strip() != ""
    
    def validar_cpf(self, cpf):
        return isinstance(cpf, str) and cpf.isdigit() and len(cpf) == 11
    
    def validar_email(self, email):
        if not isinstance(email, str):
            return False
        
        email = email.strip()
        partes = email.split("@")

        return(
            email != ""
            and len(partes) == 2
            and partes[0] != ""
            and partes[1] != ""
            and "." in partes[1]
        )
    
    def validar_senha(self, senha):
        return isinstance(senha, str) and len(senha) >= 6
    
    @abstractmethod
    def exibir_dados(self):
        pass