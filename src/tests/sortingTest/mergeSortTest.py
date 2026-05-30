from datetime import time
from src.sorting.MergeSort import merge_sort
from src.models.Atividade import Atividade
from src.utils.Prioridade import Prioridade

def testarMergeSortNumerico():
    print("===== TESTE MERGE SORT: NÚMEROS =====")
    lista = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original: {lista}")
    ordenada = merge_sort(lista)
    print(f"Ordenada: {ordenada}")
    assert ordenada == [3, 9, 10, 27, 38, 43, 82]
    print("Sucesso!\n")

def testarMergeSortCriterios():
    print("===== TESTE MERGE SORT: CRITÉRIOS DE ATIVIDADE =====")
    
    a1 = Atividade("Reunião A", time(10, 0), time(12, 0), Prioridade.ALTA, 5)
    a2 = Atividade("Palestra B", time(8, 0), time(9, 30), Prioridade.MEDIA, 20)
    a3 = Atividade("Workshop C", time(9, 0), time(11, 0), Prioridade.BAIXA, 10)
    
    lista = [a1, a2, a3]

    # 1. Ordenar por Horário de Início
    por_inicio = merge_sort(lista, chave=lambda x: x.getHorarioInicio())
    assert por_inicio[0].getNome() == "Palestra B" # 08:00
    print("Ordenação por Início: OK")

    # 2. Ordenar por Horário de Término
    por_fim = merge_sort(lista, chave=lambda x: x.getHorarioFim())
    assert por_fim[0].getNome() == "Palestra B" # 09:30
    assert por_fim[1].getNome() == "Workshop C" # 11:00
    print("Ordenação por Fim: OK")

    # 3. Ordenar por Prioridade (Crescente)
    por_prioridade = merge_sort(lista, chave=lambda x: x.getPrioridade())
    assert por_prioridade[0].getPrioridade() == Prioridade.BAIXA
    print("Ordenação por Prioridade: OK")

    print("\nSucesso!")

def testarListaVazia():
    print("===== TESTE MERGE SORT: LISTA VAZIA =====")
    assert merge_sort([]) == []
    print("Sucesso!\n")

if __name__ == "__main__":
    testarMergeSortNumerico()
    testarListaVazia()
    testarMergeSortCriterios()
