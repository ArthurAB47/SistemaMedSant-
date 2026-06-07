from services.sistema_med_sante import SistemaMedSante

def menu():
    print("\n===== SISTEMA MED SANTÉ =====")
    print("1 - Cadastrar paciente")
    print("2 - Cadastrar médico")
    print("3 - Listar pacientes")
    print("4 - Listar médicos")
    print("5 - Buscar médico por especialidade")
    print("6 - Marcar consulta")
    print("7 - Listar consultas")
    print("8 - Encerrar consulta")
    print("9 - Avaliar consulta")
    print("10 - Cadastrar horário para médico")
    print("11 - Visualizar agenda de médico")
    print("0 - Sair")

def main():
    sistema = SistemaMedSante()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                nome = input("Nome: ")
                cpf = input("CPF: ")
                email = input("Email: ")
                senha = input("Senha: ")
                localizacao = input("Localização: ")

                sistema.cadastrar_paciente(nome, cpf, email, senha, localizacao)
                print("Paciente cadastrado com sucesso!")

            elif opcao == "2":
                nome = input("Nome: ")
                cpf = input("CPF: ")
                email = input("Email: ")
                senha = input("Senha: ")
                crm = input("CRM: ")
                especialidade = input("Especialidade: ")
                clinica = input("Clínica: ")
                valor = float(input("Valor da consulta: "))

                sistema.cadastrar_medico(nome, cpf, email, senha, crm, especialidade, clinica, valor)
                print("Médico cadastrado com sucesso!")

            elif opcao == "3":
                sistema.listar_pacientes()

            elif opcao == "4":
                sistema.listar_medicos()

            elif opcao == "5":
                especialidade = input("Digite a especialidade: ")
                medicos = sistema.buscar_medico_por_especialidade(especialidade)

                if len(medicos) == 0:
                    print("Nenhum médico encontrado.")
                else:
                    print("Médicos encontrados:")
                    for i, medico in enumerate(medicos):
                        print(f"{i} - {medico.nome} | {medico.especialidade} | {medico.clinica}")

            elif opcao == "6":
                if len(sistema.pacientes) == 0 or len(sistema.medicos) == 0:
                    print("É necessário ter pelo menos um paciente e um médico cadastrado.")
                else:
                    print("Pacientes:")
                    for i, paciente in enumerate(sistema.pacientes):
                        print(f"{i} - {paciente.nome}")

                    indice_paciente = int(input("Escolha o paciente: "))
                    paciente = sistema.pacientes[indice_paciente]

                    print("Médicos:")
                    for i, medico in enumerate(sistema.medicos):
                        print(f"{i} - {medico.nome} | {medico.especialidade}")

                    indice_medico = int(input("Escolha o médico: "))
                    medico = sistema.medicos[indice_medico]

                    data = input("Data da consulta (DD/MM/AAAA): ")
                    horario = input("Horário da consulta (HH:MM): ")

                    if medico.agenda.verificar_disponibilidade(data, horario):
                        consulta = paciente.marcar_consulta(medico, data, horario)
                        medico.agenda.adicionar_consulta(consulta)
                        sistema.registrar_consulta(consulta)

                        notificacao = sistema.gerar_notificacao(paciente, consulta)
                        notificacao.enviar()

                        print("Consulta marcada com sucesso!")
                    else:
                        print("Horário indisponível na agenda do médico.")

            elif opcao == "7":
                sistema.listar_consultas()

            elif opcao == "8":
                if len(sistema.consultas) == 0:
                    print("Não há consultas cadastradas.")
                else:
                    print("Consultas:")
                    for i, consulta in enumerate(sistema.consultas):
                        print(f"{i} - {consulta}")

                    indice = int(input("Escolha a consulta: "))
                    consulta = sistema.consultas[indice]

                    observacao = input("Observação médica: ")
                    consulta.medico.confirmar_presenca_paciente(consulta)
                    consulta.medico.encerrar_consulta(consulta, observacao)

                    print("Consulta encerrada com sucesso!")

            elif opcao == "9":
                if len(sistema.consultas) == 0:
                    print("Não há consultas cadastradas.")
                else:
                    print("Consultas:")
                    for i, consulta in enumerate(sistema.consultas):
                        print(f"{i} - {consulta}")

                    indice = int(input("Escolha a consulta: "))
                    consulta = sistema.consultas[indice]

                    nota = input("Nota de 1 a 5: ")
                    comentario = input("Comentário: ")

                    avaliacao = sistema.avaliar_consulta(
                        consulta.paciente,
                        consulta.medico,
                        consulta,
                        nota,
                        comentario
                    )

                    avaliacao.exibir_avaliacao()

            elif opcao == "10":
                if len(sistema.medicos) == 0:
                    print("Não há médicos cadastrados.")
                else:
                    print("Médicos:")
                    for i, medico in enumerate(sistema.medicos):
                        print(f"{i} - {medico.nome} | {medico.especialidade}")

                    indice_medico = int(input("Escolha o médico: "))
                    medico = sistema.medicos[indice_medico]

                    data = input("Data disponível (DD/MM/AAAA): ")
                    horario = input("Horário disponível (HH:MM): ")

                    medico.cadastrar_horario(data, horario)
                    sistema.salvar_dados()
                    print("Horário cadastrado com sucesso!")

            elif opcao == "11":
                if len(sistema.medicos) == 0:
                    print("Não há médicos cadastrados.")
                else:
                    print("Médicos:")
                    for i, medico in enumerate(sistema.medicos):
                        print(f"{i} - {medico.nome} | {medico.especialidade}")

                    indice_medico = int(input("Escolha o médico: "))
                    medico = sistema.medicos[indice_medico]

                    medico.visualizar_agenda()

            elif opcao == "0":
                print("Encerrando o sistema...")
                break

            else:
                print("Opção inválida.")

        except ValueError as erro:
            print(erro)

        except IndexError:
            print("Opção escolhida não existe na lista.")


if __name__ == "__main__":
    main()