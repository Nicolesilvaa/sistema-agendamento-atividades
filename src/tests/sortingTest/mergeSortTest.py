from datetime import time
from src.sorting.MergeSort import merge_sort
from src.models.atividade import Atividade
from src.utils.prioridade import Prioridade

# Códigos de cor ANSI
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def testarMergeSortNumerico():
    print(f"{YELLOW}===== TESTE MERGE SORT: NÚMEROS ====={RESET}")
    lista = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original: {CYAN}{lista}{RESET}")
    ordenada = merge_sort(lista)
    print(f"Ordenada: {CYAN}{ordenada}{RESET}")
    assert ordenada == [3, 9, 10, 27, 38, 43, 82]
    print(f"{GREEN}Sucesso!{RESET}\n")

def testarMergeSortCriteriosAtividade():
    print(f"{YELLOW}===== TESTE MERGE SORT: CRITÉRIOS DE ATIVIDADE ====={RESET}")
    
    a1 = Atividade("Reunião A", time(10, 0), time(12, 0), Prioridade.ALTA, 5)
    a2 = Atividade("Palestra B", time(8, 0), time(9, 30), Prioridade.MEDIA, 20)
    a3 = Atividade("Workshop C", time(9, 0), time(11, 0), Prioridade.BAIXA, 10)
    
    lista = [a1, a2, a3]

    # Critério 1: Horário de Início
    por_inicio = merge_sort(lista, chave=lambda x: x.getHorarioInicio())
    assert por_inicio[0].getHorarioInicio() == time(8, 0)
    print(f"{CYAN}1. Ordenação por Horário de Início: OK{RESET}")

    # Critério 2: Horário de Término
    por_fim = merge_sort(lista, chave=lambda x: x.getHorarioFim())
    assert por_fim[0].getHorarioFim() == time(9, 30)
    assert por_fim[-1].getHorarioFim() == time(12, 0)
    print(f"{CYAN}2. Ordenação por Horário de Término: OK{RESET}")

    # Critério 3: Prioridade
    por_prioridade = merge_sort(lista, chave=lambda x: x.getPrioridade())
    assert por_prioridade[0].getPrioridade().value == 1 # BAIXA
    assert por_prioridade[-1].getPrioridade().value == 3 # ALTA
    print(f"{CYAN}3. Ordenação por Prioridade: OK{RESET}")

    print(f"\n{GREEN}Sucesso!{RESET}")

def testarListaVazia():
    print(f"{YELLOW}===== TESTE MERGE SORT: LISTA VAZIA ====={RESET}")
    assert merge_sort([]) == []
    print(f"{GREEN}Sucesso!{RESET}\n")

if __name__ == "__main__":
    testarMergeSortNumerico()
    testarListaVazia()
    testarMergeSortCriteriosAtividade()
