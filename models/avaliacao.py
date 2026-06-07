class Avaliacao:
    def __init__(self, paciente, medico, consulta, nota, comentario):
        if not consulta.esta_realizada():
            raise ValueError("erro: Só é possivel avaliar uma consulta realizada!")
        
        self.__paciente = paciente
        self.__medico = medico
        self.__consulta = consulta
        self.__nota = None
        self.__comentario = None
        
        self.nota = nota
        self.comentario = comentario
    
    @property
    def paciente(self):
        return self.__paciente
    
    @property
    def medico(self):
        return self.__medico
    
    @property
    def consulta(self):
        return self.__consulta
    
    @property
    def nota(self):
        return self.__nota
    
    @nota.setter
    def nota(self, nota):
        if not self.validar_nota(nota):
            raise ValueError("erro: A nota deve ser um número inteiro entre 1 e 5!")
        self.__nota = int(nota)
    
    @property
    def comentario(self):
        return self.__comentario
    
    @comentario.setter
    def comentario(self, comentario):
        if not self.validar_comentario(comentario):
            raise ValueError("erro: O comentário não pode estar vazio!")
        self.__comentario = comentario.strip()

    def validar_nota(self, nota):
        try:
            nota = int(nota)
            return 1 <= nota <= 5
        except ValueError:
            return False
    
    def validar_comentario(self, comentario):
        return isinstance(comentario, str) and comentario.strip() != ""
    
    def exibir_avaliacao(self):
        print(f"Avaliação de {self.paciente.nome} para Dr(a). {self.medico.nome}:")
        print(f"Nota: {self.nota}/5")
        print(f"Comentário: {self.comentario}")

    def __str__(self):
        return f"Avaliação de {self.paciente.nome} para Dr(a). {self.medico.nome}: Nota {self.nota}/5 - {self.comentario}"
    
    def to_dict(self):
        return {
            "paciente_cpf": self.paciente.cpf,
            "medico_crm": self.medico.crm,
            "consulta_data": self.consulta.data,
            "consulta_horario": self.consulta.horario,
            "nota": self.nota,
            "comentario": self.comentario
        }