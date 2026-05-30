from datetime import time
from src.models.Atividade import Atividade
from src.utils.Prioridade import Prioridade

def testarCriacaoAtividade():

    atividade = Atividade(
        nome="Workshop Python",
        horarioInicio=time(8, 0),
        horarioFim=time(10, 0),
        prioridade=Prioridade.ALTA,
        quantidadeParticipantes=30
    )

    print("===== TESTE DE CRIAÇÃO =====")
    print(atividade)
    print()


def testarValidacaoHorario():

    print("===== TESTE DE VALIDAÇÃO DE HORÁRIO =====")
    try:

        atividade = Atividade(
            nome="Atividade Inválida",
            horarioInicio=time(15, 0),
            horarioFim=time(10, 0),
            prioridade=Prioridade.MEDIA,
            quantidadeParticipantes=10
        )

    except ValueError as erro:
        print(f"Erro capturado: {erro}")

    print()


def testarValidacaoPrioridade():

    print("===== TESTE DE VALIDAÇÃO DE PRIORIDADE =====")
    try:

        atividade = Atividade(
            nome="Prioridade Inválida",
            horarioInicio=time(9, 0),
            horarioFim=time(11, 0),
            prioridade=5,
            quantidadeParticipantes=20
        )

    except TypeError as erro:
        print(f"Erro capturado: {erro}")

    print()

if __name__ == '__main__':

    testarCriacaoAtividade()

    testarValidacaoHorario()

    testarValidacaoPrioridade()