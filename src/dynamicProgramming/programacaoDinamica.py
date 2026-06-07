from src.sorting.MergeSort import merge_sort

def programacao_dinamica(atividades, criterio_peso="participantes"):
    """
    Implementação do Weighted Interval Scheduling usando Programação Dinâmica.
    Maximiza o benefício total com base no critério de peso escolhido.
    """
    if not atividades:
        return []

    # Ordenar por horário de fim (essencial para DP de intervalos)
    ordenadas = merge_sort(atividades, chave=lambda a: a.getHorarioFim())
    n = len(ordenadas)
    
    # Definir os pesos
    if criterio_peso == "prioridade":
        pesos = [a.getPrioridade().value for a in ordenadas]
    else:
        pesos = [a.getQuantidadeParticipantes() for a in ordenadas]

    # Encontrar o último índice 'p' que não conflita com a atividade i
    p = [-1] * n #guarda o índice da última atividade que não entra em conflito com a atividade i
    for i in range(n):
        for j in range(i - 1, -1, -1):
            if ordenadas[j].getHorarioFim() <= ordenadas[i].getHorarioInicio():
                p[i] = j
                break

    # Tabela de memoização para o valor máximo
    M = [0] * (n + 1)
    escolhas = [False] * (n + 1) # registra se a atividade foi escolhida.

    for j in range(1, n + 1):
        # Opção 1: Incluir atividade j-1
        valor_incluir = pesos[j-1] + (M[p[j-1] + 1] if p[j-1] != -1 else 0) #Benefício da atividade atual + melhor solução compatível anterior.
        # Opção 2: Não incluir
        valor_excluir = M[j-1]

        if valor_incluir >= valor_excluir:
            M[j] = valor_incluir
            escolhas[j] = True
        else:
            M[j] = valor_excluir

    # Reconstruir a solução obs crr -> current , atual
    selecionadas = []
    curr = n
    while curr > 0:
        if escolhas[curr]:
            selecionadas.append(ordenadas[curr-1])
            curr = p[curr-1] + 1
        else:
            curr -= 1

    return selecionadas[::-1] # A lista é invertida para ficar em ordem cronológica.