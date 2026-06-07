class Notificacao:
    def __init__(self, paciente, consulta):
        self.__paciente = paciente
        self.__consulta = consulta
        self.__mensagem = ""
        self.__status = "pendente"  
        self.gerar_mensagem()
    
    @property
    def paciente(self):
        return self.__paciente
    
    @property
    def consulta(self):
        return self.__consulta
    
    @property
    def mensagem(self):
        return self.__mensagem
    
    @property
    def status(self):
        return self.__status
    
    def gerar_mensagem(self):
        self.__mensagem = (
            f"Olá {self.paciente.nome}, sua consulta com Dr(a). {self.consulta.medico.nome} "
            f"está agendada para {self.consulta.data} às {self.consulta.horario}."
            f"Status: {self.consulta.status}."
        )
    
    def enviar(self):
        if self.__status == "pendente":
            print(f"[NOTIFICAÇÃO] Enviada para {self.paciente.nome}: {self.mensagem}")
            self._status = "enviada"
        else:
            print("Notificação já foi enviada anteriormente.")
    
    def marcar_como_lida(self):
        if self._status == "enviada":
            self._status = "lida"
            print("Notificação marcada como lida.")
        else:
            print("Não é possível marcar como lida: notificação não foi enviada ou já está lida.")
