def merge_sort(lista, chave=lambda x: x):
    """
    Implementação  do Merge Sort para ordenação de atividades.
    """
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], chave)
    direita = merge_sort(lista[meio:], chave)

    return merge(esquerda, direita, chave)

def merge(esquerda, direita, chave):
    resultado = []
    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        # Compara usando a chave fornecida (horário, prioridade, etc)
        if chave(esquerda[i]) <= chave(direita[j]):
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado
