from src.models.atividade import Atividade as at
from datetime import time
from sorting.MergeSort import merge_sort as msort
import random


def guloso(atividades:list, ordenacao= "fim"):

    if ordenacao == "prioridade":
        chave= lambda a:a.getPrioridade()
    elif ordenacao == "inicio":
        chave= lambda a:a.getHorarioInicio()
    elif ordenacao == "fim":
        chave= lambda a:a.getHorarioFim(0)
    
    ordenadas = msort(msort(atividades, chave  ))

    selecionadas = []

    ultima = None

    for atividade in ordenadas:

        if ultima is None:
            selecionadas.append(atividade)

            ultima= atividade

        elif atividade.getHorarioInicio() >= ultima.getHorarioFim():

            selecionadas.append(atividade)
            ultima = atividade

    return selecionadas
        

if __name__ == "__main__":
    from datetime import time
    from src.sorting.MergeSort import merge_sort
    from src.models.atividade import Atividade
    from src.utils.prioridade import Prioridade


    def gerar_lista_atividades(numero):
        atividades= []

        for i in range(numero):
            prio= random.randint(1,3)
            atividades.append(Atividade("Reunião A", time(10, 0), time(12, 0), Prioridade(prio), 5))
            pass

    print(Prioridade(1))

