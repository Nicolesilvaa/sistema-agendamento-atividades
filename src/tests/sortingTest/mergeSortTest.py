from datetime import time
from src.sorting.MergeSort import merge_sort
from src.models.atividade import Atividade
from src.utils.prioridade import Prioridade

def testarMergeSortNumerico():
    print("===== TESTE MERGE SORT: NÚMEROS =====")
    lista = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original: {lista}")
    ordenada = merge_sort(lista)
    print(f"Ordenada: {ordenada}")
    assert ordenada == [3, 9, 10, 27, 38, 43, 82]
    print("Sucesso!\n")

def testarMergeSortCriteriosAtividade():
    print("===== TESTE MERGE SORT: CRITÉRIOS DE ATIVIDADE =====")
    
    a1 = Atividade("Reunião A", time(10, 0), time(12, 0), Prioridade.ALTA, 5)
    a2 = Atividade("Palestra B", time(8, 0), time(9, 30), Prioridade.MEDIA, 20)
    a3 = Atividade("Workshop C", time(9, 0), time(11, 0), Prioridade.BAIXA, 10)
    
    lista = [a1, a2, a3]

    # Critério 1: Horário de Início
    por_inicio = merge_sort(lista, chave=lambda x: x.getHorarioInicio())
    assert por_inicio[0].getHorarioInicio() == time(8, 0)
    print("1. Ordenação por Horário de Início: OK")

    # Critério 2: Horário de Término
    por_fim = merge_sort(lista, chave=lambda x: x.getHorarioFim())
    assert por_fim[0].getHorarioFim() == time(9, 30)
    assert por_fim[-1].getHorarioFim() == time(12, 0)
    print("2. Ordenação por Horário de Término: OK")

    # Critério 3: Prioridade
    por_prioridade = merge_sort(lista, chave=lambda x: x.getPrioridade())
    assert por_prioridade[0].getPrioridade().value == 1 # BAIXA
    assert por_prioridade[-1].getPrioridade().value == 3 # ALTA
    print("3. Ordenação por Prioridade: OK")

    print("\nSucesso!")

def testarListaVazia():
    print("===== TESTE MERGE SORT: LISTA VAZIA =====")
    assert merge_sort([]) == []
    print("Sucesso!\n")

if __name__ == "__main__":
    testarMergeSortNumerico()
    testarListaVazia()
    testarMergeSortCriteriosAtividade()
