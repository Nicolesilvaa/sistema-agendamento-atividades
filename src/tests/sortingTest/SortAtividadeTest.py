from datetime import time
from src.models.atividade import Atividade
from src.utils.prioridade import Prioridade
from src.sorting.MergeSort import merge_sort as msort
from src.greedy.selecaoGulosa import guloso
import random






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
    print(f"{atv.getNome()} | {atv.getHorarioInicio()} | {atv.getHorarioFim()}")
    print()