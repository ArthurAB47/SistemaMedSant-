class Agenda:
    def __init__(self, medico):
        self.__medico = medico
        self.__horarios_disponiveis = []
        self.__consultas_marcadas = []

    @property
    def medico(self):
        return self.__medico

    @property
    def horarios_disponiveis(self):
        return self.__horarios_disponiveis.copy()

    @property
    def consultas_marcadas(self):
        return self.__consultas_marcadas.copy()

    def adicionar_horario(self, data, horario):
        horario_disponivel = (data.strip(), horario.strip())

        if horario_disponivel in self.__horarios_disponiveis:
            raise ValueError("erro: Esse horário já está disponível na agenda!")

        self.__horarios_disponiveis.append(horario_disponivel)

    def remover_horario(self, data, horario):
        horario_disponivel = (data.strip(), horario.strip())

        if horario_disponivel not in self.__horarios_disponiveis:
            raise ValueError("erro: Horário não encontrado na agenda!")

        self.__horarios_disponiveis.remove(horario_disponivel)

    def verificar_disponibilidade(self, data, horario):
        horario_disponivel = (data.strip(), horario.strip())
        return horario_disponivel in self.__horarios_disponiveis

    def adicionar_consulta(self, consulta):
        horario_consulta = (consulta.data, consulta.horario)

        if horario_consulta not in self.__horarios_disponiveis:
            raise ValueError("erro: Horário não disponível para agendamento!")

        self.__consultas_marcadas.append(consulta)
        self.__horarios_disponiveis.remove(horario_consulta)

    def remover_consulta(self, consulta):
        if consulta not in self.__consultas_marcadas:
            raise ValueError("erro: Consulta não encontrada na agenda!")

        self.__consultas_marcadas.remove(consulta)
        consulta.alterar_status("cancelada")

        horario_liberado = (consulta.data, consulta.horario)
        self.__horarios_disponiveis.append(horario_liberado)

    def listar_horarios_disponiveis(self):
        if len(self.__horarios_disponiveis) == 0:
            print("Não há horários disponíveis na agenda.")
        else:
            print("Horários disponíveis:")
            for data, horario in self.__horarios_disponiveis:
                print(f"{data} às {horario}")

    def listar_consultas_marcadas(self):
        if len(self.__consultas_marcadas) == 0:
            print("Não há consultas marcadas na agenda.")
        else:
            print("Consultas marcadas:")
            for consulta in self.__consultas_marcadas:
                print(consulta)