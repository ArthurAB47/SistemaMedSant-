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
        if not self.validar_data(data):
            raise ValueError("erro: Data inválida. Use o formato DD/MM/AAAA!")
        
        if not self.validar_horario(horario):
            raise ValueError("erro: Horário inválido. Use o formato HH:MM!")
        
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

    def validar_data(self, data):
        if not isinstance(data, str):
            return False

        data = data.strip()
        partes = data.split("/")

        if len(partes) != 3:
            return False

        dia = partes[0]
        mes = partes[1]
        ano = partes[2]

        if not dia.isdigit() or not mes.isdigit() or not ano.isdigit():
            return False

        if len(dia) != 2 or len(mes) != 2 or len(ano) != 4:
            return False

        dia = int(dia)
        mes = int(mes)
        ano = int(ano)

        return 1 <= dia <= 31 and 1 <= mes <= 12 and ano > 0
    
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
