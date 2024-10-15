import tkinter as tk
from tkinter import messagebox, ttk
import datetime
from tkcalendar import Calendar  # Certifique-se de que você tem o tkcalendar instalado

# Defina usuário e senha pré-definidos
USUARIO_VALIDO = "admin"
SENHA_VALIDO = "123"

def sair():
    messagebox.showinfo("Sair", "Até a próxima")
    root.destroy()

def ir_para_cadastro():
    nome_usuario = nome_entry.get()
    senha_usuario = senha_entry.get()

    # Verificação de login
    if nome_usuario == USUARIO_VALIDO and senha_usuario == SENHA_VALIDO:
        # Criação da nova janela de cadastro
        root.withdraw()
        cadastro_window = tk.Toplevel(root)
        cadastro_window.title("Cadastro")

        # Título da tela de cadastro
        tk.Label(cadastro_window, text="Cadastro", font=("Comic Sans MS", 16)).pack(pady=10)

        # Campo para nome
        tk.Label(cadastro_window, text="Nome:").pack(pady=5)
        nome_entry_cadastro = tk.Entry(cadastro_window)  # Mudar para uma nova variável
        nome_entry_cadastro.pack(pady=5)

        # Opções de sexo
        tk.Label(cadastro_window, text="Sexo:").pack(pady=5)
        sexo_var = tk.StringVar()
        sexo_options = ["Masculino", "Feminino", "Outros"]
        for option in sexo_options:
            tk.Radiobutton(cadastro_window, text=option, variable=sexo_var, value=option).pack(anchor=tk.W)

        # Data de nascimento
        tk.Label(cadastro_window, text="Data de Nascimento:").pack(pady=5)
        data_nascimento_entry = tk.Entry(cadastro_window)
        data_nascimento_entry.pack(pady=5)

        # Calendário
        def show_calendar():
            calendario_window = tk.Toplevel(cadastro_window)
            calendario_window.title("Selecione a Data")

            cal = Calendar(calendario_window, selectmode='day')
            cal.pack(pady=10)

            def set_date():
                selected_date = cal.selection_get()
                data_nascimento_entry.delete(0, tk.END)
                data_nascimento_entry.insert(0, selected_date.strftime('%d/%m/%Y'))
                calendario_window.destroy()

            tk.Button(calendario_window, text="Selecionar", command=set_date).pack(pady=10)

        tk.Button(cadastro_window, text="Escolher Data", command=show_calendar).pack(pady=5)

        # Lista de profissões
        tk.Label(cadastro_window, text="Profissão:").pack(pady=5)
        profissao_var = tk.StringVar()
        profissao_options = ["Estudante", "Desenvolvedor", "Professor", "Médico", "Job", "Hacker", "Outros"]
        profissao_combobox = ttk.Combobox(cadastro_window, textvariable=profissao_var, values=profissao_options)
        profissao_combobox.pack(pady=5)

        # Observação
        tk.Label(cadastro_window, text="Observação:").pack(pady=5)
        observacao_text = tk.Text(cadastro_window, height=5, width=30)
        observacao_text.pack(pady=5)

        # Função para gravar os dados
        def gravar_dados():
            nome = nome_entry_cadastro.get()  # Usar a nova variável
            sexo = sexo_var.get()
            data_nascimento = data_nascimento_entry.get()

            # Calcular a idade
            try:
                nascimento = datetime.datetime.strptime(data_nascimento, '%d/%m/%Y')
                idade = (datetime.datetime.now() - nascimento).days // 365
            except ValueError:
                messagebox.showerror("Erro", "Data de nascimento inválida.")
                return

            profissao = profissao_var.get()
            observacao = observacao_text.get("1.0", tk.END).strip()

            # Exibir mensagem com os dados
            messagebox.showinfo("Dados Gravados",
                                f"Nome: {nome}\nSexo: {sexo}\nIdade: {idade}\nProfissão: {profissao}\nObservação: {observacao}")

        # Botões Voltar e Gravar
        btn_voltar = tk.Button(cadastro_window, text="Voltar",
                               command=lambda: [cadastro_window.destroy(), root.deiconify()])
        btn_voltar.pack(side=tk.LEFT, padx=20, pady=20)

        btn_gravar = tk.Button(cadastro_window, text="Gravar", command=gravar_dados)
        btn_gravar.pack(side=tk.RIGHT, padx=20, pady=20)

    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos.")

# Criação da janela principal
root = tk.Tk()
root.title("Tela de Login")

# Título da página
titulo = tk.Label(root, text="Tela de Login", font=("Comic Sans MS", 16))
titulo.pack(pady=10)

# Configuração do layout Nome
tk.Label(root, text="Nome:").pack(pady=5)
nome_entry = tk.Entry(root)
nome_entry.pack(pady=5)

# Configuração do layout Senha
tk.Label(root, text="Senha:").pack(pady=5)
senha_entry = tk.Entry(root, show='*')
senha_entry.pack(pady=5)

# Botão Sair
btn_sair = tk.Button(root, text="Sair", command=sair)
btn_sair.pack(side=tk.LEFT, padx=50, pady=50)

# Botão Login
btn_login = tk.Button(root, text="Login", command=ir_para_cadastro)
btn_login.pack(side=tk.RIGHT, padx=50, pady=50)

# Inicia o loop principal da interface
root.mainloop()
