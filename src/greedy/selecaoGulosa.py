from datetime import time
from src.models.atividade import Atividade
from src.utils.prioridade import Prioridade

from src.sorting.MergeSort import merge_sort as msort
import random


def guloso(atividades, ordenacao= "fim"):

    if ordenacao == "prioridade":
        chave= lambda a: a.getPrioridade()
    elif ordenacao == "inicio":
        chave= lambda a: a.getHorarioInicio()
    elif ordenacao == "fim":
        chave= lambda a: a.getHorarioFim()
    
    ordenadas = msort(atividades, chave )

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
    
    def gerar_lista_atividades(numero):

        atividades= []

        for i in range(numero):
            prio= random.randint(1,3)
            inicio= random.randint(1,19)
            fim= inicio + random.randint(1,2)

            nomes=[ "Reunião de Equipe", "Reunião com Cliente", "Treinamento Interno", "Entrevista de Candidato", "Planejamento Estratégico", "Apresentação de Resultados", "Workshop de Inovação", "Revisão de Projeto"]
            nome_atv= random.choice(nomes)
            participantes= random.randint(1,20)

            atividades.append(Atividade(nome_atv, time(inicio, 0), time(fim, 0), Prioridade(prio), participantes))

        return atividades


    lista= gerar_lista_atividades(10)

    print(len(lista))
    for atv in lista:
        print(atv)
        print()
    print("####################################################################")
    
    lista= guloso(lista, "fim")


    print(len(lista))

    for atv in lista:
        print(atv.getNome())
        print()