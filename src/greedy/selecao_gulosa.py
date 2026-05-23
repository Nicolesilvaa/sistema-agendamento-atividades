from src.models.atividade import Atividade as at
from datetime import time


def guloso(lista= list()):
    
    for i in range(len(lista)-1):
        pass

# Teste 1
if __name__ == "__main__":
    ativ= at(
        nome="Prioridade Inválida",
        horarioInicio=time(9, 0),
        horarioFim=time(11, 0),
        prioridade=5,
        quantidadeParticipantes=20
    )
    print(ativ)
