class Avaliacao:
    """Representa uma avaliação feita por um paciente após consulta realizada."""
    
    def __init__(self, paciente, medico, consulta, nota, comentario):
        self._paciente = paciente
        self._medico = medico
        self._consulta = consulta
        self._nota = None
        self._comentario = None
        self.validar_nota(nota)
        self.validar_comentario(comentario)
    
    @property
    def paciente(self):
        return self._paciente
    
    @property
    def medico(self):
        return self._medico
    
    @property
    def consulta(self):
        return self._consulta
    
    @property
    def nota(self):
        return self._nota
    
    @property
    def comentario(self):
        return self._comentario
    
    def validar_nota(self, nota):
        """Valida a nota (deve ser inteiro entre 1 e 5)."""
        try:
            nota_int = int(nota)
            if 1 <= nota_int <= 5:
                self._nota = nota_int
            else:
                raise ValueError("A nota deve estar entre 1 e 5.")
        except ValueError:
            raise ValueError("Nota inválida. Digite um número inteiro de 1 a 5.")
    
    def validar_comentario(self, comentario):
        """Valida se o comentário não está vazio."""
        if comentario and comentario.strip():
            self._comentario = comentario.strip()
        else:
            raise ValueError("O comentário não pode estar vazio.")
    
    def exibir_avaliacao(self):
        return f"Avaliação de {self.paciente.nome} para Dr(a). {self.medico.nome}: Nota {self.nota}/5 - \"{self.comentario}\""
