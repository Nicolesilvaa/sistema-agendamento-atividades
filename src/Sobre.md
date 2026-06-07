---

## Descrição da Solução
O sistema foi desenvolvido para resolver o problema de agendamento de intervalos. A solução foca em dois objetivos distintos:
1. **Maximização da Quantidade:** Selecionar o maior número de eventos possíveis em um dia.
2. **Maximização do Valor:** Selecionar eventos que tragam o maior benefício (peso), seja por prioridade ou número de participantes.

A aplicação gerencia conflitos verificando se o `horário de início` de uma nova atividade é maior ou igual ao `horário de término` da atividade anterior selecionada.

## Algoritmos Utilizados

### 1. Merge Sort (Ordenação)
- **Uso:** Obrigatório para organizar as atividades antes da execução dos seletores.
- **Complexidade:** $O(n \log n)$.
- **Por que:** É um algoritmo de divisão e conquista estável, garantindo que a ordem relativa de elementos iguais seja preservada.

### 2. Algoritmo Guloso (Seleção de Atividades)
- **Estratégia:** Seleciona sempre a atividade que termina mais cedo (*Earliest Finish Time First*).
- **Objetivo:** Maximizar o número total de atividades sem conflito.
- **Complexidade:** $O(n \log n)$ (devido à ordenação necessária).

### 3. Programação Dinâmica (Weighted Interval Scheduling)
- **Estratégia:** Utiliza memoização para decidir entre incluir ou excluir uma atividade com base no peso (participantes).
- **Objetivo:** Maximizar o benefício total, mesmo que isso resulte em menos atividades selecionadas.
- **Complexidade:** $O(n^2)$ nesta implementação para busca de compatibilidade.

## Comparação entre Abordagens

| Característica | Algoritmo Guloso | Programação Dinâmica |
| :--- | :--- | :--- |
| **Métrica Principal** | Quantidade de atividades. | Peso total (Participantes/Prioridade). |
| **Complexidade** | Mais eficiente ($O(n \log n)$). | Mais complexo ($O(n^2)$ ou $O(n \log n)$). |
| **Resultado** | Ótimo para volume de agenda. | Ótimo para valor/importância da agenda. |

##  Exemplos de Entradas e Saídas

**Entrada Sugerida (Teste Pequeno):**
1. Workshop A (08:00 - 10:00, Part: 20)
2. Palestra B (09:00 - 11:00, Part: 50)
3. Reunião C (10:00 - 12:00, Part: 10)

**Saída Guloso:**
- Workshop A e Reunião C (Total: 2 atividades, 30 participantes)

**Saída P. Dinâmica:**
- Palestra B (Total: 1 atividade, 50 participantes) -> *Priorizou o peso em vez da quantidade.*

## Funcionalidades Implementadas

- [x] **Cadastro:** Atividades com código único (UUID), nome, horários, prioridade e participantes.
- [x] **Organização:** Ordenação via Merge Sort por início, fim ou prioridade.
- [x] **Busca:** Filtro de atividades por nome ou código.
- [x] **Análise de Desempenho:** Comparação de tempo de execução entre Guloso e DP.
- [x] **Testes Automatizados:** Scripts para cenários Pequeno (8), Médio (15) e Grande (35).

## Referências:

INTZMAYER, Carla Negri; MOTA, Guilherme Oliveira. Análise de Algoritmos e de Estruturas de Dados. Versão de 4 ago. 2023. Universidade Federal do ABC; Universidade de São Paulo. Rascunho em elaboração. Disponível em:https://www.ime.usp.br/~mota/bookFiles/livro_AAED.pdf. 

PERSSON, Aladdin. Weighted Interval Scheduling Algorithm Explained. YouTube, 15 fev. 2020. Disponível em: https://www.youtube.com/watch?v=iIX1YvbLbvc. 

QUEM DISSE, Carla. Algoritmos gulosos e Problema das Tarefas Compatíveis. YouTube, 5 maio 2020. Disponível em: https://www.youtube.com/watch?v=PCMcGPknMwk. 

## Tecnologias
- Python 3

##  Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Navegue até a pasta raiz do projeto.
3. Execute o script principal:
   ```bash
   python3 -m src.Main
   ```

## Estrutura do Projeto
- `src/models/`: Definição da classe Atividade.
- `src/dynamicProgramming/`: Lógica da programação dinâmica
- `src/sorting/`: Implementação do Merge Sort.
- `src/greedy/`: Lógica do Algoritmo Guloso.
- `src/tests/modelsTest/`: Lógica da Programação Dinâmica e testes de unidade.
- `src/utils/`: Enums de prioridade e funções de busca.
- `src/Main.py`: Orquestrador dos testes e comparações.

