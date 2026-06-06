class Agenda:
    """Agenda de um médico: gerencia horários disponíveis e consultas marcadas."""
    
    def __init__(self, medico):
        self._medico = medico
        self._horarios_disponiveis = []   # lista de strings "DD/MM/AAAA HH:MM"
        self._consultas_marcadas = []     # lista de objetos Consulta
    
    @property
    def medico(self):
        return self._medico
    
    @property
    def horarios_disponiveis(self):
        return self._horarios_disponiveis.copy()
    
    @property
    def consultas_marcadas(self):
        return self._consultas_marcadas.copy()
    
    def adicionar_horario(self, horario):
        """Adiciona um horário à lista de disponíveis."""
        if horario not in self._horarios_disponiveis:
            self._horarios_disponiveis.append(horario)
            print(f"Horário {horario} adicionado à agenda de {self.medico.nome}.")
        else:
            print("Horário já existe na agenda.")
    
    def remover_horario(self, horario):
        """Remove um horário disponível."""
        if horario in self._horarios_disponiveis:
            self._horarios_disponiveis.remove(horario)
            print(f"Horário {horario} removido.")
        else:
            print("Horário não encontrado.")
    
    def verificar_disponibilidade(self, horario):
        """Verifica se um horário está disponível."""
        return horario in self._horarios_disponiveis
    
    def adicionar_consulta(self, consulta):
        """Marca uma consulta: adiciona à lista e remove o horário dos disponíveis."""
        if consulta.data_hora in self._horarios_disponiveis:
            self._consultas_marcadas.append(consulta)
            self._horarios_disponiveis.remove(consulta.data_hora)
            print(f"Consulta agendada para {consulta.data_hora} com Dr(a). {self.medico.nome}.")
        else:
            raise ValueError("Horário não disponível para agendamento.")
    
    def remover_consulta(self, consulta):
        """Cancela uma consulta: remove da lista e devolve o horário aos disponíveis."""
        if consulta in self._consultas_marcadas:
            self._consultas_marcadas.remove(consulta)
            self._horarios_disponiveis.append(consulta.data_hora)
            consulta.status = "cancelada"
            print(f"Consulta de {consulta.data_hora} cancelada. Horário reaberto.")
        else:
            print("Consulta não encontrada na agenda.")
    
    def listar_horarios_disponiveis(self):
        return self._horarios_disponiveis.copy()
    
    def listar_consultas_marcadas(self):
        return [c.exibir_resumo() for c in self._consultas_marcadas]
