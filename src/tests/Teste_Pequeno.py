import time
import random
from datetime import time as dtime
from src.sorting.MergeSort import merge_sort
from src.models.atividade import Atividade
from src.utils.prioridade import Prioridade
from src.greedy.selecaoGulosa import guloso
from src.dynamicProgramming.programacaoDinamica import programacao_dinamica
from src.utils.busca import buscar_atividades

A1= Atividade("Workshop A", dtime(8,0), dtime(10,0),Prioridade.BAIXA , 20)
A2= Atividade("Palestra B", dtime(9,0), dtime(11,0),Prioridade.BAIXA, 50)
A3= Atividade("Reunião C", dtime(10,0), dtime(12,0),Prioridade.BAIXA, 10)

lista_atv= [A1, A2, A3]

resultado_guloso= guloso(lista_atv)

resultado_dinamica= programacao_dinamica(lista_atv)

print(f"Resultado guloso: {resultado_guloso[0]} \n Resultado dinamica: {resultado_dinamica[0]}")

if __name__ == "__main__":
    pass