# Sistema Med Santé

## Desenvolvimento de um Sistema de Agendamento Médico em Python com Programação Orientada a Objetos

### Integrantes

* Arthur Vinicios de Abreu
* Gabriela Julia dos Santos Silva

---

## Visão Geral

O Sistema Med Santé é um sistema de agendamento médico desenvolvido em Python utilizando os princípios da Programação Orientada a Objetos (POO). O projeto tem como objetivo auxiliar no gerenciamento de pacientes, médicos, consultas, agendas, notificações e avaliações, proporcionando uma estrutura organizada para o controle dos atendimentos.

O sistema permite o cadastro e gerenciamento dos usuários, o agendamento de consultas médicas, o acompanhamento do histórico de atendimentos e o armazenamento permanente dos dados por meio de arquivos JSON.

Atualmente o sistema encontra-se funcional, possuindo integração entre todas as classes principais, persistência de dados e um menu interativo executado via terminal.

---

## Objetivos do Projeto

* Aplicar os conceitos de Programação Orientada a Objetos.
* Desenvolver um sistema modular e organizado.
* Simular o funcionamento básico de uma plataforma de agendamento médico.
* Implementar armazenamento permanente dos dados.
* Promover reutilização de código e separação de responsabilidades entre as classes.

---

## Funcionalidades Implementadas

### Pacientes

* Cadastro de pacientes.
* Visualização de informações pessoais.
* Marcação de consultas.
* Cancelamento de consultas.
* Remarcação de consultas.
* Consulta ao histórico de atendimentos.

### Médicos

* Cadastro de médicos.
* Visualização de dados profissionais.
* Confirmação de presença do paciente.
* Encerramento de consultas.
* Recebimento de avaliações.
* Cálculo da média das avaliações recebidas.

### Consultas

* Criação de consultas médicas.
* Alteração de status.
* Registro de observações médicas.
* Controle de consultas realizadas e canceladas.

### Agenda

* Cadastro de horários disponíveis.
* Controle de disponibilidade dos horários.
* Gerenciamento das consultas marcadas.

### Avaliações

* Registro de notas e comentários.
* Associação entre paciente, médico e consulta.
* Cálculo da média de avaliações dos profissionais.

### Notificações

* Geração automática de mensagens para os pacientes.
* Controle de envio e leitura das notificações.

### Persistência de Dados

O sistema realiza o armazenamento permanente dos dados utilizando arquivos JSON:

* pacientes.json
* medicos.json
* consultas.json
* avaliacoes.json

Os dados são salvos automaticamente durante a utilização do sistema e carregados novamente sempre que a aplicação é iniciada.

---

## Requisitos de Programação Orientada a Objetos Aplicados

Durante o desenvolvimento do projeto foram utilizados os seguintes conceitos:

* Classes e Objetos
* Encapsulamento
* Herança
* Classe Abstrata
* Polimorfismo
* Getters e Setters
* Associação entre Objetos
* Tratamento de Exceções
* Persistência de Dados em Arquivos JSON

---

## Organização do Projeto

### models/

Contém as entidades principais do sistema:

* Usuario
* Paciente
* Medico
* Consulta
* Agenda
* Avaliacao
* Notificacao

### services/

Contém a classe responsável pelo gerenciamento geral do sistema:

* SistemaMedSante

### database/

Responsável pelo armazenamento permanente dos dados em formato JSON:

* pacientes.json
* medicos.json
* consultas.json
* avaliacoes.json

---

## Estrutura de Diretórios

```text
SistemaMedSante/
│
├── database/
│   ├── pacientes.json
│   ├── medicos.json
│   ├── consultas.json
│   └── avaliacoes.json
│
├── models/
│   ├── usuario.py
│   ├── paciente.py
│   ├── medico.py
│   ├── consulta.py
│   ├── agenda.py
│   ├── avaliacao.py
│   └── notificacao.py
│
├── services/
│   └── sistema_med_sante.py
│
├── interface.py
├── main.py
└── README.md
```

---

## Fluxo Básico de Utilização

1. Cadastrar pacientes e médicos.
2. Disponibilizar horários para atendimento.
3. Realizar o agendamento de consultas.
4. Confirmar a presença do paciente.
5. Encerrar a consulta.
6. Registrar avaliações.
7. Salvar automaticamente os dados em arquivos JSON.
8. Recuperar os dados ao reiniciar o sistema.

---

## Execução do Sistema

Para executar o sistema:

```bash
python main.py
```

Após a execução, o usuário poderá utilizar o menu principal para realizar cadastros, consultas, avaliações e gerenciamento dos dados armazenados.

---

## Situação Atual do Projeto

O sistema possui atualmente:

* Todas as classes principais implementadas.
* Integração completa entre os módulos.
* Persistência de dados em JSON.
* Menu funcional via terminal.
* Tratamento de exceções para validação de dados.
* Funcionalidades essenciais para gerenciamento de consultas médicas.

---

## Próximas Melhorias

* Implementação de interface gráfica.
* Ampliação dos mecanismos de busca.
* Melhorias no gerenciamento de agendas.
* Expansão das funcionalidades administrativas.
* Evolução da experiência de utilização do sistema.

Essas melhorias poderão ser incorporadas em versões futuras do projeto.
