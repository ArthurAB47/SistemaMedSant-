import tkinter as tk
from tkinter import messagebox

class InterfaceMedSante:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Sistema Med Santé")
        self.janela.geometry("400x300")

        self.pacientes = []
        self.medicos = []
        self.consultas = []

        self.criar_tela_inicial()

    def limpar_tela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

    def criar_tela_inicial(self):
        self.limpar_tela()

        titulo = tk.Label(self.janela, text="Sistema Med Santé", font=("Arial", 18))
        titulo.pack(pady=20)

        botao_paciente = tk.Button(self.janela, text="Cadastrar paciente", width=25)
        botao_paciente.pack(pady=5)

        botao_medico = tk.Button(self.janela, text="Cadastrar médico", width=25)
        botao_medico.pack(pady=5)

        botao_consulta = tk.Button(self.janela, text="Marcar consulta", width=25)
        botao_consulta.pack(pady=5)

        botao_listar = tk.Button(self.janela, text="Listar consultas", width=25)
        botao_listar.pack(pady=5)

        botao_sair = tk.Button(self.janela, text="Sair", width=25, command=self.janela.destroy)
        botao_sair.pack(pady=5)

    def executar(self):
        self.janela.mainloop()


app = InterfaceMedSante()
app.executar()