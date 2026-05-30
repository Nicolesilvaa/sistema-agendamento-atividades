from datetime import time

from src.models.atividade import Atividade
from src.utils.prioridade import Prioridade

# Códigos de cor ANSI
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def testarCriacaoAtividade():

    atividade = Atividade(
        nome="Workshop Python",
        horarioInicio=time(8, 0),
        horarioFim=time(10, 0),
        prioridade=Prioridade.ALTA,
        quantidadeParticipantes=30
    )

    print(f"{YELLOW}===== TESTE DE CRIAÇÃO ====={RESET}")
    print(f"{CYAN}{atividade}{RESET}")
    print()


def testarValidacaoHorario():

    print(f"{YELLOW}===== TESTE DE VALIDAÇÃO DE HORÁRIO ====={RESET}")
    try:

        atividade = Atividade(
            nome="Atividade Inválida",
            horarioInicio=time(15, 0),
            horarioFim=time(10, 0),
            prioridade=Prioridade.MEDIA,
            quantidadeParticipantes=10
        )

    except ValueError as erro:
        print(f"{GREEN}Sucesso - Erro capturado esperado: {erro}{RESET}")

    print()


def testarValidacaoPrioridade():

    print(f"{YELLOW}===== TESTE DE VALIDAÇÃO DE PRIORIDADE ====={RESET}")
    try:

        atividade = Atividade(
            nome="Prioridade Inválida",
            horarioInicio=time(9, 0),
            horarioFim=time(11, 0),
            prioridade=5,
            quantidadeParticipantes=20
        )

    except TypeError as erro:
        print(f"{GREEN}Sucesso - Erro capturado esperado: {erro}{RESET}")

    print()

if __name__ == '__main__':

    testarCriacaoAtividade()

    testarValidacaoHorario()

    testarValidacaoPrioridade()