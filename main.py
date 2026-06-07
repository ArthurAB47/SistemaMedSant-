from services.SistemaMedSante import SistemaMedSante
from models.agenda import Agenda

def main():
    sistema = SistemaMedSante()

    paciente = sistema.cadastrar_paciente(
        "Arthur Vinicios",
        "12345678901",
        "arthur@email.com",
        "123456",
        "Belo Horizonte"
    )

    medico = sistema.cadastrar_medico(
        "Gabriela Santos",
        "10987654321",
        "gabriela@email.com",
        "123456",
        "CRM12345",
        "Cardiologia",
        "Clínica Med Santé - Belo Horizonte",
        150.00
    )

    agenda = Agenda(medico)

    agenda.adicionar_horario("10/06/2026", "14:00")

    consulta = paciente.marcar_consulta(medico, "10/06/2026", "14:00")

    agenda.adicionar_consulta(consulta)

    sistema.registrar_consulta(consulta)

    notificacao = sistema.gerar_notificacao(paciente, consulta)
    notificacao.enviar()

    medico.confirmar_presenca_paciente(consulta)

    medico.encerrar_consulta(consulta, "Paciente compareceu e realizou a consulta normalmente.")

    avaliacao = sistema.avaliar_consulta(
        paciente,
        medico,
        consulta,
        5,
        "Ótimo atendimento."
    )

    print()
    paciente.exibir_dados()

    print()
    medico.exibir_dados()

    print()
    consulta.exibir_dados()

    print()
    avaliacao.exibir_avaliacao()

    print()
    print(f"Média de avaliações do médico: {medico.calcular_media_avaliacoes():.2f}")


if __name__ == "__main__":
    main()