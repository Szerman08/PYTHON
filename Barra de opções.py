from tkinter import *
from tkinter import messagebox

def semComando():
    print("")

def mostrarProgramador():
        messagebox.showinfo("Dados do Programador", "Nome: Caio Szerman\nIdade: 21\n\nBy Caio Szerman")

app = Tk()
app.title("Caio Szerman")
app.geometry("500x300")
app.configure(background="#dde")

barraDeMenus = Menu(app)
menuContatos = Menu(barraDeMenus, tearoff=0)
menuContatos.add_command(label="Novo", command=semComando)
menuContatos.add_command(label="Pesquisar", command=semComando)
menuContatos.add_command(label="Deletar", command=semComando)
menuContatos.add_separator()
menuContatos.add_command(label="Fechar", command=app.quit)
barraDeMenus.add_cascade(label="Contatos", menu=menuContatos)

menuManutenção=Menu(barraDeMenus, tearoff=0)
menuManutenção.add_command(label="Banco de Dados",command=semComando)
barraDeMenus.add_cascade(label="Manutenção", menu=menuManutenção)

menuSobre=Menu(barraDeMenus, tearoff=0)
menuSobre.add_command(label="Caio Cursos",command=semComando)
barraDeMenus.add_cascade(label="Sobre", menu=menuSobre)

menuRelatorio=Menu(barraDeMenus, tearoff=0)
menuRelatorio.add_command(label="Relatório 1",command=semComando)
menuRelatorio.add_command(label="Relatório 2",command=semComando)
menuRelatorio.add_command(label="Relatório 3",command=semComando)
barraDeMenus.add_cascade(label="Relatório", menu=menuRelatorio)

menuInformaçoes=Menu(barraDeMenus, tearoff=0)
menuInformaçoes.add_command(label="Programa",command=semComando)
menuInformaçoes.add_command(label="Programador",command=mostrarProgramador)
menuInformaçoes.add_command(label="Sair", command=app.quit)
barraDeMenus.add_cascade(label="Informações", menu=menuInformaçoes)



# Configurando a barra de menus na janela

app.config(menu=barraDeMenus)
app.mainloop()

