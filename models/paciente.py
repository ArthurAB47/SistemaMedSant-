from models.usuario import Usuario

class Paciente(Usuario):
    def __init__(self, nome, cpf, email, senha, localizacao):
        super().__init__(nome, cpf, email, senha)

        self.__localizacao = None
        self.__consultas = []
        self.__historico_consultas = []

        self.localizacao = localizacao

    @property
    def localizacao(self):
        return self.__localizacao
    
    @localizacao.setter
    def localizacao(self, localizacao):
        if not self.validar_localizacao(localizacao):
            raise ValueError("erro: A localização não pode estar vazia!")
        self.__localizacao = localizacao.strip()

    @property
    def consultas(self):
        return self.__consultas.copy()
    
    @property
    def historico_consultas(self):
        return self.__historico_consultas.copy()
    
    def validar_localizacao(self, localizacao):
        return isinstance(localizacao, str) and localizacao.strip() != ""

    def visualizar_consultas(self):
        if len(self.__consultas) == 0:
            print("O paciente não possui nenhuma consulta agendada!")
        else:
            print("Consultas agendadas:")
            for consulta in self.__consultas:
                print(consulta)

    def visualizar_historico(self):
        if len(self.__historico_consultas) == 0:
            print("O paciente não possui historico de consultas!")
        else:
            print("Historico de consultas:")
            for consulta in self.__historico_consultas:
                print(consulta)
    
    def exibir_dados(self):
        print("Dados de paciente:")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Email: {self.email}")
        print(f"Localização: {self.localizacao}")