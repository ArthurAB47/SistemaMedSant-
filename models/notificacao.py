class Notificacao:
    """Representa uma notificação enviada ao paciente sobre sua consulta."""
    
    def __init__(self, paciente, consulta):
        self._paciente = paciente
        self._consulta = consulta
        self._mensagem = ""
        self._status = "pendente"   # pendente, enviada, lida
        self.gerar_mensagem()
    
    @property
    def paciente(self):
        return self._paciente
    
    @property
    def consulta(self):
        return self._consulta
    
    @property
    def mensagem(self):
        return self._mensagem
    
    @property
    def status(self):
        return self._status
    
    def gerar_mensagem(self):
        """Gera automaticamente a mensagem com base nos dados da consulta."""
        self._mensagem = (f"Olá {self.paciente.nome}, sua consulta com Dr(a). {self.consulta.medico.nome} "
                          f"está agendada para {self.consulta.data_hora}. Status: {self.consulta.status}.")
    
    def enviar(self):
        """Simula o envio da notificação."""
        if self._status == "pendente":
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
