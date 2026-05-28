from models.usuario import Usuario
from models.consulta import Consulta

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
    
    def marcar_consulta(self, medico, data, horario): #Esse metodo cria um objeto Consulta, dentro da classe Paciente.
        consulta = Consulta(self, medico, data, horario)
        self.__consultas.append(consulta)
        return consulta
    
    def cancelar_consulta(self, consulta): #Esse metodo cancela uma consulta ja marcada, retira a consulta da lista de consultas, e adiciona ela na lista de historico de consultas
        if consulta not in self.__consultas:
            raise ValueError("erro: Consulta não encontrada na lista de consultas do paciente!")

        consulta.alterar_status("cancelada")
        self.__consultas.remove(consulta)
        self.__historico_consultas.append(consulta)

    def remarcar_consulta(self, consulta, nova_data, novo_horario): #Esse metodo vai remarcar uma consulta, ou seja alterar a data e o horario daquela consulta pra novos valores.
        if consulta not in self.__consultas:
            raise ValueError("erro: Consulta não encontrada na lista de consultas do paciente!")

        consulta.data = nova_data
        consulta.horario = novo_horario
        consulta.alterar_status("agendada")

    def exibir_dados(self):
        print("Dados de paciente:")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Email: {self.email}")
        print(f"Localização: {self.localizacao}")