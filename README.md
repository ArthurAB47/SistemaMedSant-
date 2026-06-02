# Sistema Med Santé

### Desenvolvimento de um Sistema de Agendamento Médico em Python com Programação Orientada a Objetos

---

## Sobre o Projeto

O Sistema Med Santé é um projeto desenvolvido para a disciplina de Programação Orientada a Objetos (POO) com o objetivo de simular um sistema de agendamento médico utilizando os principais conceitos da orientação a objetos em Python.

O sistema permite o gerenciamento de pacientes, médicos, consultas, agendas, avaliações e notificações, buscando representar de forma simplificada o funcionamento de uma plataforma de agendamento de consultas médicas.

Durante o desenvolvimento são aplicados conceitos como:

* Encapsulamento;
* Herança;
* Polimorfismo;
* Classes abstratas;
* Getters e Setters;
* Validação de dados;
* Tratamento de exceções;
* Persistência de dados em arquivos JSON;
* Organização modular do código.

---

## Objetivos

O projeto tem como objetivo desenvolver uma aplicação capaz de:

* Cadastrar pacientes e médicos;
* Realizar agendamentos de consultas;
* Gerenciar horários disponíveis;
* Controlar o status das consultas;
* Registrar avaliações de atendimentos;
* Gerar notificações para os usuários;
* Armazenar informações de forma organizada.

---

## Estrutura do Projeto

```text
SistemaMedSante/
│
├── database/
│   ├── pacientes.json
│   ├── medicos.json
│   ├── consultas.json
│   └── avaliacoes.json
│
├── docs/
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

## Classes do Sistema

### Usuario

Classe abstrata responsável por armazenar os atributos comuns aos usuários do sistema.

#### Principais atributos

* nome
* cpf
* email
* senha

#### Principais responsabilidades

* Validação de dados;
* Encapsulamento de atributos;
* Fornecimento de métodos comuns para pacientes e médicos.

---

### Paciente

Representa os pacientes cadastrados no sistema.

#### Funcionalidades

* Marcar consultas;
* Cancelar consultas;
* Remarcar consultas;
* Visualizar consultas agendadas;
* Visualizar histórico de consultas;
* Avaliar médicos após atendimentos concluídos.

---

### Medico

Representa os profissionais responsáveis pelos atendimentos.

#### Funcionalidades

* Gerenciar horários disponíveis;
* Confirmar presença dos pacientes;
* Encerrar consultas;
* Visualizar avaliações recebidas;
* Calcular média das avaliações.

---

### Consulta

Representa uma consulta médica entre um paciente e um médico.

#### Informações armazenadas

* Paciente;
* Médico;
* Data;
* Horário;
* Local;
* Valor da consulta;
* Status;
* Observações médicas.

#### Funcionalidades

* Alteração de status;
* Registro de observações;
* Exibição dos dados da consulta.

---

### Agenda

Responsável pelo gerenciamento dos horários disponíveis dos médicos.

#### Funcionalidades previstas

* Cadastro de horários disponíveis;
* Cancelamento de horários;
* Visualização da agenda;
* Verificação de disponibilidade para novos agendamentos.

---

### Avaliacao

Responsável pelo armazenamento das avaliações realizadas pelos pacientes.

#### Informações armazenadas

* Paciente;
* Médico;
* Nota;
* Comentário.

#### Funcionalidades previstas

* Registro de avaliações;
* Exibição de avaliações;
* Cálculo de médias dos profissionais.

---

### Notificacao

Responsável pelo envio e exibição de mensagens do sistema.

#### Funcionalidades previstas

* Geração de mensagens automáticas;
* Lembretes de consultas;
* Notificações para pacientes e médicos.

---

### SistemaMedSante

Classe principal responsável pela integração de todas as demais classes.

#### Funcionalidades previstas

* Cadastro de usuários;
* Busca de médicos;
* Gerenciamento de consultas;
* Controle geral do sistema;
* Persistência dos dados.

---

## Tecnologias Utilizadas

* Python 3
* Programação Orientada a Objetos
* Git
* GitHub
* Arquivos JSON

---

## Status Atual do Projeto

### Classes Implementadas

* [x] Usuario
* [x] Paciente
* [x] Medico
* [x] Consulta

### Classes em Desenvolvimento

* [ ] Agenda
* [ ] Avaliacao
* [ ] Notificacao
* [ ] SistemaMedSante

---

## Integrantes

* Arthur Vinicios de Abreu
* Gabriela Julia dos Santos Silva

---

## Instituição

Universidade Federal de Minas Gerais (UFMG)

Disciplina: Programação Orientada a Objetos
