from database.db_manager import DatabaseManager
from models.paciente import Paciente
from models.medico import Medico
from models.consulta import Consulta
from models.agenda import Agenda
from models.notificacao import Notificacao
from models.avaliacao import Avaliacao

class SistemaMedSante:
    """Classe central que gerencia todos os dados do sistema e persistência."""
    
    def __init__(self):
        self.db = DatabaseManager()
        self.pacientes = []
        self.medicos = []
        self.consultas = []
        self.notificacoes = []
        self._carregar_dados()
    
    def _carregar_dados(self):
        """Carrega dados do banco para a memória (reconstroi objetos)."""
        # Carregar médicos
        cursor = self.db.executar("SELECT id, nome, email, telefone, especialidade, crm, localidade FROM medicos")
        if cursor:
            for row in cursor.fetchall():
                medico = Medico(row[1], row[2], row[3], row[4], row[5], row[6])
                medico._id = row[0]   # armazenamento interno
                self.medicos.append(medico)
                # Criar agenda associada
                agenda = Agenda(medico)
                medico.agenda = agenda
                # Carregar horários disponíveis
                cursor_h = self.db.executar("SELECT horario FROM horarios_disponiveis WHERE medico_id=?", (row[0],))
                if cursor_h:
                    for h in cursor_h.fetchall():
                        agenda.adicionar_horario(h[0])
        
        # Carregar pacientes
        cursor = self.db.executar("SELECT id, nome, email, telefone, data_nascimento, endereco FROM pacientes")
        if cursor:
            for row in cursor.fetchall():
                paciente = Paciente(row[1], row[2], row[3], row[4], row[5])
                paciente._id = row[0]
                self.pacientes.append(paciente)
        
        # Carregar consultas (necessita ligar objetos paciente/medico)
        cursor = self.db.executar("SELECT id, paciente_id, medico_id, data_hora, status, observacao FROM consultas")
        if cursor:
            for row in cursor.fetchall():
                paciente = self._buscar_paciente_por_id(row[1])
                medico = self._buscar_medico_por_id(row[2])
                if paciente and medico:
                    consulta = Consulta(paciente, medico, row[3], row[5])
                    consulta.status = row[4]
                    consulta._id = row[0]
                    self.consultas.append(consulta)
                    # Adicionar à agenda do médico se não cancelada
                    if consulta.status != "cancelada":
                        medico.agenda._consultas_marcadas.append(consulta)
        # Notificações e avaliações podem ser carregadas sob demanda, mas simplificamos.
    
    def _buscar_medico_por_id(self, id_):
        for m in self.medicos:
            if hasattr(m, '_id') and m._id == id_:
                return m
        return None
    
    def _buscar_paciente_por_id(self, id_):
        for p in self.pacientes:
            if hasattr(p, '_id') and p._id == id_:
                return p
        return None
    
    def salvar_paciente(self, paciente):
        self.db.executar(
            "INSERT INTO pacientes (nome, email, telefone, data_nascimento, endereco) VALUES (?,?,?,?,?)",
            (paciente.nome, paciente.email, paciente.telefone, paciente.data_nascimento, paciente.endereco)
        )
        self.pacientes.append(paciente)
    
    def salvar_medico(self, medico):
        cursor = self.db.executar(
            "INSERT INTO medicos (nome, email, telefone, especialidade, crm, localidade) VALUES (?,?,?,?,?,?)",
            (medico.nome, medico.email, medico.telefone, medico.especialidade, medico.crm, medico.localidade)
        )
        if cursor:
            medico._id = cursor.lastrowid
            self.medicos.append(medico)
            agenda = Agenda(medico)
            medico.agenda = agenda
    
    def salvar_consulta(self, consulta):
        cursor = self.db.executar(
            "INSERT INTO consultas (paciente_id, medico_id, data_hora, status, observacao) VALUES (?,?,?,?,?)",
            (consulta.paciente._id, consulta.medico._id, consulta.data_hora, consulta.status, consulta.observacao)
        )
        if cursor:
            consulta._id = cursor.lastrowid
            self.consultas.append(consulta)
            consulta.medico.agenda.adicionar_consulta(consulta)
            # Gerar notificação
            notif = Notificacao(consulta.paciente, consulta)
            notif.enviar()
            self.notificacoes.append(notif)
    
    def buscar_medico_por_nome(self, nome):
        return [m for m in self.medicos if nome.lower() in m.nome.lower()]
    
    def buscar_medico_por_especialidade(self, especialidade):
        return [m for m in self.medicos if m.especialidade.lower() == especialidade.lower()]
    
    def buscar_medico_por_localidade(self, localidade):
        return [m for m in self.medicos if m.localidade.lower() == localidade.lower()]
    
    def listar_pacientes(self):
        return [p.exibir_informacoes() for p in self.pacientes]
    
    def listar_medicos(self):
        return [m.exibir_informacoes() for m in self.medicos]
    
    def listar_consultas(self):
        return [c.exibir_resumo() for c in self.consultas]
    
    def finalizar_consulta(self, consulta):
        if consulta.status == "agendada":
            consulta.status = "realizada"
            self.db.executar("UPDATE consultas SET status='realizada' WHERE id=?", (consulta._id,))
            print(f"Consulta de {consulta.data_hora} finalizada.")
        else:
            print("Somente consultas agendadas podem ser finalizadas.")
    
    def avaliar_consulta(self, consulta, nota, comentario):
        if consulta.status != "realizada":
            raise ValueError("Apenas consultas realizadas podem ser avaliadas.")
        avaliacao = Avaliacao(consulta.paciente, consulta.medico, consulta, nota, comentario)
        self.db.executar(
            "INSERT INTO avaliacoes (paciente_id, medico_id, consulta_id, nota, comentario) VALUES (?,?,?,?,?)",
            (consulta.paciente._id, consulta.medico._id, consulta._id, nota, comentario)
        )
        consulta.medico.adicionar_avaliacao(avaliacao)
        print(avaliacao.exibir_avaliacao())
    
    def fechar(self):
        self.db.fechar()
