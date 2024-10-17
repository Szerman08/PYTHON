from tkinter import *
from tkinter import messagebox

def mostrarMsg(tiposmg, msg):
    if tiposmg == "1":
        messagebox.showinfo("App Szerman", msg)
    elif tiposmg == "2":
        messagebox.showwarning("App Szerman", msg)
    elif tiposmg == "3":
        messagebox.showerror("App Szerman", msg)

def resetarTB():
    res = messagebox.askyesno("Resetar", "Confirmar reset do textbox?")
    if res == True:
        tb_num.delete(0, END)
        tb_num.insert(0, "1")

def exibirMensagem():
    # Capturar o nome digitado na caixa de nome
    nome = nome_var.get()
    if nome == "":
        messagebox.showerror("Erro", "Por favor, digite um nome")
        return
    # Construir a mensagem com o nome
    vmsg = f"Olá, {nome}, Seja bem vindo ao Curso do Caio/Tkinter"
    # Exibir a mensagem na caixa correspondente ao tipo selecionado
    mostrarMsg(vnum_cstexto.get(), vmsg)

# Configuração da janela principal
app = Tk()
app.title("App Szerman")
app.geometry("500x300")

# Variável que armazena o nome digitado
nome_var = StringVar()

# Adicionando rótulo e campo de entrada para o nome
Label(app, text="Digite seu nome:").place(x=20, y=20)
nome_entry = Entry(app, textvariable=nome_var)
nome_entry.place(x=150, y=20)

# Variável que armazena o valor digitado no campo de texto
vnum_cstexto = StringVar()

# Adicionando rótulo para o tipo de caixa
Label(app, text="Tipo de caixa (1, 2, 3)").place(x=20, y=50)

# Adicionando campo de entrada (Entry) com textvariable
tb_num = Entry(app, textvariable=vnum_cstexto)
vnum_cstexto.set("1")
tb_num.place(x=150, y=50)

# Adicionando botão para mostrar a mensagem
btn_msg = Button(app, text="Mostrar mensagem", command=exibirMensagem)
btn_msg.place(x=20, y=100)

# Adicionando botão para resetar o campo de texto
btn_reset = Button(app, text="Resetar TextBox", command=resetarTB)
btn_reset.place(x=150, y=100)

app.mainloop()
