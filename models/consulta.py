class Consulta:
    def __init__(self, paciente, medico, data, horario):
        self.__paciente = paciente
        self.__medico = medico
        self.__data = None
        self.__horario = None
        self.__local = medico.clinica
        self.__valor = medico.valor_consulta
        self.__status = "agendada"
        self.__observacoes = ""

        self.data = data
        self.horario = horario

    @property
    def paciente(self):
        return self.__paciente

    @property
    def medico(self):
        return self.__medico

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if not self.validar_data(data):
            raise ValueError("erro: A data não pode estar vazia!")
        self.__data = data.strip()

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario):
        if not self.validar_horario(horario):
            raise ValueError("erro: Horário inválido. Use o formato HH:MM!")
        self.__horario = horario.strip()

    @property
    def local(self):
        return self.__local

    @property
    def valor(self):
        return self.__valor

    @property
    def status(self):
        return self.__status

    @property
    def observacoes(self):
        return self.__observacoes

    def validar_data(self, data):
        return isinstance(data, str) and data.strip() != ""

    def validar_horario(self, horario):
        if not isinstance(horario, str):
            return False

        horario = horario.strip()
        partes = horario.split(":")

        if len(partes) != 2:
            return False

        hora = partes[0]
        minuto = partes[1]

        if not hora.isdigit() or not minuto.isdigit():
            return False

        hora = int(hora)
        minuto = int(minuto)

        return 0 <= hora <= 23 and 0 <= minuto <= 59

    def validar_status(self, status):
        status_validos = ["agendada", "cancelada", "confirmada", "realizada"]
        return isinstance(status, str) and status in status_validos

    def alterar_status(self, novo_status):
        if not self.validar_status(novo_status):
            raise ValueError("erro: Status inválido para a consulta!")
        self.__status = novo_status

    def adicionar_observacao(self, observacao):
        if not isinstance(observacao, str) or observacao.strip() == "":
            raise ValueError("erro: Observação inválida. A observação não pode estar vazia!")
        self.__observacoes = observacao.strip()

    def esta_cancelada(self):
        return self.__status == "cancelada"

    def esta_realizada(self):
        return self.__status == "realizada"

    def exibir_dados(self):
        print("Dados da consulta:")
        print(f"Paciente: {self.paciente.nome}")
        print(f"Médico: {self.medico.nome}")
        print(f"Data: {self.data}")
        print(f"Horário: {self.horario}")
        print(f"Local: {self.local}")
        print(f"Valor: R$ {self.valor:.2f}")
        print(f"Status: {self.status}")

        if self.observacoes != "":
            print(f"Observações: {self.observacoes}")

    def __str__(self): #Esse metodo só mostra um resumo em forma de texto da consulta.
        return f"Consulta com Dr(a). {self.medico.nome} em {self.data} às {self.horario} - Status: {self.status}"
    
    def to_dict(self):
        return {
            "paciente_cpf": self.paciente.cpf,
            "medico_crm": self.medico.crm,
            "data": self.data,
            "horario": self.horario,
            "local": self.local,
            "valor": self.valor,
            "status": self.status,
            "observacoes": self.observacoes
        }