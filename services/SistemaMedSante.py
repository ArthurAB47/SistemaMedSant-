from models.paciente import Paciente
from models.medico import Medico
from models.notificacao import Notificacao
from models.avaliacao import Avaliacao

class SistemaMedSante:
    def __init__(self):
        self.__pacientes = []
        self.__medicos = []
        self.__consultas = []
        self.__notificacoes = []

    @property
    def pacientes(self):
        return self.__pacientes.copy()

    @property
    def medicos(self):
        return self.__medicos.copy()

    @property
    def consultas(self):
        return self.__consultas.copy()

    @property
    def notificacoes(self):
        return self.__notificacoes.copy()

    def cadastrar_paciente(self, nome, cpf, email, senha, localizacao):
        paciente = Paciente(nome, cpf, email, senha, localizacao)
        self.__pacientes.append(paciente)
        return paciente

    def cadastrar_medico(self, nome, cpf, email, senha, crm, especialidade, clinica, valor_consulta):
        medico = Medico(nome, cpf, email, senha, crm, especialidade, clinica, valor_consulta)
        self.__medicos.append(medico)
        return medico

    def buscar_medico_por_nome(self, nome):
        medicos_encontrados = []

        for medico in self.__medicos:
            if nome.lower() in medico.nome.lower():
                medicos_encontrados.append(medico)

        return medicos_encontrados

    def buscar_medico_por_especialidade(self, especialidade):
        medicos_encontrados = []

        for medico in self.__medicos:
            if especialidade.lower() == medico.especialidade.lower():
                medicos_encontrados.append(medico)

        return medicos_encontrados

    def buscar_medico_por_localidade(self, localidade):
        medicos_encontrados = []

        for medico in self.__medicos:
            if localidade.lower() in medico.clinica.lower():
                medicos_encontrados.append(medico)

        return medicos_encontrados

    def registrar_consulta(self, consulta):
        if consulta not in self.__consultas:
            self.__consultas.append(consulta)

    def gerar_notificacao(self, paciente, consulta):
        notificacao = Notificacao(paciente, consulta)
        self.__notificacoes.append(notificacao)
        return notificacao

    def avaliar_consulta(self, paciente, medico, consulta, nota, comentario):
        avaliacao = Avaliacao(paciente, medico, consulta, nota, comentario)
        medico.adicionar_avaliacao(avaliacao)
        return avaliacao

    def listar_pacientes(self):
        if len(self.__pacientes) == 0:
            print("Nenhum paciente cadastrado.")
        else:
            print("Pacientes cadastrados:")
            for paciente in self.__pacientes:
                paciente.exibir_dados()

    def listar_medicos(self):
        if len(self.__medicos) == 0:
            print("Nenhum médico cadastrado.")
        else:
            print("Médicos cadastrados:")
            for medico in self.__medicos:
                medico.exibir_dados()

    def listar_consultas(self):
        if len(self.__consultas) == 0:
            print("Nenhuma consulta cadastrada.")
        else:
            print("Consultas cadastradas:")
            for consulta in self.__consultas:
                print(consulta)