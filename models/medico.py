from models.usuario import Usuario

class Medico(Usuario):
    def __init__(self, nome, cpf, email, senha, crm, especialidade, clinica, valor_consulta):
        super().__init__(nome, cpf, email, senha)

        self.__crm = None
        self.__especalidade = None
        self.__clinica = None
        self.__valor_consulta = None
        self.__agenda = []
        self.__avaliacoes = []

        self.crm = crm
        self.especialidade = especialidade
        self.clinica = clinica
        self.valor_consulta = valor_consulta

    @property
    def crm(self):
        return self.__crm
        
    @crm.setter
    def crm(self, crm):
        if not self.validar_crm(crm):
            raise ValueError("erro: O CRM não pode estar vazio!")
        self.__crm = crm.strip()

    @property
    def especialidade(self):
         return self.__especalidade
    
    @especialidade.setter
    def especialidade(self, especialidade):
         if not self.validar_especialidade(especialidade):
              raise ValueError("erro: A especialidade não pode estar vazia!")
         self.__especalidade = especialidade.strip()

    @property
    def clinica(self):
         return self.__clinica
    
    @clinica.setter
    def clinica(self, clinica):
        if not self.validar_clinica(clinica):
            raise ValueError("erro: A clinica não pode estar vazia!")
        self.__clinica = clinica.strip()

    @property
    def valor_consulta(self):
        return self.__valor_consulta
    
    @valor_consulta.setter
    def valor_consulta(self, valor_consulta):
        if not self.validar_valor_consulta(valor_consulta):
            raise ValueError("erro: O valor da consulta não pode ser negativo!")
        self.__valor_consulta = valor_consulta

    @property
    def agenda(self):
        return self.__agenda.copy()
    
    @property
    def avaliacoes(self):
        return self.__avaliacoes.copy()
    
    def validar_crm(self, crm):
        return isinstance(crm, str) and crm.strip() != ""
    
    def validar_especialidade(self, especialidade):
        return isinstance(especialidade, str) and especialidade.strip() != ""

    def validar_clinica(self, clinica):
        return isinstance(clinica, str) and clinica.strip() != ""
    
    def validar_valor_consulta(self, valor_consulta):
        return isinstance(valor_consulta, (int, float)) and valor_consulta >= 0
    
    def visualizar_avaliacoes(self):
        if len(self.__avaliacoes) == 0:
            print("O medico ainda não tem nenhuma avaliação!")
        else:
            print("Avaliações recebidas:")
            for avaliacao in self.__avaliacoes:
                print(avaliacao)

    def calcular_media_avaliacoes(self):
        if len(self.__avaliacoes) == 0:
            return 0
        
        soma = 0

        for avaliacao in self.__avaliacoes:
            soma += avaliacao.nota

        return soma / len(self.__avaliacoes)
    
    def confirmar_presenca_paciente(self, consulta):
        if consulta.medico != self:
            raise ValueError("erro: Essa consulta não pertence a este médico!")
        
        consulta.alterar_status("confirmada")

    def encerrar_consulta(self, consulta, observacao):
        if consulta.medico != self:
            raise ValueError("erro: Essa consulta não pertence a este médico!")

        consulta.adicionar_observacao(observacao)
        consulta.alterar_status("realizada")
    
    def exibir_dados(self):
        print("Dados do médico:")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Email: {self.email}")
        print(f"CRM: {self.crm}")
        print(f"Especialidade: {self.especialidade}")
        print(f"Clinica: {self.clinica}")
        print(f"Valor da consulta: R$ {self.valor_consulta:.2f}")