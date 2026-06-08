import time
import random
from datetime import time as dtime
from src.sorting.MergeSort import merge_sort
from src.models.atividade import Atividade
from src.utils.prioridade import Prioridade
from src.greedy.selecaoGulosa import guloso
from src.dynamicProgramming.programacaoDinamica import programacao_dinamica
from src.utils.busca import buscar_atividades

# Cores para o console
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def gerar_dados_teste(quantidade):
    
    atividades = []
    nomes = ["Workshop", "Palestra", "Reunião", "Treinamento", "Brainstorm", "Feedback"]
    for i in range(quantidade):
        inicio_h = random.randint(8, 17)
        duracao = random.randint(1, 3)
        fim_h = min(inicio_h + duracao, 20)
        
        atividades.append(Atividade(
            nome=f"{random.choice(nomes)} {i+1}",
            horarioInicio=dtime(inicio_h, 0),
            horarioFim=dtime(fim_h, 0),
            prioridade=random.choice(list(Prioridade)),
            quantidadeParticipantes=random.randint(5, 50)
        ))
    return atividades

def executar_analise(titulo, lista, ordenacao="fim"):

    print(f"\n{YELLOW}>>> TESTE: {titulo} ({len(lista)} atividades){RESET}")
    
    # Teste Guloso
    start = time.perf_counter()
    res_guloso = guloso(lista, ordenacao)
    end = time.perf_counter()
    tempo_guloso = end - start

    # Teste Programação Dinâmica (Maximizando Participantes)
    start = time.perf_counter()
    res_dp = programacao_dinamica(lista, criterio_peso="participantes")
    end = time.perf_counter()
    tempo_dp = end - start

    # Resultados
    print(f"{'Algoritmo':<25} | {'Qtd Selecionada':<15} | {'Peso Total (Part.)':<18} | {'Tempo (s)':<10}")
    print("-" * 80)
    
    peso_guloso = sum(a.getQuantidadeParticipantes() for a in res_guloso)
    print(f"{'Guloso (Qtd)':<25} | {len(res_guloso):<15} | {peso_guloso:<18} | {tempo_guloso:.6f}")
    
    peso_dp = sum(a.getQuantidadeParticipantes() for a in res_dp)
    print(f"{'P. Dinâmica (Peso)':<25} | {len(res_dp):<15} | {peso_dp:<18} | {tempo_dp:.6f}")

def menu_busca(todas_atividades):
    print(f"\n{CYAN}--- BUSCAR ATIVIDADE ---{RESET}")
    termo = input("Digite o nome ou código da atividade: ")
    resultados = buscar_atividades(todas_atividades, termo)
    if resultados:
        for r in resultados: 
            print(f" [Achado] {r.getNome()} {r}")
    else:
        print("  Nenhuma atividade encontrada.")

############################### Funções para o sistema #############################################

def cadastrar_atividade(lista):

    nome = input("Nome: ")

    inicio = input("Horário início (HH:MM): ")
    fim = input("Horário fim (HH:MM): ")

    h_i, m_i = map(int, inicio.split(":"))
    h_f, m_f = map(int, fim.split(":"))

    print("\nPrioridades:")
    print("1 - BAIXA")
    print("2 - MEDIA")
    print("3 - ALTA")

    prioridade = Prioridade(
        int(input("Escolha: "))
    )

    participantes = int(
        input("Quantidade de participantes: ")
    )

    atividade = Atividade(
        nome=nome,
        horarioInicio=dtime(h_i, m_i),
        horarioFim=dtime(h_f, m_f),
        prioridade=prioridade,
        quantidadeParticipantes=participantes
    )

    lista.append(atividade)

    print("\nAtividade cadastrada!")



def listar_atividades(lista):

    print("\nATIVIDADES")

    for atividade in lista:
        print(atividade)


def ordenar_inicio(lista):

    return merge_sort(
        lista,
        chave=lambda a: a.getHorarioInicio()
    )

def ordenar_fim(lista):

    return merge_sort(
        lista,
        chave=lambda a: a.getHorarioFim()
    )


def ordenar_prioridade(lista):

    return merge_sort(
        lista,
        chave=lambda a: -a.getPrioridade().value
    )

def iniciar_sistema(todas_atividades):

    print( f"\nQuantidade de atividades cadastradas: {len(todas_atividades)}")

    opcao = -1

    while opcao != 0:

        print("\n===== MENU =====")

        print("1 - Cadastrar atividade")
        print("2 - Listar atividades")
        print("3 - Ordenar por início")
        print("4 - Ordenar por fim")
        print("5 - Ordenar por prioridade")
        print("6 - Buscar atividade")
        print("7 - Executar guloso")
        print("8 - Executar programação dinâmica")
        print("9 - Comparar algoritmos")
        print("0 - Sair")

        opcao = int(input("Escolha: "))

        if opcao == 1:
            cadastrar_atividade(todas_atividades)
        elif opcao == 2:
            listar_atividades(todas_atividades)
        elif opcao == 3:
            ordenadas = ordenar_inicio(
                todas_atividades
            )

            listar_atividades(ordenadas)
        elif opcao == 4:

            ordenadas = ordenar_fim(
                todas_atividades
            )

            listar_atividades(ordenadas)
        elif opcao == 5:

            ordenadas = ordenar_prioridade(
                todas_atividades
            )

            listar_atividades(ordenadas)
        elif opcao == 6:

            menu_busca(todas_atividades)
        elif opcao == 7:
            
            resultado = guloso(
                todas_atividades
            )
            print(f"\nQuantidade de atividades selecionadas:{len(resultado)}")

            print("\nSelecionadas:")

            for atividade in resultado:
                print(atividade)

            print(f"\nQuantidade de atividades selecionadas:{len(resultado)}")
            todas_atividades= resultado

        elif opcao == 8:

            resultado = programacao_dinamica(
                todas_atividades,
                criterio_peso="participantes"
            )
            print(f"\nQuantidade de atividades selecionadas:{len(resultado)}")

            print("\nSelecionadas:")

            for atividade in resultado:
                print(atividade)

            print(f"\nQuantidade de atividades selecionadas:{len(resultado)}")
            todas_atividades= resultado

        elif opcao == 9:

            executar_analise(
                "COMPARAÇÃO",
                todas_atividades
            )


if __name__ == "__main__":

    #print(f"{CYAN}{' SISTEMA DE AGENDAMENTO DE ATIVIDADES '.center(80, '=')}{RESET}")

    # Conjuntos de Teste Obrigatórios
    teste_pequeno = gerar_dados_teste(8)
    teste_medio = gerar_dados_teste(15)
    teste_grande = gerar_dados_teste(40)

    #executar_analise("PEQUENO", teste_pequeno)
    #executar_analise("MÉDIO", teste_medio)
    #executar_analise("GRANDE", teste_grande)

    # Demonstração de Busca
    #menu_busca(teste_grande)
    
    #print(f"\n{GREEN}Projeto executado com sucesso conforme critérios.{RESET}")


    iniciar_sistema(teste_medio)