class Tarefa :
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao

# Função para exibir um menu
def exibirMenu():
    print("╔══════════════════════════════╗")
    print("║           MENU               ║")
    print("╟──────────────────────────────╢")
    print("║ 1. Adicionar tarefa          ║")
    print("║ 2. Listar tarefas            ║")
    print("║ 3. Visualizar detalhes       ║")
    print("║    de uma tarefa             ║")
    print("║ 4. Atualizar tarefa          ║")
    print("║ 5. Excluir tarefa            ║")
    print("║ 6. Sair                      ║")
    print("╚══════════════════════════════╝")

# Lista para armazenar as tarefas
tarefas = []

# Função para adicionar uma tarefa
def adicionarTarefa():
    id = len(tarefas) + 1
    nome = input("Digite o nome da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")

    tarefa = Tarefa(id, nome, descricao)

    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso")

# Função para listar as tarefas
def listarTarefas():
    if len(tarefas) == 0:
        print("-" * 30)  
        print("Não existem tarefas cadastradas")
        print("-" * 30)  
    else :
        print("Lista de Tarefas")
        print("-" * 30)  
        for tarefa in tarefas:
            print(f"{tarefa.id} - {tarefa.nome}")
        print("-" * 30)  

# Função para visualizar detalhes de uma tarefa
def visualizarDetalhes():
    listarTarefas()

    if len(tarefas) == 0:
        return
    else :
        id = int(input("Digite o ID da tarefa que deseja visualizar: "))

        if id <= len(tarefas):
            tarefa = tarefas[id - 1]

            print("Detalhes da tarefa")
            print("-" * 30)  
            print("Nome: " + tarefa.nome)
            print("Descrição: " + tarefa.descricao)
            print("-" * 30)  
        else:
            print("-" * 30)  
            print("Tarefa não encontrada")
            print("-" * 30)  

# Função para atualizar uma tarefa
def atualizarTarefa():
    listarTarefas()
    
    if len(tarefas) == 0:
        return
    else :
        id = int(input("Digite o ID da tarefa que deseja atualizar: "))

        if id <= len(tarefas):
            tarefa = tarefas[id - 1]

            tarefa.nome = input("Digite o nome da tarefa: ")
            tarefa.descricao = input("Digite a descrição da tarefa: ")
        else:
            print("-" * 30)  
            print("Tarefa não encontrada")
            print("-" * 30)

# Função para excluir uma tarefa
def excluirTarefa():
    listarTarefas()

    if len(tarefas) == 0:
        return
    else :
        id = int(input("Digite o ID da tarefa que deseja excluir: "))
        
        if id <= len(tarefas):
            tarefas.pop(id - 1)
        else:
            print("-" * 30)  
            print("Tarefa não encontrada")
            print("-" * 30)

# Função para sair do programa
def sair():
    print("Saindo do programa")
    exit()

# Dicionário de opções
opcoes = {
    1: adicionarTarefa,
    2: listarTarefas,
    3: visualizarDetalhes,
    4: atualizarTarefa,
    5: excluirTarefa,
    6: sair
}

# Loop infinito
while True:
    exibirMenu()

    opcao = int(input("Digite a opção desejada: "))
    
    if opcao in opcoes:
        opcoes[opcao]()
    else:
        print("Opção inválida! Por favor, tente novamente")
        