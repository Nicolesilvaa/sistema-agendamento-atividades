from src.models.atividade import Atividade as at
from datetime import time
from sorting.MergeSort import merge_sort as msort

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


