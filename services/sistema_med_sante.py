import json
from models.paciente import Paciente
from models.medico import Medico
from models.notificacao import Notificacao
from models.avaliacao import Avaliacao
from models.consulta import Consulta

class SistemaMedSante:
    def __init__(self):
        self.__pacientes = []
        self.__medicos = []
        self.__consultas = []
        self.__notificacoes = []

        self.carregar_dados()

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
        self.salvar_dados()
        return paciente

    def cadastrar_medico(self, nome, cpf, email, senha, crm, especialidade, clinica, valor_consulta):
        medico = Medico(nome, cpf, email, senha, crm, especialidade, clinica, valor_consulta)
        self.__medicos.append(medico)
        self.salvar_dados()
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
    
    def buscar_paciente_por_cpf(self, cpf):
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                return paciente
        return None


    def buscar_medico_por_crm(self, crm):
        for medico in self.__medicos:
            if medico.crm == crm:
                return medico
        return None

    def registrar_consulta(self, consulta):
        if consulta not in self.__consultas:
            self.__consultas.append(consulta)
            self.salvar_dados()

    def gerar_notificacao(self, paciente, consulta):
        notificacao = Notificacao(paciente, consulta)
        self.__notificacoes.append(notificacao)
        return notificacao

    def avaliar_consulta(self, paciente, medico, consulta, nota, comentario):
        avaliacao = Avaliacao(paciente, medico, consulta, nota, comentario)
        medico.adicionar_avaliacao(avaliacao)
        self.salvar_dados()
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

    def salvar_pacientes(self):
        with open("database/pacientes.json", "w", encoding="utf-8") as arquivo:
            json.dump([paciente.to_dict() for paciente in self.__pacientes], arquivo, indent=4, ensure_ascii=False)

    def salvar_medicos(self):
        with open("database/medicos.json", "w", encoding="utf-8") as arquivo:
            json.dump([medico.to_dict() for medico in self.__medicos], arquivo, indent=4, ensure_ascii=False)

    def salvar_consultas(self):
        with open("database/consultas.json", "w", encoding="utf-8") as arquivo:
            json.dump([consulta.to_dict() for consulta in self.__consultas], arquivo, indent=4, ensure_ascii=False)

    def salvar_avaliacoes(self):
        avaliacoes = []

        for medico in self.__medicos:
            for avaliacao in medico.avaliacoes:
                avaliacoes.append(avaliacao.to_dict())

        with open("database/avaliacoes.json", "w", encoding="utf-8") as arquivo:
            json.dump(avaliacoes, arquivo, indent=4, ensure_ascii=False)

    def salvar_dados(self):
        self.salvar_pacientes()
        self.salvar_medicos()
        self.salvar_consultas()
        self.salvar_avaliacoes()

    def carregar_pacientes(self):
        try:
            with open("database/pacientes.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            for item in dados:
                paciente = Paciente(
                    item["nome"],
                    item["cpf"],
                    item["email"],
                    item["senha"],
                    item["localizacao"]
                )
                self.__pacientes.append(paciente)

        except FileNotFoundError:
            pass

    def carregar_medicos(self):
        try:
            with open("database/medicos.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            for item in dados:
                medico = Medico(
                    item["nome"],
                    item["cpf"],
                    item["email"],
                    item["senha"],
                    item["crm"],
                    item["especialidade"],
                    item["clinica"],
                    item["valor_consulta"]
                )

                if "horarios_disponiveis" in item:
                    for data, horario in item["horarios_disponiveis"]:
                        medico.cadastrar_horario(data, horario)

                self.__medicos.append(medico)

        except FileNotFoundError:
            pass

    def carregar_consultas(self):
        try:
            with open("database/consultas.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            for item in dados:
                paciente = self.buscar_paciente_por_cpf(item["paciente_cpf"])
                medico = self.buscar_medico_por_crm(item["medico_crm"])

                if paciente is not None and medico is not None:
                    consulta = Consulta(
                        paciente,
                        medico,
                        item["data"],
                        item["horario"]
                    )

                    consulta.alterar_status(item["status"])

                    if item["observacoes"] != "":
                        consulta.adicionar_observacao(item["observacoes"])

                    self.__consultas.append(consulta)

        except FileNotFoundError:
            pass

    def carregar_avaliacoes(self):
        try:
            with open("database/avaliacoes.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            for item in dados:
                paciente = self.buscar_paciente_por_cpf(item["paciente_cpf"])
                medico = self.buscar_medico_por_crm(item["medico_crm"])

                consulta_encontrada = None

                for consulta in self.__consultas:
                    if (
                        consulta.paciente == paciente
                        and consulta.medico == medico
                        and consulta.data == item["consulta_data"]
                        and consulta.horario == item["consulta_horario"]
                    ):
                        consulta_encontrada = consulta

                if paciente is not None and medico is not None and consulta_encontrada is not None:
                    avaliacao = Avaliacao(
                        paciente,
                        medico,
                        consulta_encontrada,
                        item["nota"],
                        item["comentario"]
                    )
                    medico.adicionar_avaliacao(avaliacao)

        except FileNotFoundError:
            pass

    def carregar_dados(self):
        self.carregar_pacientes()
        self.carregar_medicos()
        self.carregar_consultas()
        self.carregar_avaliacoes()